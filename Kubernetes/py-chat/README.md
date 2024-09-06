- Build a Docker Image
> docker build -t python-chat-app .

- Run Docker
> docker run -p 5000:5000 python-chat-app

# K8s
> kubectl apply -f deploy/deployment.yaml
> kubectl apply -f deploy/service.yaml
> kubectl apply -f deploy/nginx-deployment.yaml

- Delete
> kubectl delete -f deploy/deployment.yaml
> kubectl delete -f deploy/service.yaml
> kubectl delete -f deploy/nginx-deployment.yaml