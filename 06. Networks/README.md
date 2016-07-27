# BIG DATA AND SOCIAL SCIENCE RESEARCH: THEORY AND PRACTICAL APPROACHES - networks with Neo4J

<!-- TOC -->

# networks with Neo4J

## Directory Contents

- README.md - this file, an introduction and setup guide for the networks workbooks.
- requirements.txt - list of Python packages used in the network notebooks.  These can be installed together using pip (in a command shell, go to the networks workbook directory, then type `pip install -r requirements.txt`), or just used as a reference when installing the packages individually.
- Installing_neo4j.docx - Instructions for installing Neo4j, adding some data, and then testing your install of Neo4j.
- data files:
    
    - employee_data.csv - employee data, loaded during `Installing_neo4j.docx`
    - award_data.csv - award data, loaded during `Installing_neo4j.docx`
    - student_data.csv - student data, loaded while running `networks with neo4j.ipynb`

- ipython notebooks
    
    - networks with neo4j.ipynb - IPython Notebook with introduction to using Neo4j with python, networkx, and matplotlib.
    - networks_exercise.ipynb - IPython Notebook that contains the actual exercises for this section of the workbook.

## Setup

### Install Python packages

First, we need to install the Python packages we'll use in the networks notebooks.  The packages we'll use are listed below, and they are also in the file `requirements.txt`, located in the same directory as this file.

When a package can be installed with `conda` or `pip`, it is probably a good idea to install with `conda` since Continuum, the makers of Anaconda, do considerable work to pre-compile and make sure the packages they provide work.

The following packages can be installed with either `conda` or `pip`:

- pymysql
- numpy
- networkx
- matplotlib

The following packages can only be installed using `pip`:

- py2neo

### Install neo4j

- See the document "installing_neo4j.docx" for detailed instructions on installing Neo4j on your computer and verifying that it is installed correctly.  This document includes installing faculty and awards data.  Student data is installed during the process of working through the notebooks.

