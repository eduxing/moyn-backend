.PHONY: local docker setup

venv:
	pipenv shell

local:
	docker-compose up db -d && DJANGO_DATABASE='local' ./manage.py runserver

migrate_local: 
	docker-compose up db -d && DJANGO_DATABASE='local' ./manage.py migrate

docker:
	docker-compose up -d

migrate:
	docker-compose exec web python manage.py migrate

fixtures:
	docker-compose exec web python manage.py loaddata fixtures/users.json
	docker-compose exec web python manage.py loaddata fixtures/communities.json
	docker-compose exec web python manage.py loaddata fixtures/posts.json	
	
setup:
	docker-compose run web python manage.py migrate
	docker-compose exec web python manage.py loaddata fixtures/users.json
	docker-compose exec web python manage.py loaddata fixtures/communities.json
	docker-compose exec web python manage.py loaddata fixtures/posts.json
	docker-compose run web python manage.py createsuperuser