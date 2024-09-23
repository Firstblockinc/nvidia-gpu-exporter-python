import requests
import logging
from metrics import (
    gpu_utilization_metric,
    gpu_memory_total_metric,
    gpu_memory_free_metric,
    gpu_memory_used_metric,
    gpu_temperature_metric,
    gpu_power_consumption_metric
)

logging.basicConfig(level=logging.INFO)


class Rig:
    def __init__(self, ip, label):
        self.ip = ip
        self.label = label

    def gather_gpus_metrics(self):
        agent_url = f'http://{self.ip}:5000/data' 

        try:
            response = requests.get(agent_url)
            response.raise_for_status() 

            gpu_data = response.json()
            for gpu in gpu_data:
                gpu_model = gpu['model']
                gpu_id = gpu['id']
                gpu_utilization = gpu['utilization']
                gpu_temp = gpu['temperature']
                memory_used = gpu['vram_used']
                memory_free = gpu['vram_free']
                memory_total = gpu['vram_total']
                power_consumption = gpu['power_consumption']

                gpu_utilization_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(gpu_utilization))
                gpu_temperature_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(gpu_temp))
                gpu_memory_total_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(memory_total))
                gpu_memory_free_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(memory_free))
                gpu_memory_used_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(memory_used))
                gpu_power_consumption_metric.labels(rig=self.label, ip=self.ip, gpu_model=gpu_model, gpu_id=gpu_id).set(float(power_consumption))

            logging.info(f"Successfully gathered GPU metrics from {self.ip}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get GPU data from {self.ip}: {e}")
