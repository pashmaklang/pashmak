PYTHON = python3

update-headers:
	$(PYTHON) ./scripts.py update-headers

test:
	$(PYTHON) ./scripts.py test
