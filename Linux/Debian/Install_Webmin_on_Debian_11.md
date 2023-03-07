### Install Webmin on Debian 11
1. Update the package repository index using the following command:
~~~
    sudo apt update
~~~

2. Install the necessary dependencies required by Webmin using the following command:
~~~
	sudo apt install -y curl gnupg2 software-properties-common apt-transport-https

~~~

3. Add the Webmin GPG key using the following command:
~~~
	curl -fsSL https://download.webmin.com/jcameron-key.asc | sudo gpg --dearmor -o /usr/share/keyrings/webmin-archive-keyring.gpg

~~~

4. Add the Webmin repository to the list of package sources by creating a new file named webmin.list in the /etc/apt/sources.list.d/ directory with the following command:
~~~
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/webmin-archive-keyring.gpg] https://download.webmin.com/download/repository sarge contrib" | sudo tee /etc/apt/sources.list.d/webmin.list > /dev/null

~~~

5. Update the package repository index again to include the Webmin repository using the following command:
~~~
	sudo apt update

~~~

6. Install Webmin using the following command:
~~~
	sudo apt install -y webmin
	
~~~
7. By default, Webmin listens on port 10000. To access the Webmin web interface, open a web browser and go to https://<your-server-ip>:10000. Note that you may need to allow incoming traffic on port 10000 in your firewall if it is enabled.
That's it! You should now have Webmin installed and ready to use on your Debian 11 system.
	