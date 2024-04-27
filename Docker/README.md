# Docker

> docker compose -f "compose.yml" up -d --build

> docker logs -f nginx

> docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo@2024 -e POSTGRES_DB=postgres --name db postgres:15
> docker stop db