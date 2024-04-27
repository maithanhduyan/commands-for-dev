# SSH Install

~~~

sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
sudo systemctl start ssh
sudo systemctl enable ssh
 
~~~~
- SSH Server Allow user root
> sudo nano /etc/ssh/sshd_config

Add new line :
> PermitRootLogin yes

Restart SSH server
> sudo sysyemctl restart ssh

- Install Firewall
> apt install ufw -y
> ufw allow 22
> ufw allow 10000
> ufw enable

