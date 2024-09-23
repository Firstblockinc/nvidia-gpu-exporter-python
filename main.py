from prometheus_client import start_http_server
import time
import logging
from src.poller import poll_all_rigs
from src.config_loader import load_config

# Configure logging
logging.basicConfig(level=logging.INFO)

## Setup rig objects and provisioning
if __name__ == "__main__":
    config = load_config("config.json")
    rigs = config["rigs"]

    # Start the Prometheus HTTP server
    start_http_server(8000)
    logging.info("Prometheus metrics server started on port 8000.")

    while True:
        logging.info("Polling all rigs for metrics...")
        poll_all_rigs(rigs)
        logging.info("Polling completed. Waiting for the next cycle...")
        time.sleep(300)
