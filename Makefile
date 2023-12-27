up:
	docker-compose -f local.yml up -d --build

down:
	docker-compose -f local.yml down

down-v:
	docker-compose -f local.yml down -v