all: image run

image:
	docker build . -t getupcloud/patroni-healthz:latest

push:
	docker push getupcloud/patroni-healthz:latest

run:
	docker run -p 8080:8080 -e PATRONI_URL=$(PATRONI_URL) -it patroni-healthz:latest
