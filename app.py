from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

# ================= DASHBOARD =================

@app.route("/")
def dashboard():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    network = psutil.net_io_counters()
    network_usage = round(
        (network.bytes_sent + network.bytes_recv) / (1024 * 1024), 2
    )

    hostname = socket.gethostname()

    operating_system = platform.system()

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        network=network_usage,
        hostname=hostname,
        os=operating_system,
        time=current_time
    )

# ================= METRICS =================

@app.route("/metrics")
def metrics():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    network = psutil.net_io_counters()

    network_usage = round(
        (network.bytes_sent + network.bytes_recv) / (1024 * 1024), 2
    )

    return render_template(
        "metrics.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        network=network_usage
    )

# ================= ALERTS =================

@app.route("/alerts")
def alerts():

    disk = psutil.disk_usage('/').percent

    memory = psutil.virtual_memory().percent

    cpu = psutil.cpu_percent(interval=1)

    alerts = []

    if cpu > 80:
        alerts.append("High CPU Usage Detected")

    if memory > 80:
        alerts.append("High Memory Usage Detected")

    if disk > 80:
        alerts.append("Disk Space Almost Full")

    if len(alerts) == 0:
        alerts.append("All Systems Running Normally")

    return render_template("alerts.html", alerts=alerts)

# ================= CONTAINERS =================

@app.route("/containers")
def containers():

    containers = [
        {
            "name": "cloudops-monitor",
            "status": "Running"
        },
        {
            "name": "jenkins",
            "status": "Running"
        },
        {
            "name": "docker-engine",
            "status": "Healthy"
        }
    ]

    return render_template(
        "containers.html",
        containers=containers
    )

# ================= REPORTS =================

@app.route("/reports")
def reports():

    report_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    return render_template(
        "reports.html",
        report_time=report_time
    )

# # ================= SETTINGS =================

# @app.route("/settings")
# def settings():

#     return render_template("settings.html")

# ================= RUN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)