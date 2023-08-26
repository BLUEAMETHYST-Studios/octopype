build:
	python3 setup.py sdist bdist_wheel
release:
	twine upload dist/*