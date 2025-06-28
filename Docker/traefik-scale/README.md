Rất hay! Dùng **Traefik** làm reverse proxy là một giải pháp hiện đại, linh hoạt và mạnh mẽ — đặc biệt phù hợp khi bạn chạy nhiều dịch vụ với Docker.

---

## ✅ Mục tiêu

Chúng ta sẽ dùng **Traefik v2** làm reverse proxy để tự động route 3 dịch vụ tới 3 domain/subdomain:

* `dotcon.vn`
* `mail.dotcon.vn`
* `workflow.dotcon.vn`

Với **Let’s Encrypt tự động**, không cần cấu hình Nginx thủ công!

---

## 📁 Cấu trúc thư mục ví dụ

```
traefik-project/
├── docker-compose.yml
├── traefik/
│   └── traefik.yml
├── services/
│   ├── dotcon/
│   │   └── docker-compose.yml
│   ├── mail/
│   │   └── docker-compose.yml
│   └── workflow/
│       └── docker-compose.yml
```

---

## 1️⃣ `traefik/traefik.yml` (cấu hình Traefik)

```yaml
entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

providers:
  docker:
    exposedByDefault: false

certificatesResolvers:
  letsencrypt:
    acme:
      email: your-email@dotcon.vn
      storage: /letsencrypt/acme.json
      httpChallenge:
        entryPoint: web
```

---

## 2️⃣ `docker-compose.yml` (root - chạy Traefik)

```yaml
version: '3.8'

services:
  traefik:
    image: traefik:v2.11
    container_name: traefik
    command:
      - --api.insecure=true  # Dashboard, nên disable ở production
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false
      - --entrypoints.web.address=:80
      - --entrypoints.websecure.address=:443
      - --certificatesresolvers.letsencrypt.acme.httpchallenge.entrypoint=web
      - --certificatesresolvers.letsencrypt.acme.email=your-email@dotcon.vn
      - --certificatesresolvers.letsencrypt.acme.storage=/letsencrypt/acme.json
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080" # dashboard
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./traefik/traefik.yml:/traefik.yml
      - ./traefik/acme.json:/letsencrypt/acme.json
    networks:
      - web

networks:
  web:
    external: true
```

> ⚠️ Chạy lệnh: `touch traefik/acme.json && chmod 600 traefik/acme.json` trước khi start.

---

## 3️⃣ Một dịch vụ ví dụ: `services/dotcon/docker-compose.yml`

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    container_name: dotcon
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.dotcon.rule=Host(`dotcon.vn`)"
      - "traefik.http.routers.dotcon.entrypoints=web,websecure"
      - "traefik.http.routers.dotcon.tls.certresolver=letsencrypt"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - web

networks:
  web:
    external: true
```

Làm tương tự cho `mail.dotcon.vn` và `workflow.dotcon.vn`, chỉ cần đổi label `Host()` tương ứng.

---

## 4️⃣ Trỏ DNS các domain/subdomain về IP VPS

* `dotcon.vn` → IP VPS
* `mail.dotcon.vn` → IP VPS
* `workflow.dotcon.vn` → IP VPS

---

## 5️⃣ Chạy hệ thống

```bash
# Bước 1: tạo external network
docker network create web

# Bước 2: chạy Traefik
docker compose up -d

# Bước 3: chạy các dịch vụ
cd services/dotcon && docker compose up -d
cd ../mail && docker compose up -d
cd ../workflow && docker compose up -d
```

---

## ✅ Kết quả

* Truy cập `http://dotcon.vn`, `https://mail.dotcon.vn`,... sẽ được proxy chính xác đến từng container.
* HTTPS được cấp tự động bởi Let’s Encrypt.
* Quản lý dễ dàng, mở rộng quy mô cực tốt.

---

1. Chạy lệnh tạo network:
```
docker network create web

```

2. Chạy Traefik:
```
docker compose up -d
```

3. Khởi động từng dịch vụ:

```
cd services/dotcon && docker compose up -d
cd ../mail && docker compose up -d
cd ../workflow && docker compose up -d
```


