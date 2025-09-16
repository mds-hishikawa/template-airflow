#!/bin/bash
TARGET_USER=$1
TARGET_HOST=$2
REMOTE_PATH="/opt/airflow/dags" # Mude para /opt/spark/jobs, /home/user/notebooks, etc.

echo "🐍 Deploying Python project to ${TARGET_HOST}..."
rsync -avz --delete --exclude='tests' -e "ssh -o StrictHostKeyChecking=no" ./app/src/ "${TARGET_USER}@${TARGET_HOST}:${REMOTE_PATH}/"
echo "✅ Project deployed."