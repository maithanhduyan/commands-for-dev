# Alpine nginx
- Build docker image
> docker build -t alpine-nginx-web-server .

- Run container 
> docker run -d -p 80:80 alpine-nginx-web-server