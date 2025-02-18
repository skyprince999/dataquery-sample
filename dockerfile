# Use a lightweight base image
FROM alpine:latest

# Set environment variables
ENV DOCKER_CLI_AWESOME="yes"

# Install Docker CLI inside the container
RUN apk add --no-cache docker-cli

# Copy the cleanup script
COPY cleanup.sh /cleanup.sh

# Give execution permission
RUN chmod +x /cleanup.sh

# Run the script when the container starts
CMD ["/cleanup.sh"]
