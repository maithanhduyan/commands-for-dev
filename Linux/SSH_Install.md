# SSH Install

~~~

sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl enable ssh
 
~~~~


- Install Firewall
> apt install ufw -y
> ufw allow 22
> ufw allow 10000
> ufw enable