fmt::
	pipenv run black floop tests
	pipenv run isort .
	pipenv run flake8 .

lint::
	pipenv run mypy --config-file mypy.ini floop tests

test::
	pipenv run nosetests -v --with-coverage --cover-package=floop

install:
	pipenv install --dev

run:
	pipenv run bin/floop

# Other targets
# publish:
# 	rm -rf dist
# 	pipenv run python3 setup.py sdist
# 	pipenv run twine upload ./dist/floop-*.tar.gz