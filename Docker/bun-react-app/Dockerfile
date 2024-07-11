# Use the official Bun image as the base image
FROM oven/bun:latest

# Set the working directory
WORKDIR /app

# Copy the app files to the container
COPY . .

# Install dependencies
RUN bun install

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["bun", "start"]
