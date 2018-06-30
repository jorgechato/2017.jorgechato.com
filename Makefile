.PHONY: deploy backend db

default: deploy

deploy: rm db pull back

back:
	docker run -p 8000:8000 --env-file env/jorgechato.com/${ENV}.env --link database:database --restart on-failure --name backend -d quay.io/orggue/jorgechato

db:
	docker run -p 5432:5432 --env-file env/jorgechato.com/${ENV}.env -v dbdata:/var/lib/postgresql/data --restart on-failure --name database -d postgres:alpine

rm: rmb rmd

rmb:
	docker rm -f backend

rmd:
	docker rm -f database

clear:
	rm -rf out

collect:
	python manage.py collectstatic

pull:
	docker pull quay.io/orggue/jorgechato

build:
	docker rmi -f backend
	docker rmi -f quay.io/orggue/jorgechato
	docker build -t backend .
	docker tag backend quay.io/orggue/jorgechato
