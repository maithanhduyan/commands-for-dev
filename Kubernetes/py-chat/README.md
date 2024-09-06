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

# Helm 
- Install Helm on windows
> winget install Helm.Helm

- Install Helm on linux
```
    curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
    sudo apt-get install apt-transport-https --yes
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
    sudo apt-get update
    sudo apt-get install helm
```

- Create helm directories structure
> cd deploy/k8s/helm
> helm create py-chat