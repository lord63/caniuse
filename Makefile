test:
	@py.test --pep8 -v --cov-report term-missing --cov=caniuse/ tests/ caniuse/
