### Install Redmine on Debian 11

#### 
1. To install Redmine on Debian 11, you can follow the steps below:

Update the package index:
~~~~
sudo apt-get update

~~~~

2. Install the necessary dependencies:
~~~~
sudo apt-get install -y apache2 libapache2-mod-passenger mariadb-server ruby ruby-dev zlib1g-dev liblzma-dev libmariadb-dev-compat libmariadb-dev libpq-dev libmagickcore-dev libmagickwand-dev imagemagick libcurl4-openssl-dev nodejs npm

~~~~

3. Install the latest version of Bundler:
~~~~
sudo gem install bundler

~~~~

4. Download Redmine:
~~~~
cd /var/www/html
sudo wget --no-check-certificate https://www.redmine.org/releases/redmine-5.0.4.tar.gz
sudo tar xzf redmine-5.0.4.tar.gz

~~~~

5. Rename the extracted directory:
~~~~
sudo mv redmine-5.0.4 redmine

~~~~

6. Set the ownership and permissions of the Redmine directory:
~~~~
sudo chown -R www-data:www-data /var/www/html/redmine
sudo chmod -R 755 /var/www/html/redmine

~~~~
Create database
~~~~
    sudo mysql -u root -p

~~~~
With name: redmine
~~~~
    CREATE DATABASE redmine CHARACTER SET utf8mb4;
    CREATE USER 'redmine'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON redmine.* TO 'redmine'@'localhost';
    FLUSH PRIVILEGES;
    exit
~~~~

~~~~
cd /var/www/html/redmine/config
sudo cp configuration.yml.example configuration.yml
sudo nano configuration.yml

cd /var/www/html/redmine/config
sudo cp database.yml.example database.yml
sudo nano database.yml

~~~~

7. Install the necessary Ruby gems:
~~~~
cd /var/www/html/redmine
sudo bundle install --without development test

~~~~

8. Generate a secret key for Redmine:
~~~~
sudo bundle exec rake generate_secret_token

~~~~

9. Configure the database settings:
~~~~
sudo cp config/database.yml.example config/database.yml
sudo nano config/database.yml

~~~~
In the database.yml file, replace the database configuration with your own MySQL or MariaDB credentials.

10. Initialize the database:
~~~~
sudo bundle exec rake db:migrate RAILS_ENV=production
sudo bundle exec rake redmine:load_default_data RAILS_ENV=production REDMINE_LANG=en

~~~~

11. Configure Apache to serve Redmine:
~~~~
sudo nano /etc/apache2/sites-available/redmine.conf

~~~~

In the file, paste the following configuration:
~~~~
<VirtualHost *:80>
    ServerName localhost
    ServerAlias localhost/redmine
    DocumentRoot /var/www/html/redmine/public

    PassengerRuby /usr/bin/ruby
    PassengerAppEnv production
    PassengerStartTimeout 600
    PassengerMaxPoolSize 20

    <Directory "/var/www/html/redmine/public">
        Require all granted
        Options -MultiViews
        PassengerEnabled on
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

~~~~

12. Enable the Redmine virtual host:
~~~~
sudo a2ensite redmine.conf
sudo systemctl reload apache2

~~~~