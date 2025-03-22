# Use Node.js base image
FROM node:latest

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (needed for installing dependencies)
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all project files (including src, public, etc.)
COPY . .

# Expose the development server port
EXPOSE 8080

# Start the development server (usually for development)
CMD ["npm", "run", "serve"]

