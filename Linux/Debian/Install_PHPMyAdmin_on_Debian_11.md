### To install phpMyAdmin on Debian, you can follow these steps:

1. Update the package index and upgrade the system:
~~~
    sudo apt-get update
    sudo apt-get upgrade

~~~ 

2. Install phpMyAdmin and its dependencies:
~~~
    sudo apt-get install phpmyadmin

~~~

3. During the installation process, you will be prompted to choose a web server to configure. Select "apache2" using the spacebar and press "Enter" to continue.

4. When prompted, choose "yes" to configure the database for phpMyAdmin.

5. You will then be prompted to enter the password for the phpMyAdmin administrative user. Choose a strong password and remember it, as you will need it later.

6. After the installation is complete, you can verify that phpMyAdmin is working by opening a web browser and navigating to the following URL:
~~~
    http://your_server_ip/phpmyadmin

~~~
Replace "your_server_ip" with the IP address of your server.

7. You should see the phpMyAdmin login page. Log in with the username "phpmyadmin" and the password you chose during the installation.

That's it! You have now installed phpMyAdmin on your Debian server and can use it to manage your MySQL or MariaDB databases.


Note:

Secure MariaDB
Configure basic MariaDB security features by launching a built-in script:
~~~~
sudo mysql_secure_installation

~~~~
As you have not yet set a root password for your database, hit Enter to skip the initial query. Complete the following queries:

Switch to unix_socket authentication [Y/n] - Enter n to skip.
Set root password? [Y/n] - Type y and press Enter to create a strong root password for your database. If you already have a root password, enter n to answer the Change the root password question.
Remove anonymous users? [Y/n] - Type y and press Enter.
Disallow root login remotely? [Y/n] - Type y and press Enter.
Remove test database and access to it? [Y/n] - Type y and confirm with Enter.
Reload privilege tables now? [Y/n] - Type y and confirm with Enter.
The output shows the MariaDB installation is now secure.



[How to Install phpMyAdmin on Debian 11](https://phoenixnap.com/kb/how-to-install-phpmyadmin-on-debian)