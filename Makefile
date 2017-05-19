.PHONY: devserver init lint isort

devserver:
	pipenv run python manage.py runserver --settings=demo_project.settings.dev

init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

lint:
	pipenv run flake8

isort:
	pipenv run isort --check-only --recursive --diff demo demo_project
