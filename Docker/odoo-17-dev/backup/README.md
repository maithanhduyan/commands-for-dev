# Auto backup odoo

> python -m venv venv
> venv\Scripts\activate

## Build Backup Image
> docker build --pull --rm -f "Docker\odoo-17\backup\Dockerfile" -t odoo-backup:latest "Docker\odoo-17\backup" 