superuser:
	docker exec -it catocms ./manage.py createsuperuser

shell:
	docker exec -it catocms ./manage.py shell

makemigrations:
	docker exec -it catocms ./manage.py makemigrations

showmigrations:
	docker exec -it catocms ./manage.py showmigrations

migrate:
	docker exec -it catocms ./manage.py migrate

initialfixture:
	docker exec -it catocms ./manage.py loaddata initial

demofixture:
	docker exec -it catocms ./manage.py loaddata demo

templatesfixture:
	docker exec -it catocms ./manage.py loaddata templates

statics:
	docker exec -it catocms ./manage.py collectstatic --noinput

makemessages:
	docker exec -it catocms django-admin makemessages

compilemessages:
	docker exec -it catocms django-admin compilemessages
