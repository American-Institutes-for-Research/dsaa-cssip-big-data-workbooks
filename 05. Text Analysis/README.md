# BIG DATA AND SOCIAL SCIENCE RESEARCH: THEORY AND PRACTICAL APPROACHES - Text Analysis

<!-- TOC -->

# networks with Neo4J

## Directory Contents

- README.md - this file, an introduction and setup guide for the Text Analysis workbooks.
- requirements.txt - list of Python packages used in the Text Analysis notebooks.  These can be installed together using pip (in a command shell, go to the networks workbook directory, then type `pip install -r requirements.txt`), or just used as a reference when installing the packages individually.
- Topic Modeling.docx - Instructions for installing and verifying your install of Mallet, the "Machine LEarning for Language Toolkit".
- ipython notebooks

    - Topic Modeling.ipynb - IPython Notebook with introduction to using Neo4j with python, networkx, and matplotlib.

## Setup

### Install Python packages

First, we need to install the Python packages we'll use in the networks notebooks.  The packages we'll use are listed below, and they are also in the file `requirements.txt`, located in the same directory as this file.

When a package can be installed with `conda` or `pip`, it is probably a good idea to install with `conda` since Continuum, the makers of Anaconda, do considerable work to pre-compile and make sure the packages they provide work.

The following packages can be installed with either `conda` or `pip`:

- pymysql
- nltk

### Install mallet

- See the document "Topic Modeling.docx" for detailed instructions on installing mallet on your computer and verifying that it is installed correctly.

### Access jupyter notebooks
- At this point, you should already have jupyter installed.  If not, see the
- Start jupyter via a command line prompt by issuing the command jupyter notebook.  Navigate to your notebook ipynb files to start reviewing, running, and writing code
- Only start one instance of jupyter at a time
