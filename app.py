from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    hostname = socket.gethostname()
    system = platform.system()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        'index.html',
        cpu=cpu,
        memory=memory,
        disk=disk,
        hostname=hostname,
        system=system,
        time_now=time_now
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)