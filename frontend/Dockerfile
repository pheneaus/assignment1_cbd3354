# Use a base image that has a web server (e.g., Nginx) and any necessary dependencies
FROM nginx:latest

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Copy the HTML file into the container
COPY index.html .

# Expose the port the frontend application will be listening on
EXPOSE 80

# Start the web server
CMD ["nginx", "-g", "daemon off;"]
