# NVIDIA GPU Metrics Exporter

This project is a simple HTTP-based exporter for NVIDIA GPU metrics using Flask and Prometheus. It collects various GPU metrics and exposes them for monitoring and visualization.

## Features

- Collects GPU metrics such as utilization, memory usage, and temperature.
- Exposes metrics in a format that Prometheus can scrape.
- Supports multiple rigs, allowing easy monitoring of multiple GPU machines.

## Requirements

- Python 3.x
- Flask
- Prometheus Client
- NVIDIA PyNVML

## Installation

1. Clone the repository:

   ```bash
   git clone https://your-repo-url.git
   cd your-repo-directory
