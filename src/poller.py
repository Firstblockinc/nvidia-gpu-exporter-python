import requests
from metrics import (
    gpu_utilization_metric,
    gpu_memory_total_metric,
    gpu_memory_free_metric,
    gpu_memory_used_metric,
    gpu_temperature_metric,
    start_metrics_server
)


def poll_single_rig(rig_ip, rig_label):
    agent_url = f'http://{rig_ip}:5000/data'  # Assuming the agent runs on port 5000

    try:
        response = requests.get(agent_url)
        response.raise_for_status()  # Raise an error for bad responses

        gpu_data = response.json()

        for gpu in gpu_data:
            gpu_name = gpu['name']
            gpu_utilization = gpu['utilization']
            gpu_temp = gpu['temperature']
            memory_total = gpu['memory_total']
            memory_free = gpu['memory_free']
            memory_used = gpu['memory_used']

            gpu_utilization_metric.labels(rig=rig_label, gpu=gpu_name).set(float(gpu_utilization))
            gpu_temperature_metric.labels(rig=rig_label, gpu=gpu_name).set(float(gpu_temp))
            gpu_memory_total_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_total))
            gpu_memory_free_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_free))
            gpu_memory_used_metric.labels(rig=rig_label, gpu=gpu_name).set(float(memory_used))

    except requests.exceptions.RequestException as e:
        print(f"Failed to get GPU data from {rig_ip}: {e}")

def poll_all_rigs(rigs):
        for rig in rigs:
            rig_ip, rig_label = rig['ip'], rig['label']
            poll_single_rig(rig_ip, rig_label)
