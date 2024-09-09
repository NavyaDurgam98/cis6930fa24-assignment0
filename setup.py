from setuptools import setup, find_packages

setup(
	name='assignment0',
	version='1.0',
	author='Navya Durgam',
	author_email='durgam.navya@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)