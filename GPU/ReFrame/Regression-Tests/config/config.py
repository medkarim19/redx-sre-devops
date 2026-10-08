site_configuration = {
    'systems': [
        {
            'name': 'toubkal_supercomputer',
            'descr': 'Toubkal SuperComputer',
            'modules_system': 'lmod',
            'hostnames': ['.*'],
            'partitions': [
                {
                    'name': 'gpu_h100',  
                    'scheduler': 'slurm',
                    'launcher': 'local',  
                    'access': [
                        '-A', 'SW_STACK-373LCD9R8IO-DEFAULT-GPU',
                        '-p', 'gpu_h100',
                        '--qos=premium-gpu-temp',
                        '--gres=gpu:1'
                    ],
                    'environs': ['cuda', 'vasp_h100'],
                },
                {
                    'name': 'gpu',  
                    'scheduler': 'slurm',
                    'launcher': 'local',
                    'access': [
                        '-A', 'sw_stack-373lcd9r8io-default-gpu',
                        '-p', 'gpu',
                        '--gres=gpu:1'
                    ],
                    'environs': ['cuda', 'vasp_a100'],
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'cuda',
            'cc': 'nvcc',
            'cxx': 'nvcc',
            'modules': ['CUDA/12.1.0'],  
        },
        {
            'name': 'vasp_h100',
            'modules': ['vasp/6.5.0-gpu_h100'],
        },
        {
            'name': 'vasp_a100',
            'modules': ['vasp/6.5.0-gpu_a100'],
        }
    ]
}
