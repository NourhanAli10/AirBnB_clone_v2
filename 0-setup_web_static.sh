#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt update -y
sudo apt install nginx -y
sudo ufw allow 'Nginx HTTP'
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
echo "Hello from the server" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '52 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;'  /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
