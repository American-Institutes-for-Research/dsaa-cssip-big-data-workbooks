pyalm
=====

A Python Wrapper for the PLOS Article Level Metrics App API
-----------------------------------------------------------

The wrapper is based on the orcid-python wrapper by github users scholrly which can be
found at https://github.com/scholrly/orcid-python.

Installation
------------
Clone the github repository to your local machine as desired and then run

	python setup.py install 
	
or

	python setup.py develop
	
if you wish to work on the code.

To use the API you will need an api key. Look for the api_key.example.py file for 
instructions on how to get an API key for the PLOS installation and where to put it.

Testing and Contributions
-------------------------
[![Build Status](https://travis-ci.org/cameronneylon/pyalm.png?branch=master)](https://travis-ci.org/cameronneylon/pyalm)
[![Coverage Status](https://img.shields.io/coveralls/cameronneylon/pyalm.svg)](https://coveralls.io/r/cameronneylon/pyalm?branch=master)

pyalm is currently tested via a small unittest suite and continuous integration via
Travis-CI with tests run for Python 2.7. Feel free to fork and to issue a pull request 
for any contributions and improvements (including getting it to pass tests under other
Python versions).
