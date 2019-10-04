from setuptools import setup, find_packages

setup(name='validathor',
      version='0.1',
      url='https://github.com/rnduldulaojr/validathor',
      license='MIT',
      author='Rodolfo N. Duldulao, Jr.',
      author_email='rnduldulaojr@gmail.com',
      description='Just another validation library that brings joy - we hope.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)


