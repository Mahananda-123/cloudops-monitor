from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

# EMAIL LIBRARIES
import smtplib
from email.mime.text import MIMEText

# ENV LIBRARIES
from dotenv import load_dotenv
import os

app = Flask(__name__)

# LOAD ENV VARIABLES
load_dotenv()

# ================= EMAIL ALERT FUNCTION =================

def send_email_alert(subject, message):

    sender_email = os.getenv("EMAIL_USER")

    sender_password = os.getenv("EMAIL_PASS")

    receiver_email = os.getenv("RECEIVER_EMAIL")

    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print("Email Alert Sent Successfully")

    except Exception as e:

        print("Email Error:", e)

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

    # ALERTS
    alerts = []

    if cpu > 80:

        alerts.append("High CPU Usage Detected")

        send_email_alert(
            "CloudOps CPU Alert",
            f"CPU Usage is High: {cpu}%"
        )

    if memory > 85:

        alerts.append("High Memory Usage Detected")

        send_email_alert(
            "CloudOps Memory Alert",
            f"Memory Usage is High: {memory}%"
        )

    if disk > 90:

        alerts.append("Low Disk Space Warning")

        send_email_alert(
            "CloudOps Disk Alert",
            f"Disk Usage is High: {disk}%"
        )

    if len(alerts) == 0:

        alerts.append("All Systems Running Normally")

    return render_template(
        "index.html",
        cpu=cpu,
        memory=memory,
        disk=disk,
        network=network_usage,
        hostname=hostname,
        os=operating_system,
        time=current_time,
        alerts=alerts
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
def alerts_page():

    disk = psutil.disk_usage('/').percent

    memory = psutil.virtual_memory().percent

    cpu = psutil.cpu_percent(interval=1)

    alerts = []

    if cpu > 80:
        alerts.append("High CPU Usage Detected")

    if memory > 85:
        alerts.append("High Memory Usage Detected")

    if disk > 90:
        alerts.append("Low Disk Space Warning")

    if len(alerts) == 0:
        alerts.append("All Systems Running Normally")

    return render_template(
        "alerts.html",
        alerts=alerts
    )

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

# ================= RUN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)