# CloudOps Monitor - Multi-Branch CI/CD Pipeline

## Project Overview

CloudOps Monitor is a containerized monitoring application that demonstrates a complete DevOps workflow using Git, GitHub, Jenkins, Docker, and Ansible. The project implements a Multi-Branch CI/CD Pipeline that automatically builds and deploys the application whenever code changes are pushed to GitHub.

## Features

* Multi-Branch Pipeline using Jenkins
* Automated Build and Deployment
* Docker Containerization
* Infrastructure Automation with Ansible
* GitHub Webhook Integration
* Continuous Integration and Continuous Deployment (CI/CD)
* Branch-wise Build Management

## Technologies Used

* Git & GitHub
* Jenkins
* Docker
* Ansible
* Python Flask
* Linux (Ubuntu EC2)
* AWS EC2

## Project Structure

```text
cloudops-monitor/
│
├── ansible/
│   ├── deploy.yml
│   └── inventory
│
├── templates/
├── static/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub webhook triggers Jenkins.
3. Jenkins detects the branch change.
4. Docker image is built automatically.
5. Ansible executes deployment tasks.
6. Existing container is removed.
7. New container is launched.
8. Updated application becomes available.

## Docker Commands

Build Image:

```bash
docker build -t cloudops-monitor .
```

Run Container:

```bash
docker run -d -p 5000:5000 --name monitor-container cloudops-monitor
```

## Jenkins Pipeline Stages

### Build Stage

* Checkout source code
* Build Docker image

### Deploy Stage

* Remove old container
* Build updated image
* Deploy new container

## Ansible Deployment

The deployment is automated using Ansible playbooks that:

* Remove old containers
* Build Docker images
* Deploy updated containers

## Future Enhancements

* Kubernetes Deployment
* Docker Hub Integration
* Monitoring with Prometheus and Grafana
* Automated Testing Stage
* Blue-Green Deployment


## License

This project is created for educational and learning purposes.
