import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class qe_h100(rfm.RunOnlyRegressionTest):
    valid_systems = ['toubkal_supercomputer:gpu_h100']
    valid_prog_environs = ['cuda']
    num_tasks = 1
    num_tasks_per_node = 1
    executable = 'singularity'
    executable_opts = [
        'exec',
        '--nv',
        '-B /home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/espresso:/host_pwd',
        '--pwd', '/host_pwd',
        '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/espresso/quantum_espresso_qe-7.3.1.sif',
        'mpirun', '-np', '1', 'pw.x', '-in', '/host_pwd/quantum/input.in'
    ]
    input_file = 'input.in'
    sourcesdir = '/home/saber.feki-ext/lustre/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/espresso'
    @sanity_function
    def validate_job_done(self):
        return sn.assert_found(r'JOB DONE', self.stdout)
