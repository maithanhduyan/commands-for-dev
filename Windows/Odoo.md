# All in One Odoo on Windows OS
### Install Odoo Python dependencies
- Install requirements
~~~~
C:\odoo\python\python.exe -m pip install -r requirements.txt
~~~~
### Postgresql Config:

~~~~
    max_connections = 200
    shared_buffers = 1600MB
    effective_cache_size = 4GB
    maintenance_work_mem = 600MB
    checkpoint_completion_target = 0.7
    wal_buffers = 16MB
    default_statistics_target = 100
    random_page_cost = 1.1
    #effective_io_concurrency = 200  <----- ????
    work_mem = 64MB
    min_wal_size = 1GB
    max_wal_size = 2GB
    max_worker_processes = 4
    max_parallel_workers_per_gather = 2

~~~~

### clear-cache-python-on-window
~~~~
    python -Bc "import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]"
    python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]"
~~~~

### create-odoo-service

- create
~~~~
C:\nssm\win64\nssm.exe install odoo-server-15.0 "C:\odoo\python\python.exe" "C:\odoo\odoo\odoo-bin"
~~~~
- Delete Odoo service
~~~~
sc delete odoo-server
~~~~
or using nssm
~~~~
C:\nssm\win64\nssm.exe remove odoo-server
~~~~
- Edit Odoo service
~~~~
C:\nssm\win64\nssm.exe edit odoo-server
~~~~
- Start Odoo
~~~~
C:\odoo\python\python.exe ./odoo-bin -c odoo.conf
~~~~

### Change Odoo title file 
\odoo\addons\web\static\src\webclient\webclient.js
at line 36 :
~~~~
this.title.setParts({ zopenerp: "TAYA" }); // zopenerp is easy to grep
~~~~


### Create bat file for restart Nginx

~~~~
@ECHO OFF
taskkill /f /IM nginx.exe
start nginx
EXIT
~~~~

### Create bat file to stop Nginx
~~~~
@ECHO OFF
wmic process where name='nginx.exe' delete
~~~~

### Odoo high performance turning

~~~~
db_maxconn = 200
limit_memory_hard = 13690208256
limit_memory_soft = 11408506880
limit_time_cpu = 600
limit_time_real = 1200
limit_request = 8192
max_cron_threads = 2
workers = 16
~~~~

### Preferences Link
- [how-to-optimize-an-odoo-server-postgresql](https://www.cybrosys.com/blog/how-to-optimize-an-odoo-server-postgresql)
- [Odoo 16 documents](https://www.odoo.com/documentation/16.0/index.html)