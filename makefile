start:
	python3 -m example.app
prepare:
	python3 -m venv venv
	pip install -r requirements.txt
	python3 setup.py build
	