# Install minimal Python 3.
FROM python:3.7-alpine

# Define variables.
ARG PORT
ENV SERVER_PORT=${PORT}

# Install Python requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Copy app source code.
COPY src/ /app
