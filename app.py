from flask import Flask, render_template
import psutil
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    hostname = socket.gethostname()
    os = platform.system()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        'index.html',
        cpu=cpu,
        memory=memory,
        disk=disk,
        hostname=hostname,
        os=os,
        time=current_time
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)