### Install Apache on Debian 11

1. Open a terminal window on your Debian 11 system.
2. Update your package index by running the following command:
~~~
    sudo apt update
~~~

3. Install the Apache web server package by running the following command:
~~~
    sudo apt install apache2
~~~

4. After the installation is complete, start the Apache service by running the following command:
~~~
    sudo systemctl start apache2
~~~

5. To check if Apache is running, you can run the following command:
~~~
    sudo systemctl status apache2
~~~
If Apache is running, you should see the message "active (running)".

6. By default, Apache should start automatically on system boot. However, if you need to manually start Apache or set it to start automatically, you can use the following commands:
~~~
    sudo systemctl enable apache2    # to enable automatic start on boot
    sudo systemctl start apache2     # to start Apache service
    sudo systemctl stop apache2      # to stop Apache service
    sudo systemctl restart apache2   # to restart Apache service
~~~

That's it! You should now have Apache installed and running on your Debian 11 system. You can test it by opening a web browser and navigating to http://localhost/. If Apache is running properly, you should see the default Apache page.