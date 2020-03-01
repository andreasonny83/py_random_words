phony: clean build

clean:
	rm -rf dist build py_random_words.egg-info

build: clean
	python3 setup.py sdist bdist_wheel

release:
	twine upload dist/*