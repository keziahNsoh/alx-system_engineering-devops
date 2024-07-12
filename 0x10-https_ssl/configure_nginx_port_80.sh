#!/bin/bash

# Function to check if Nginx is installed and running
check_nginx() {
    if ! command -v nginx &> /dev/null; then
        echo "Nginx is not installed. Installing..."
        sudo apt-get update
        sudo apt-get install -y nginx
    fi

    if ! systemctl is-active --quiet nginx; then
        echo "Starting Nginx..."
        sudo systemctl start nginx
    fi
}

# Function to configure Nginx to listen on port 80 for all IPv4 IPs
configure_nginx() {
    # Define default Nginx server block configuration
    sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        root /var/www/html;
        index index.html;
    }
}
EOF

    # Enable the default site
    sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

    # Restart Nginx to apply the configuration
    sudo systemctl restart nginx
}

# Main script execution
check_nginx
configure_nginx

# Check if Nginx is listening on port 80 for all IPv4 IPs
echo "Checking Nginx status..."
if sudo netstat -tuln | grep ':80 .* LISTEN'; then
    echo "Nginx is listening on port 80 for all IPv4 IPs"
else
    echo "Failed to configure Nginx to listen on port 80 for all IPv4 IPs"
fi

