from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Disk
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # Network
    network = psutil.net_io_counters()
    bytes_sent = round(network.bytes_sent / (1024 * 1024), 2)
    bytes_recv = round(network.bytes_recv / (1024 * 1024), 2)

    # System info
    hostname = socket.gethostname()
    operating_system = platform.system()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        cpu=cpu_usage,
        memory=memory_usage,
        disk=disk_usage,
        sent=bytes_sent,
        recv=bytes_recv,
        hostname=hostname,
        os=operating_system,
        time=current_time
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)