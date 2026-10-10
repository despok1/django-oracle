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
scp:
	scp -i ~/.ssh/ssh-key-2026-09-27.key django.service ubuntu@152.70.190.140:~/django.service
	ssh -i ~/.ssh/ssh-key-2026-09-27.key ubuntu@152.70.190.140 "sudo install -m 644 ~/django.service /etc/systemd/system/django.service && rm ~/django.service && sudo systemctl daemon-reload"
scp2:
	scp -i ~/.ssh/ssh-key-2026-09-27.key deploy.sh ubuntu@152.70.190.140:~/deploy.sh