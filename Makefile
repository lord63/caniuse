test:
	@py.test --pep8 -v --cov-report term-missing --cov=caniuse/ tests/ caniuse/

create:
	@python setup.py sdist bdist_wheel

upload:
	@python setup.py sdist bdist_wheel upload
