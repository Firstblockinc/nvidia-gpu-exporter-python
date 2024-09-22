from prometheus_client import start_http_server
import time
from src.poller import poll_all_rigs
from src.config_loader import load_config

##setup rig objects and provisiong next
if __name__ == "__main__":
    config = load_config("config.json")
    rigs = config["rigs"]

    start_http_server(8000)

    while True:
        poll_all_rigs(rigs)
        time.sleep(300)
