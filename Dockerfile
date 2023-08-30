# Define variables.
ARG PORT
ENV SERVER_PORT=${PORT}

# Copy app source code.
COPY src/ /app
