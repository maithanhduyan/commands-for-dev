# Odoo 15 on Docker

### on Windows
- run
> docker compose -f "Docker\odoo-17\docker-compose.yml" up -d --build 

- stop
> docker compose -f "Docker\odoo-17\docker-compose.yml" down 

- restart
> docker compose -f "Docker\odoo-17\docker-compose.yml" restart 

### on Debian

- run
> docker compose -f "/home/odoo-17/Docker-compose.yml" up -d --build 

- stop
> docker compose -f "/home/odoo-17/Docker-compose.yml" down 

- restart
> docker compose -f "/home/odoo-17/Docker-compose.yml" restart 


### Deploy
- Create new user non root
> adduser odoo-17
> usermod -aG sudo odoo-17

