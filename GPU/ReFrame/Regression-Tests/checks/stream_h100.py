import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class stream_h100(rfm.RunOnlyRegressionTest):
    descr = 'STREAM on H100 GPU'
    valid_systems      = ['toubkal_supercomputer:gpu_h100']
    valid_prog_environs= ['cuda']
    num_tasks          = 1
    num_gpus_per_node  = 1
    time_limit         = '10m'
    exclusive_access   = True
    # Paths to your container and data
    sif_path  = '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/benchmarks/hpc-benchmarks_23.10.sif'
    dat_mount = '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/data'
    executable      = 'bash'
    executable_opts = []
    @run_before('run')
    def set_executable_opts(self):
        self.executable_opts = ['-c', f'''
            echo "=== Checking GPU ==="
            nvidia-smi
            echo "=== Checking Singularity Bind ==="
            singularity exec --bind {self.dat_mount}:/mnt {self.sif_path} \
              ls -l /mnt/HPL.dat
            echo "=== Running STREAM Benchmark ==="
            singularity run --nv {self.sif_path} \
              /workspace/stream-gpu-linux-x86_64/stream-gpu-test.sh --n 1300000000 \
              --dat /mnt/hpcg.dat \
              > STREAM.out 2>&1
            
            cat STREAM.out
        ''']
    @run_before('setup')
    def do_not_stage_container(self):
        self.readonly_files = []
    @sanity_function
    def validate_gpu_and_hpl(self):
        return sn.all([
        sn.assert_found(r'Copy', self.stdout),
        sn.assert_found(r'Scale', self.stdout),
        sn.assert_found(r'Add', self.stdout),
        sn.assert_found(r'Triad', self.stdout)
        ])
