from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    # Disk Usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    # Network Usage
    net = psutil.net_io_counters()

    network_usage = round(
        (net.bytes_sent + net.bytes_recv) / (1024 * 1024),
        2
    )

    # System Information
    hostname = socket.gethostname()

    operating_system = (
        platform.system() + " " + platform.release()
    )

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return render_template(

        "index.html",

        cpu=cpu_usage,

        memory=memory_usage,

        disk=disk_usage,

        network=network_usage,

        hostname=hostname,

        os=operating_system,

        time=current_time
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )