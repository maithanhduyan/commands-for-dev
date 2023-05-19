# NSSM - the Non-Sucking Service Manager

nssm is a service helper which doesn't suck. srvany and other service helper programs suck because they don't handle failure of the application running as a service. If you use such a program you may see a service listed as started when in fact the application has died. nssm monitors the running service and will restart it if it dies. With nssm you know that if a service says it's running, it really is. Alternatively, if your application is well-behaved you can configure nssm to absolve all responsibility for restarting it and let Windows take care of recovery actions.

nssm logs its progress to the system Event Log so you can get some idea of why an application isn't behaving as it should.

nssm also features a graphical service installation and removal facility. Prior to version 2.19 it did suck. Now it's quite a bit better.

### Create nginx-service on Windows OS
- Install a service
~~~~
    nssm install nginx-service 
~~~~

- Edit service
~~~~
    nssm edit nginx-service 
~~~~

- Remove a service
~~~~
    nssm remove nginx-service 
~~~~