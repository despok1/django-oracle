run-server:
	python3 manage.py runserver 0.0.0.0:8000
run:
	python3 manage.py runserver
migrate:
	python3 manage.py migrate
push:
	git add . && git commit && git push