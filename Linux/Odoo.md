# [Install Odoo](https://www.odoo.com/documentation/17.0/administration/on_premise/packages.html)
#### Prepare
Odoo needs a PostgreSQL server to run properly.
> sudo apt install postgresql -y
~~~~
 wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
 echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/17.0/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
 sudo apt-get update && sudo apt-get install odoo

 ~~~~

 ### [Source Install](https://www.odoo.com/documentation/17.0/administration/on_premise/source.html)