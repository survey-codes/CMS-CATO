superuser:
	docker exec -it catocms-backend ./manage.py createsuperuser

shell:
	docker exec -it catocms-backend ./manage.py shell

makemigrations:
	docker exec -it catocms-backend ./manage.py makemigrations

showmigrations:
	docker exec -it catocms-backend ./manage.py showmigrations

migrate:
	docker exec -it catocms-backend ./manage.py migrate

initialfixture:
	docker exec -it catocms-backend ./manage.py loaddata initial

demofixture:
	docker exec -it catocms-backend ./manage.py loaddata demo

templatesfixture:
	docker exec -it catocms-backend ./manage.py loaddata templates

statics:
	docker exec -it catocms-backend ./manage.py collectstatic --noinput

makemessages:
	docker exec -it catocms-backend django-admin makemessages

compilemessages:
	docker exec -it catocms-backend django-admin compilemessages
