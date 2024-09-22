from prometheus_client import start_http_server, Gauge

# Define Prometheus metrics for each attribute we want to collect
gpu_utilization_metric = Gauge('gpu_utilization', 'GPU Utilization', ['rig', 'gpu'])
gpu_memory_total_metric = Gauge('gpu_memory_total', 'GPU Memory Total (MB)', ['rig', 'gpu'])
gpu_memory_free_metric = Gauge('gpu_memory_free', 'GPU Memory Free (MB)', ['rig', 'gpu'])
gpu_memory_used_metric = Gauge('gpu_memory_used', 'GPU Memory Used (MB)', ['rig', 'gpu'])
gpu_temperature_metric = Gauge('gpu_temperature', 'GPU Temperature (°C)', ['rig', 'gpu'])
