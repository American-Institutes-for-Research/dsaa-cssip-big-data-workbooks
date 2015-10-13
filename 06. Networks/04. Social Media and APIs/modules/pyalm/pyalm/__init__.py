# pyalm

'''
pyalm library
~~~~~~~~~~~~~~~~~~~~~

pyalm is a Python client for the PLOS ALM API. Example usage:

   >>> import pyalm
   >>> pyalm.get_alm("10.1371/journal.pone.0029797", info="summary")

   <ArticleALM Ecological Guild Evolution and the Discovery of the World's Smallest Vertebrate, DOI 10.1371/journal.pone.0029797>
'''

from .cleanup import *
from .config import *
from .events import *
from .pyalm import get_alm
from .utils import *

import os
import re

def _insert_items(keydict, mdict, i):
	for p in keydict.iterkeys():
		if bool(re.search(i, p, re.IGNORECASE)):
			if bool(re.search('URL', p)):
				mdict[i]['url'] = keydict[p]
			if bool(re.search('KEY', p)):
				mdict[i]['key'] = keydict[p]
	return mdict

def _get_env_vars():
	kk = [pyalm.config.PLOS_KEY_ENVVAR, pyalm.config.ELIFE_KEY_ENVVAR,
		pyalm.config.CROSSREF_KEY_ENVVAR, pyalm.config.PKP_KEY_ENVVAR,
		pyalm.config.COPERNICUS_KEY_ENVVAR, pyalm.config.PENSOFT_KEY_ENVVAR,
		pyalm.config.PLOS_URL_ENVVAR, pyalm.config.ELIFE_URL_ENVVAR,
		pyalm.config.CROSSREF_URL_ENVVAR, pyalm.config.PKP_URL_ENVVAR,
		pyalm.config.COPERNICUS_URL_ENVVAR, pyalm.config.PENSOFT_URL_ENVVAR]
	keydict = {}
	for x in kk:
		keydict[x] = os.environ.get(x)

	mdict = {}
	mdict['plos'] = {}
	mdict['elife'] = {}
	mdict['pkp'] = {}
	mdict['pensoft'] = {}
	mdict['crossref'] = {}
	mdict['copernicus'] = {}

	names = ['plos','elife','pkp','pensoft','crossref','copernicus']
	for x in names:
		_insert_items(keydict, mdict, x)

	return mdict

def _attempt_key_load():
	"""
	This function (which will be auto-called on import of :mod:`pyalm`),
	will attempt to pull the API Keys from a few places.

	.. note::
		This function is implemented to let the enviroment variable override
		the file read key. Keep this in mind when debugging silly issues.
	"""

	try:
		fp = os.path.expanduser(pyalm.config.PYALM_LOCATION)
		fd = open(fp, 'r')
		vals = fd.read().splitlines()
		pyalm.config.APIS = dict(iter([i.split("=") for i in vals]))
	except IOError as e:
		if e.errno != 2:
			warnings.warn('pyalm file %s exists but could not be opened: %s' % (
				pyalm.config.PYALM_LOCATION, str(e)))
	try:
		pyalm.config.APIS = _get_env_vars()
	except KeyError as e:
		pass

_attempt_key_load()
