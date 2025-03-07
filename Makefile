#initialize the fsk app
init:
	pip3 install -r requirements.txt

run:
	python manage.py run

lint:
	flake8 ./*.py app tests

pylint:
	pylint ./*.py app tests

# database migration commands
clean:
	rm -rf db/migrations

reset_tables:
	python manage.py reset_tables

init-db:
	flask db init --directory db/migrations

migrate:
	flask db migrate -d db/migrations

upgrade:
	flask db upgrade -d db/migrations

downgrade:
	python manage.py db downgrade -d db/migrations

seed: reset_tables
	python manage.py seed

migrate_upgrade: migrate upgrade

db-setup: clean init-db migrate upgrade seed

# run all tests
# by default uses sugar
test:
	python -m pytest

testprint:
	python -m pytest --capture=no --verbose

testprint_nosugar:
	python -m pytest --capture=no -p no:sugar --verbose

test-v:
	python -m pytest --verbose

testcov:
	python -m pytest --verbose -p no:sugar --cov=app tests/

testcovreport:
	python -m pytest --verbose -p no:sugar --cov-report html:cov_html --cov=app tests/

# run all tests without the sugar plugin
nosugar:
	python -m pytest -p no:sugar

# run all tests without the sugar plugin verbose mode
nosugar-v:
	python -m pytest --verbose -p no:sugar

# we can run test directory on a single file or a module with this command
# edit this section to change file being tested
solotest:
	python -m pytest tests/controllers/users/test_dao.py

# we can also run a specific function within a test file
# edit this section to reflect the test
functest:
	python -m pytest tests/controllers/test_mod.py::test_func

# Run tests by Marker expression
# the example here are tests labelled with `marked`. Replace `marked` with desired label
markedtest:
	python -m pytest -p no:sugar --verbose -m marked