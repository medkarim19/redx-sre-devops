import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class knn_cuda_a100(rfm.RunOnlyRegressionTest):
    valid_systems = ['toubkal_supercomputer:gpu']
    valid_prog_environs = ['*']
    num_tasks = 1
    num_tasks_per_node = 1
    executable = 'singularity'
    executable_opts = [
        'exec',
        '--nv',
        '-B /home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/knn_cuda/shared:/mnt',
        '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/knn_cuda/python-cuda117_1.0.6.sif',
        'python3.10', '/mnt/tests/test.py'
    ]
    @sanity_function
    def validate_job_done(self):
        return sn.assert_found(r'KNN CUDA is working fine on GPU!', self.stdout)
