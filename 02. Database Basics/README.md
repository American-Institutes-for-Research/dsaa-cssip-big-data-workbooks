# BIG DATA AND SOCIAL SCIENCE RESEARCH: THEORY AND PRACTICAL APPROACHES - Database Basics

<!-- TOC -->

# Database Basics

## Goals:

In this chapter you will learn the practical benefits that stem from using a Database Management System (DBMS). The materials in this chapter will focus on both the basics of database and SQL language. Specifically the chapter will focus on the following topics:

1. Connecting to a database through Python
2. Querying the database, i.e. using SQL in python
3. Introduction to SQL language
4. Closing database connections

## Directory Contents

- README.md - this file, an introduction and setup guide for the Database Basics workbooks.
- requirements.txt - list of Python packages used in the Database Basics notebooks.  These can be installed together using pip (in a command shell, go to the networks workbook directory, then type `pip install -r requirements.txt`), or just used as a reference when installing the packages individually.
- ipython notebooks:

    - Data_and_databases.ipynb - IPython Notebook with introduction to using relational databases and SQL with Python.

## Setup

### Install Python, database and data

Make sure that you have installed Anaconda and Python (using the document "Anaconda_Installation_Guide.docx" in the root of this repository) and the MySQL database and accompanying data (using the document "Database_Installation_Guide.docx" in the root of this repository) before you attempt this exercise.

### Install Python packages

First, we need to install the Python packages we'll use in the networks notebooks.  The packages we'll use are listed below, and they are also in the file `requirements.txt`, located in the same directory as this file.

When a package can be installed with `conda` or `pip`, it is probably a good idea to install with `conda` since Continuum, the makers of Anaconda, do considerable work to pre-compile and make sure the packages they provide work.

The following packages can be installed with either `conda` or `pip`:

- pymysql

### Access jupyter notebooks
- At this point, you should already have jupyter installed.  If not, see the document "Anaconda_Installation_Guide.docx" in the root of the workbooks repository.
- Start jupyter via a command line prompt by issuing the command jupyter notebook.  Navigate to your notebook ipynb files to start reviewing, running, and writing code
- Only start one instance of jupyter at a time.