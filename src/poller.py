from metrics import (
    gpu_utilization_metric,
    gpu_memory_total_metric,
    gpu_memory_free_metric,
    gpu_memory_used_metric,
    gpu_temperature_metric,
)
from snmp import get_snmp_data

def poll_single_rig(rig_ip, rig_label):
    oid_gpu_name = '1.3.6.1.4.1.2021.1'
    oid_gpu_utilization = '1.3.6.1.4.1.2021.2'
    oid_gpu_temp = '1.3.6.1.4.1.2021.3'
    oid_memory_total = '1.3.6.1.4.1.2021.4'
    oid_memory_free = '1.3.6.1.4.1.2021.5'
    oid_memory_used = '1.3.6.1.4.1.2021.6'

    gpu_name = get_snmp_data(oid_gpu_name, rig_ip)
    gpu_utilization = get_snmp_data(oid_gpu_utilization, rig_ip)
    gpu_temp = get_snmp_data(oid_gpu_temp, rig_ip)
    memory_total = get_snmp_data(oid_memory_total, rig_ip)
    memory_free = get_snmp_data(oid_memory_free, rig_ip)
    memory_used = get_snmp_data(oid_memory_used, rig_ip)

    if gpu_name:
        gpu_utilization_metric.labels(rig=rig_label, gpu=gpu_name).set(float(gpu_utilization))
        gpu_temperature_metric.labels(rig=rig_label, gpu=gpu_name).set(float(gpu_temp))
        gpu_memory_total_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_total))
        gpu_memory_free_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_free))
        gpu_memory_used_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_used))
    else:
        print(f"Failed to get GPU data from {rig_ip}")

def poll_all_rigs(rigs):
    for rig in rigs:
        rig_ip, rig_label = rig['ip'], rig['label']
        poll_single_rig(rig_ip, rig_label)
