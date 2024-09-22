from prometheus_client import start_http_server
import time
from poller import poll_all_rigs
from config_loader import load_config

if __name__ == "__main__":
    config = load_config("config.json")
    rigs = config["rigs"]

    # Start Prometheus HTTP server on port 8000
    start_http_server(8000)

    # Poll each rig every 60 seconds
    while True:
        poll_all_rigs(rigs)
        time.sleep(60)
