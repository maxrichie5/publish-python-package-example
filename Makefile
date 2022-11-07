# Targets for local development
shell::   pipenv shell
install:: ci_install
fmt::     ci_fmt
lint::    fmt ci_lint
test::    fmt ci_lint ci_test

.SILENT: git_reset

# Targets for CI
ci_fmt::
	pipenv run black max_richmond_publish_python_package_example tests

ci_lint::
	pipenv run mypy --config-file mypy.ini max_richmond_publish_python_package_example tests

ci_test::
	pipenv run nosetests -v --with-coverage --cover-package=max_richmond_publish_python_package_example

ci_install:
	pipenv install --dev

# Other targets
publish:
	rm -rf dist
	pipenv run python3 setup.py sdist
	pipenv run twine upload ./dist/max_richmond_publish_python_package_example-*.tar.gz