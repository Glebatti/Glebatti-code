run :
	docker run -d -p 3000:3000 -v logs:/app/data --name logsapp logsapp:volumes
run-dev:
	docker run -d -p 3000:3000 -v "/Work Python/Docker_NodeJS:/app" -v /app/node_modules -v logs:/app/data --rm --name logsapp logsapp:volumes
stop:
	docker stop logsapp