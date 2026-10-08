import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class hpl_h100(rfm.RunOnlyRegressionTest):
    descr = 'HPL on H100 GPU'
    valid_systems = ['toubkal_supercomputer:gpu_h100']
    valid_prog_environs = ['cuda']
    num_tasks = 1
    num_gpus_per_node = 1
    time_limit = '10m'
    exclusive_access = True
    # Paths to your container and data
    sif_path = '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/benchmarks/hpc-benchmarks_23.10.sif'
    dat_mount = '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/data'
    executable = 'bash'
    executable_opts = []
    @run_before('run')
    def set_executable_opts(self):
        self.executable_opts = ['-c', f'''
            echo "=== Checking GPU ==="
            nvidia-smi
            echo "=== Checking Singularity Bind ==="
            singularity exec --bind {self.dat_mount}:/mnt {self.sif_path} \
              ls -l /mnt/HPL.dat
            echo "=== Running HPL Benchmark ==="
            singularity exec --nv --bind {self.dat_mount}:/mnt {self.sif_path} \
              mpirun -np 1 /workspace/hpl-linux-x86_64/hpl.sh \
              --dat /mnt/HPL.dat \
              --gpu-affinity 0 \
              --no-multinode \
              --cuda-compat > HPL.out 2>&1
            echo "=== Output ==="
            cat HPL.out
        ''']
    @run_before('setup')
    def do_not_stage_container(self):
        self.readonly_files = []
    @run_before('sanity')
    def set_sanity_patterns(self):
        self.sanity_patterns = sn.all([
            sn.assert_found(r'End of Tests\.', 'HPL.out'),
            sn.assert_found(r'0 tests completed and failed residual checks', 'HPL.out'),
            sn.assert_found(r'0 tests skipped because of illegal input values\.', 'HPL.out')
        ])
