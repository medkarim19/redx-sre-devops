#!/bin/bash
echo "========== GPU System Check =========="
echo -e "\nHostname:"
hostname
echo -e "\nSlurm Version:"
sinfo -V
echo -e "\nNodes in partition 'gpu':"
sinfo -p gpu -N
echo -e "\nNodes in partition 'gpu_h100':"
sinfo -p gpu_h100 -N
echo -e "\nOperating System Version:"
cat /etc/redhat-release
echo -e "\nKernel Version:"
uname -r
echo -e "\nNVIDIA GPU Summary:"
nvidia-smi --query-gpu=name,memory.total,memory.free,driver_version,compute_mode --format=csv || echo "nvidia-smi not found or no GPUs detected"
echo -e "\nNVIDIA Driver Version:"
cat /proc/driver/nvidia/version 2>/dev/null || echo "Driver info not available"
echo -e "\nCUDA Version:"
nvcc --version 2>/dev/null || echo "nvcc not found"
echo -e "\nDetailed NVIDIA GPU Info (Clocks, Memory, Power, Temp):"
nvidia-smi -q -d TEMPERATURE,UTILIZATION,POWER,MEMORY || echo "nvidia-smi -q failed"
echo -e "\nGPU Topology (NVLink/PCIe):"
nvidia-smi topo -m || echo "Topology info not available"
echo -e "\nMIG Configuration (if supported):"
nvidia-smi mig -lci 2>/dev/null || echo "MIG not supported or not enabled"
echo -e "\nMellanox OFED:"
ofed_info -n 2>/dev/null || echo "OFED not found"
echo -e "\nIB Adapters and Firmware:"
ibstat 2>/dev/null || echo "IB not found"
echo -e "\nLocal Storage Devices:"
lsblk
echo -e "\nFilesystem Disk Usage:"
df -h
echo -e "\nLustre Version:"
cat /sys/fs/lustre/version 2>/dev/null || echo "Lustre not found"

echo -e "\nLoaded Modules:"
module list 2>&1 || echo "Modules not available or not loaded"
echo -e "\n========== End of GPU System Check =========="
