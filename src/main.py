from prometheus_client import start_http_server
import time
from poller import poll_all_rigs

if __name__ == "__main__":
    # List of rigs to monitor, will require a discovery service
    rigs = [
        {'ip': '192.168.1.101', 'label': 'rig1'},
        {'ip': '192.168.1.102', 'label': 'rig2'},
        # Add more rigs as needed
    ]

    # Start Prometheus HTTP server on port 8000
    start_http_server(8000)

    # Poll each rig every 60 seconds
    while True:
        poll_all_rigs(rigs)
        time.sleep(60)
