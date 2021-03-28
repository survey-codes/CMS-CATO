superuser:
	docker exec -it catoback ./manage.py createsuperuser

shell:
	docker exec -it catoback ./manage.py shell

makemigrations:
	docker exec -it catoback ./manage.py makemigrations

migrate:
	docker exec -it catoback ./manage.py migrate

initialfixture:
	docker exec -it catoback ./manage.py loaddata initial

statics:
	docker exec -it catoback ./manage.py collectstatic --noinput

makemessages:
	docker exec -it catoback django-admin makemessages

compilemessages:
	docker exec -it catoback django-admin compilemessages

templatesfixture:
	docker exec -it catoback ./manage.py loaddata templates
