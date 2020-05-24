run:
	python3 manage.py runserver

lint:
	pylint ./*.py app tests

# run all tests
# by default uses sugar
test:
	python -m pytest

testprint:
	python -m pytest --capture=no --verbose

testprint_nosugar:
	python -m pytest --capture=no -p no:sugar --verbose

test_v:
	python -m pytest --verbose

testcov:
	python -m pytest --verbose -p no:sugar --cov=vanilla-fsk tests/

testcovreport:
	python -m pytest --verbose -p no:sugar --cov-report html:cov_html --cov=vanilla-fsk tests/

# run all tests without the sugar plugin
nosugar:
	python -m pytest -p no:sugar

# run all tests without the sugar plugin verbose mode
nosugar_v:
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
	python -m pytest --verbose -m marked