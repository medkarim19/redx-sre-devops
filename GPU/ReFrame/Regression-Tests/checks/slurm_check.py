import reframe as rfm
import reframe.utility.sanity as sn
import getpass
import subprocess
@rfm.simple_test
class SlurmCheckTest(rfm.RunOnlyRegressionTest):
    variant = parameter(['slurmctld', 'squeue', 'sacct'])
    partition = parameter(['gpu', 'gpu_h100'])
    descr = "Reframe Slurm Check Test"
    valid_systems = ['*']
    valid_prog_environs = ['*']
    
    @run_before('run')
    def check_partition_resources(self):
        if self.partition in ('gpu', 'gpu_h100'):
            try:
                sinfo_output = subprocess.check_output(
                    ['sinfo', '-p', self.partition, '--noheader', '-o', '%T']
                ).decode().lower()
                if not any(state in sinfo_output for state in ['idle', 'mix']):
                    self.skip(f'No available resources in partition "{self.partition}", skipping test.')
            except Exception as e:
                self.skip(f'Failed to check partition "{self.partition}" resources: {e}')
    @run_before('run')
    def set_executable(self):
        user = getpass.getuser()
        if self.variant == "slurmctld":
            self.executable = 'scontrol ping'
            self.sanity_patterns = sn.assert_found(
                r'Slurmctld\(primary\) at .* is UP',
                self.stdout
            )
        elif self.variant == "squeue":
            self.executable = f'squeue -u {user}'
            self.sanity_patterns = sn.assert_found(r'NODELIST', self.stdout)
        elif self.variant == "sacct":
            self.executable = f'sacct -u {user}'
            self.sanity_patterns = sn.assert_found(r'JobID\s+JobName\s+Partition', self.stdout)
