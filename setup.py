from setuptools import setup, find_packages

setup(name='py_random_words',
      version='0.1',
      url='https://github.com/andreasonny83/py_random_words',
      license='MIT',
      author='andreasonny83',
      author_email='andreasonny83@gmail.com',
      description='Generate random names',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)