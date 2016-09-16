# BIG DATA AND SOCIAL SCIENCE RESEARCH: THEORY AND PRACTICAL APPROACHES - Machine Learning

<!-- TOC -->

# Machine Learning

## Directory Contents

- README.md - this file, an introduction and setup guide for the Machine Learning workbooks.
- requirements.txt - list of Python packages used in the Machine Learning notebooks.  These can be installed together using pip (in a command shell, go to the networks workbook directory, then type `pip install -r requirements.txt`), or just used as a reference when installing the packages individually.
- ipython notebooks

    - Machine Learning.ipynb - IPython Notebook with introduction to Machine Learning using pandas and scikit-learn.
    
## Setup

### Install Python packages

First, we need to install the Python packages we'll use in the networks notebooks.  The packages we'll use are listed below, and they are also in the file `requirements.txt`, located in the same directory as this file.

When a package can be installed with `conda` or `pip`, it is probably a good idea to install with `conda` since Continuum, the makers of Anaconda, do considerable work to pre-compile and make sure the packages they provide work.

The following packages can be installed with either `conda` or `pip`:

- pandas
- sqlalchemy
- numpy
- ipython
- scikit-learn
- pymysql

### Access jupyter notebooks
- At this point, you should already have jupyter installed.  If not, see the document "Anaconda_Installation_Guide.docx" in the root of the workbooks repository.
- Start jupyter via a command line prompt by issuing the command jupyter notebook.  Navigate to your notebook ipynb files to start reviewing, running, and writing code
- Only start one instance of jupyter at a time.