up:
	docker-compose -f local.yml up -d --build

down:
	docker-compose -f local.yml down

down-v:
	docker-compose -f local.yml down -v

lang-fa:
	docker-compose -f local.yml run --rm django python manage.py makemessages -l fa

lang-en:
	docker-compose -f local.yml run --rm django python manage.py makemessages -l en

lang-com:
	docker-compose -f local.yml run --rm django python manage.py compilemessages

createsuperuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

migrate:
	docker-compose -f local.yml run --rm django python manage.py makemigrations
	docker-compose -f local.yml run --rm django python manage.py migrate

fix-permission:
	sudo chown ho:ho --recursive .