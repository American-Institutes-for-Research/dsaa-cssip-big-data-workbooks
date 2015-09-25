from setuptools import setup

setup(name='pyalm',
      version='0.1',
      description='Python Wrapper for the PLOS Article Level Metrics API',
      url='http://github.com/cameronneylon/pyalm',
      author='Cameron Neylon',
      author_email='pyalm@cameronneylon.net',
      license='Apache',
      packages=['pyalm'],
      install_requires=['requests',],
      zip_safe=False)