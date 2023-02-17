### Install Apache, PHP, MariaDB
1. Update the package index and upgrade the system:
~~~
	sudo apt-get update
	sudo apt-get upgrade

~~~
2. Install Apache web server:
~~~
	sudo apt-get install apache2

~~~

3. Install PHP and required modules:
~~~
	sudo apt-get install php libapache2-mod-php php-mysql php-curl php-gd php-json php-mbstring php-xml php-zip

~~~

4. Install MySQL or MariaDB database server:
~~~
	sudo apt-get install mysql-server

~~~
For MariaDB:
~~~
	sudo apt-get install mariadb-server

~~~
5. During the installation process, you will be prompted to set a root password for the database server. Make sure to set a strong password and remember it, as you will need it later.

6. Once the installation is complete, you can verify that Apache and PHP are working by creating a PHP file with the following contents:
~~~
<?php
phpinfo();
?>

~~~
Save the file as info.php in the /var/www/html directory.

7. Open a web browser and navigate to the URL for your server with /info.php appended to it. For example, if your server's IP address is 10.0.2.15, you can access the PHP info file by visiting:
~~~
http://10.0.2.15/info.php

~~~

8. If everything is working correctly, you should see a page with information about your PHP installation.

That's it! You have now installed Apache, PHP, and MySQL or MariaDB on your Debian server and can proceed with the installation of Roundcube webmail.