# Personal web page
[![Docker Repository on Quay](https://quay.io/repository/orggue/jorgechato/status "Docker Repository on Quay")](https://quay.io/repository/orggue/jorgechato)
[![jorgechato.com](https://img.shields.io/badge/web-jorgechato.com-orange.svg)](https://jorgechato.com)

To run it you will need a /env/ folder with some .env files:

```yaml
# dev.env
SECRET_KEY="XXX"

git_user=xxx
git_pass=xxx

instagram_id=xxx
access_token=xxx
client_secret=xxx

email=xxx

DATABASE_HOST=xxx
POSTGRES_USER=xxx
POSTGRES_DB=xxx
POSTGRES_PASSWORD=xxx

SUPERUSER_PWD=xxx
SUPERUSER_NAME=xxx
```

```bash
env
├── jorgechato.com
│   ├── Makefile
│   ├── README.md
│   ├── config
│   │   └── nginx
│   │       ├── certs
│   │       │   ├── server.crt
│   │       │   └── server.key
│   │       └── nginx.conf
│   ├── dev.env
│   ├── docker-compose.yml
│   ├── env.sh
│   └── prod.env
└── utilities
    ├── install-docker-deb9.sh
    └── wait-for-it.sh
```
