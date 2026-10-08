import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class env_check(rfm.RunOnlyRegressionTest):
    def __init__(self):
        super().__init__()
        self.valid_systems = ['toubkal_supercomputer:gpu_h100']
        self.valid_prog_environs = ['*']
        self.descr = 'GPU environment system check using env.sh'
        self.executable = '/home/karim.bezine-ext/lustre/sw_stack-373lcd9r8io/users/karim.bezine-ext/src/reframe/redx_tests/env.sh'
        self.time_limit = '5m'
        self.sanity_patterns = self.sanity_check()
    def sanity_check(self):
        return sn.all([
            sn.assert_found(r'Hostname:', self.stdout),
            sn.assert_found(r'Slurm Version:', self.stdout),
            sn.assert_found(r'slurm 23\.11\.10', self.stdout),
            sn.assert_found(r"Nodes in partition 'gpu':", self.stdout),
            sn.assert_found(r"Nodes in partition 'gpu_h100':", self.stdout),
            sn.assert_found(r'Operating System Version:', self.stdout),
            sn.assert_found(r'Rocky Linux release 8\.10', self.stdout),
            sn.assert_found(r'Kernel Version:', self.stdout),
            sn.assert_found(r'4\.18\.0-553\.27\.1\.el8_10\.x86_64', self.stdout),
            sn.assert_found(r'Mellanox OFED:', self.stdout),
            sn.assert_found(r'24\.07-0\.6\.1\.0\.202411090046', self.stdout),
            sn.assert_found(r"CA 'mlx5_0'", self.stdout),
            sn.assert_found(r"CA 'mlx5_1'", self.stdout),
            sn.assert_found(r'Local Storage Devices:', self.stdout),
            sn.assert_found(r'Filesystem Disk Usage:', self.stdout),
            sn.assert_found(r'Lustre Version:', self.stdout),
            sn.assert_found(r'2\.15\.5', self.stdout),
            sn.assert_found(r'Currently Loaded Modules:', self.stdout),
        ])
