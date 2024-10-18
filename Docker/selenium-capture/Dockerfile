# For more information, please refer to https://aka.ms/vscode-docker-python
# Sử dụng Python 3.12 làm base image
FROM python:3.12-slim as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Cài đặt curl và các phụ thuộc cần thiết
RUN apt-get update && apt-get install -y curl && apt-get clean

# Cập nhật pip
RUN pip install --upgrade pip

COPY . .

# Install pip requirements
COPY ./app/requirements.txt .
RUN python3 -m pip install -r requirements.txt


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python3","./app/src/main.py"]
