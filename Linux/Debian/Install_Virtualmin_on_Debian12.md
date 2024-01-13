# Install Virtualmin on Debian 12

- The easiest way to get the install script onto your server, is to login to your server and use wget or curl. For example:
> wget https://software.virtualmin.com/gpl/scripts/virtualmin-install.sh

- Execute the downloaded install script using a command like the following:
>  sudo sh virtualmin-install.sh

#### Configure Firewall

- It is also recommended to secure your server with a UFW firewall. To do so, install the UFW firewall with the following command:
> apt install ufw -y

~~~~
ufw allow 22
ufw allow 10000
~~~~

- Next, enable the UFW firewall using the command below:
> ufw enable

- Next, verify the firewall with the following command:
> ufw status