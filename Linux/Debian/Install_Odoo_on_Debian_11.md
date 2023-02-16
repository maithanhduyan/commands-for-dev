### Install Odoo on Debian 11
1. Update the system packages:
~~~
	sudo apt update
	sudo apt upgrade
~~~

2. Install PostgreSQL database server:
~~~
	sudo apt install postgresql
~~~

3. Create a PostgreSQL user and database for Odoo:
~~~
	sudo su - postgres
	createuser --createdb --username postgres --no-createrole --no-superuser openpg
	createdb --username postgres --owner odoo --encoding UTF8 --template template0 odoo_db
	exit
~~~

4. Install the required Python libraries and dependencies:
~~~
	sudo apt-get install python3-pip python3-dev build-essential libxml2-dev libxslt1-dev libevent-dev libsasl2-dev libldap2-dev libpq-dev libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev libtiff5-dev libopenjp2-7-dev libblas-dev liblapack-dev libatlas-base-dev gfortran python-dev libssl-dev
~~~

5. Install the wkhtmltopdf package:
~~~
	sudo apt install wkhtmltopdf
~~~

6. Install Odoo from the source:
~~~
	sudo mkdir /opt/odoo
	sudo apt install git
	sudo git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 /opt/odoo/odoo
	sudo apt install python3-venv
	sudo python3 -m venv /opt/odoo/venv
	sudo /opt/odoo/venv/bin/pip install wheel
	sudo /opt/odoo/venv/bin/python3 pip install --upgrade pip
	sudo /opt/odoo/venv/bin/pip install -r /opt/odoo/odoo/requirements.txt
~~~

7. Create a configuration file for Odoo:
~~~
	sudo mkdir /etc/odoo
	sudo cp /opt/odoo/odoo/debian/odoo.conf /etc/odoo/odoo.conf
	sudo nano /etc/odoo/odoo.conf
~~~	
Edit the file as follows:
~~~
	[options]
	addons_path = /opt/odoo/odoo/addons
	admin_passwd = admin
	csv_internal_sep = ,
	db_host = localhost
	db_maxconn = 64
	db_name = False
	db_port = 5432
	db_user = openpg
	db_password = openpgpwd
	db_sslmode = prefer
	dbfilter = False
	default_productivity_apps = True

	http_enable = True
	http_interface = 
	http_port = 8069
	list_db = True
	log_db = False
	log_db_level = warning
	log_handler = :INFO
	log_level = info
	logfile = /etc/odoo/odoo.log
~~~

8. Create a service file for Odoo:
~~~
	sudo nano /etc/systemd/system/odoo.service
~~~
Add the following lines to the file: 
~~~	
    [Unit]
	Description=Odoo
	After=postgresql.service

	[Service]
	Type=simple
	User=root
	ExecStart=/opt/odoo/venv/bin/python3 /opt/odoo/odoo/odoo-bin -c /etc/odoo/odoo.conf
	StandardOutput=journal+console

	[Install]
	WantedBy=multi-user.target
~~~

9. Start the Odoo service and enable it to start at boot:
~~~
	sudo systemctl start odoo
	sudo systemctl enable odoo
~~~	

Reload con file odoo.service
~~~
	sudo systemctl daemon-reload
~~~

That's it! You should now be able to access Odoo by navigating to your server's IP address in a web browser.


