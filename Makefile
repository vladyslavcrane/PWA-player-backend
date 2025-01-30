install: requirements.txt manage.py 
	python3 -m venv venv
	. ./venv/bin/activate
	pip install -r requirements.txt
	python3 manage.py makemigrations
	python3 manage.py migrate
run-dev: manage.py
	python3 manage.py runserver
