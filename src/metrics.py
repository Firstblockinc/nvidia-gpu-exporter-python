from prometheus_client import Gauge

gpu_utilization_metric = Gauge('gpu_utilization', 'GPU Utilization', ['rig', "ip", 'gpu_model', "gpu_id"])
gpu_memory_total_metric = Gauge('gpu_memory_total', 'GPU Memory Total (MB)', ['rig', "ip", 'gpu_model', "gpu_id"])
gpu_memory_free_metric = Gauge('gpu_memory_free', 'GPU Memory Free (MB)', ['rig', "ip", 'gpu_model', "gpu_id"])
gpu_memory_used_metric = Gauge('gpu_memory_used', 'GPU Memory Used (MB)', ['rig', "ip", 'gpu_model', "gpu_id"])
gpu_temperature_metric = Gauge('gpu_temperature', 'GPU Temperature (°C)', ['rig', "ip", 'gpu_model', "gpu_id"])
gpu_power_consumption_metric = Gauge('gpu_power_consumption', 'GPU Power Consumption (W)', ['rig', 'ip', 'gpu_model', 'gpu_id'])
