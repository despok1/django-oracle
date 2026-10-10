run-server:
	python3 manage.py runserver 0.0.0.0:8000
run:
	python3 manage.py runserver
migrate:
	python3 manage.py migrate
push:
	git add . && git commit && git push
ssh:
	ssh -i ~/.ssh/ssh-key-2026-09-27.key ubuntu@152.70.190.140 