start:
	python3 -m example.app
prepare:
	python3 -m pip install --upgrade build
	python3 -m venv venv
	pip install -r requirements.txt
	make build
build:
	python -m build --sdist --wheel	