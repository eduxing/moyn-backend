.PHONY: local docker setup

local:
	docker-compose up db -d && DJANGO_DATABASE='local' ./manage.py runserver

docker:
	docker-compose up -d

setup:
	docker-compose run web python manage.py migrate
	docker-compose exec web python manage.py loaddata fixtures/users.json
	docker-compose exec web python manage.py loaddata fixtures/communities.json
	docker-compose exec web python manage.py loaddata fixtures/posts.json
	docker-compose run web python manage.py createsuperuser