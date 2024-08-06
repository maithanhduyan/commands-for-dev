# Odoo 15 on Docker

- run
> docker compose -f "Docker\odoo-15\docker-compose.yml" up -d --build 

- stop
> docker compose -f "Docker\odoo-15\docker-compose.yml" down 

- restart
> docker compose -f "Docker\odoo-15\docker-compose.yml" restart 



### Nginx
> docker compose  -f "docker-compose.yml" up -d --build nginx
> docker compose  -f "docker-compose.yml" restart nginx

### Certbot
> docker exec -it certbot certbot renew

> docker exec -it certbot certbot certonly --email tiachop0102@gmail.com --agree-tos --no-eff-email -d tayafood.com

- domain name: tayafood.com
- webroot: /var/www/html

> docker compose  -f "/home/odoo-15/docker-compose.yml" restart certbot

# Backup 
> docker compose  -f "/home/odoo-15/docker-compose.yml" up -d --build backup-odoo
> docker compose  -f "/home/odoo-15/docker-compose.yml" stop backup-odoo
> docker compose  -f "/home/odoo-15/docker-compose.yml" restart backup-odoo

# Odoo
> docker compose  -f "docker-compose.yml" restart odoo 