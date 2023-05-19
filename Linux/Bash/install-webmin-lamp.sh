#!/bin/bash

# Update the system
apt update
apt upgrade -y

# Install Webmin
echo "deb https://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list
cd /root
wget https://download.webmin.com/jcameron-key.asc
apt-key add jcameron-key.asc
apt update
apt install webmin -y

# Install LAMP
apt install apache2 mariadb-server php libapache2-mod-php php-mysql -y
mysql_secure_installation

# Configure firewall
ufw allow 10000/tcp
ufw allow in "Apache Full"

# Restart services
systemctl restart apache2
systemctl restart mysql
systemctl restart webmin

echo "Webmin and LAMP have been installed and configured."
echo "You can access Webmin at https://your-server-ip:10000"
