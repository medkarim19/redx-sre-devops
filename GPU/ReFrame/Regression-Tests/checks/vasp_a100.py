import reframe as rfm
import reframe.utility.sanity as sn
@rfm.simple_test
class vasp_h100(rfm.RunOnlyRegressionTest):
    valid_systems = ['toubkal_supercomputer:gpu']
    valid_prog_environs = ['vasp_a100']
    sourcesdir = '/srv/lustre01/project/sw_stack-373lcd9r8io/users/saber.feki-ext/karim/vasp_test'
    num_tasks = 1
    num_tasks_per_node = 1
    num_cpus_per_task = 1
    exclusive_access = True
    use_multithreading = False
    executable = 'mpirun'
    executable_opts = ['-np', '1', 'vasp_std']
    @sanity_function
    def validate_vasp_run(self):
        return sn.assert_found(r'reached required accuracy', self.stdout)
