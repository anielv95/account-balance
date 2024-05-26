install:
	pip install --upgrade pip &&\
		pip install -r requirements-dev.txt

lint:
	pylint --disable=R,C src/*.py src/*/*.py

format:
	black src/*.py

test:
	python -m pytest -vv -s --cov=functions src/test.py