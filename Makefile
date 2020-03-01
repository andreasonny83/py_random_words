clean:
    rm -rf dist build py_random_words.egg-info

build: clean
    python3 setup.py sdist

release:
    twine upload dist/*