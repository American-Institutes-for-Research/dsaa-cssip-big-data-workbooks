# BIG DATA AND SOCIAL SCIENCE RESEARCH: THEORY AND PRACTICAL APPROACHES
=========

“The first big breakthrough in our understanding of the mechanism of association was an improvement in a method of measurement” - Daniel Kahneman, 2011 Thinking Fast and Slow (p. 52)

## GOAL
---------

The goal of the book is to bring computer scientists and social scientists together to provide a practically oriented overview of the analytical and statistical tools associated with big data for social science students. We use real data used for real world policy problems to analyze some of the vast new sets of data on human beings. We show them how these data can be collected, integrated, and analyzed in a scientific fashion.

## Directory Contents

- `README.md` - this file, an introduction and setup guide for the book's IPython Notebooks.
- `Anaconda_Installation_Guide.docx` - Instructions for installing Anaconda, a Python distribution that also includes IPython and Jupyter.    
- `Database_Installation_Guide.docx` - Instructions for installing a local database instance and downloading and installing the data used by the exercise IPython notebooks.
- exercise directories, each of which contains its own README.md file with more details and further instructions:

    - `02. Database Basics`
    - `03. Visualization`
    - `04. Social Media and APIs`
    - `05. Text Analysis`
    - `06. Networks`
    - `07. Machine Learning`
    - `08. Data Linkage`
    - `10. Samples and Statistical Inference`

## Setup

### Install Python, jupyter and jupyterhub

First, you'll need to install Anaconda, so you have Python and Jupyter.  Instructions are in the document `Anaconda_Installation_Guide.docx` in this directory.

### Install the Database and Data

Then, you'll need to install the database and data used in the book's exercises.  Instructions are in the document `Database Installation Guide.docx` in this directory.

### Access jupyter notebooks
- Start jupyter via a command line prompt by issuing the command `jupyter notebook`.  This will open a command window (leave it open) and a browser window containing the main jupyter page, a file browser that lets you find, run, and create jupyter notebooks.
- Navigate to the exercises folder, and then into one of the Exercises.  Double-click on one of the `*.ipynb` files in the directory to get started.
- Only start one instance of jupyter at a time

## BOOK EDITORS
---------

Ian Foster, University of Chicago

Rayid Ghani, University of Chicago

Ron Jarmin, U.S. Census Bureau

Frauke Kreuter, University of Maryland

Julia Lane, American Institutes for Research

## WORKBOOK EDITORS
---------

Christina Jones, Josh Tokle and Ahmad Emad, American Institutes for Research

Jonathan Morgan, Michigan State University

## KEY FEATURES
---------

We will incorporate several features that have been successfully used in two classes to federal science agency staff by the proposed chapter authors.

1. There is a clear conceptual framework that leads naturally to the data structure and to the techniques used (see Figures 1 and 2 below for examples)
2. There is high quality content that incorporates both computer science and social science in all sections of the book
3. The approach combines both research and programming; there is the development of subject matter knowledge, and acknowledgement of the importance of trial and error and experimentation, but a laser like focus on producing high quality statistical output
4. There is an emphasis on coding, but that coding is made as dynamic as possible. As in the classes, we will make use of iPython Notebook (http://ipython.org/notebook.html) so that text, code and mathematics are integrated for classroom use.

## BACKGROUND
---------

Big data have brought a new analytical paradigm to statisticians and social scientists (Hey, Tansley, & Tolle, 2009). The research community has moved beyond survey and even administrative data to begin to understand how data can be mined from social media to capture national sentiment, from cellphone data to understand anti-government uprisings, and from financial data to examine swings in the economy.

The change in paradigm results from changes in many factors that affect the measurement of human behavior: the nature of the new types of data, their availability, the way in which they are collected, and data dissemination. The consequences of these changes for social science research is fundamental change in both the potential analysis that can be done and who the analysts might be. Indeed, while the statistical community has moved beyond survey and even administrative data to begin to understand how data can be mined from social media to capture national sentiment, from cellphone data to understand anti-government uprisings, and from financial data to examine swings in the economy, it is equally important to note that now data are freely available and usable to all who want to mash two data series together that are downloaded from the internet – creating an entire new class of citizen, rather than professional, data analysts.

The change in the nature of the new type of data is transformative. Its characteristics – its velociy, volume and variety – and the way in which it is collected, mean that a new analytical paradigm is open to statisticians and social scientists (Hey et al., 2009). The classic statistical paradigm was one in which researchers formulated a hypothesis, identified a population frame, designed a survey and a sampling technique and then analysed the results(Groves, 2011). The new paradigm means that it is now possible to digitally capture, semantically reconcile, aggregate, and correlate. Those correlations might be effective (Cukier & Schoenberger, 2014; Halevy, Norvig, & Pereira, 2009) or suspect (Couper, 2013). They certainly enable completely new analysis to be undertaken – none of which can be done using survey data alone. For example, the new type of analysis might be one that captures rich environmental detail on individuals (from sensors, google earth, videos, photos or financial transactions). Or the analysis might include rich and detailed information on unique and quite small subsets of the population (from microbiome data, or websearch logs). Or the analysis might be on completely new units of analysis, like networks of individuals or businesses, whose connections can only be captured by new types of data (like tweets, cell phone conversations, and administrative records). As Kahneman points out, the new measurement can change the paradigm in its own right (Kahneman, 2011).

The change also means a change in the production of social science research. The change in the way in which data are processed and the type of skills that are needed to process the data stems from the fact that the cost of converting data to usable information is very different in a big data world relative to a survey world. One of the most obvious advantages is that electronic data gathering is substantially cheaper than surveys. Surveys are inherently expensive, requiring a good deal of labor to collect the data. In contrast, by relying on computer software, electronic data gathering, while requiring some upfront costs and maintenance costs, can be much more cost effective. But while big data are relatively cheap to collect, they are expensive to clean and process. So the human capital which previously went into designing and sampling now needs to be repurposed into structuring, linking and managing the new types of data.

The change in the ownership of the data has also transformed the way in which data are disseminated. Data are much less likely to be carefully curated and disseminated by professionals in federally funded statistical agencies or in major survey research organizations. As a result, the population of potential data analysts – trained and untrained has dramatically expanded. This expansion can result in enormous new insights, as the Sloan Digital Sky Survey and the Polymath project has shown (Nielsen, 2012), and is reflected in Grey’s Fourth Paradigm (Figure 1) (Hey et al., 2009), but can also lead to the degradation of the quality of analysis that can be done.

Finally, the excitement of the change in research paradigm should be tempered by a recognition that our existing ways of protecting confidentiality are no longer viable (Karr & Reiter, 2014) As order and analytical rigor is brought to the new data frontier, we should ensure that the future structure of data access ensures that the goal of good science is attained while protecting confidentiality. There is a great deal of research that can be used to inform the development of such a structure, but it has been siloed into separate activities in different research areas - statistics, cybersecurity, cryptography – as well as a variety of different practical applications, including the successful development of remote access secure data enclaves. We must identify ways in which vast new sets of data on human beings can be collected, integrated, and analysed for analysis life while protecting confidentiality (Lane, Stodden, Bender, & Nissenbaum, 2014).

## Textbook and Workbook Outline

1. INTRODUCTION AND MOTIVATION (THE EDITORS)

    The goal of this chapter is to introduce students to the overall approach, to the data, what will be learned
    1. The social science of measurement
    2. “Big Data”: Definitions, technical issues
    3. Introduction to big data and overview of existing analysis
    4. Introduction to the data that will be used in the book

2. DATABASE BASICS (JULIANA FRIERE AND JULIA LANE)

    The goal of this chapter is for students to be able to read, write, and build different types of databases using heterogeneous sources of data.
    1. Database concepts
    2. Database taxonomies
    3. ETL in different databases
    4. Data hygiene: curation and documentation

3. VISUALIZATION (CATHERINE PLAISANT)

    The goal of this chapter is to provide an overview of different approaches to conveying information in an intuitive and statistically valid manner. The chapter will focus on the uses of visualization for analytical purposes as well as for communication purposes.
    1. Overview of visualization approaches
    2. Using graphics packages for data visualization, including network geolocation and GIS software to display shape files

4. UNDERSTANDING THE USES OF SOCIAL MEDIA AND USING APIS (CAMERON NEYLON)

    The goal of this chapter is to examine how to make use of social media APIs. The particular application is capturing information about the transmission of knowledge and ideas
    1. Introduction to APIs
    2. Use the PLOS Search API to obtain a list of DOIs for relevant papers.
    3. Use clustering algorithms to identify subsets of articles that appear to have differing “impact signals”
    4. Identify followers
    5. Application of visualization techniques

5. PROGRAMMING WITH BIG DATA (CLAUDIO SILVA)

    This chapter shows how to combine large datasets and optimize programming. It will provide an introduction to NOSQL, MapReduce and Hadoop
    1. Introduction to characteristics of large databases
    2. Building datasets to be linked
    3. Create a big data sample work flow
    4. Example of record linkage with MapReduce

6. NETWORKS (JASON OWEN SMITH)

    The goal of this chapter is to develop new units of analysis (networks) and show how to measure different types of networks
    1. Directed and undirected graphs
    2. Relational analysis on graphs
    3. Changes in structure, size and orientation of networks as a result of federal grants

7. DATA LINKAGE (STEFAN BENDER AND JOSH TOKLE)

    The goal of the chapter is to go through the basics of data linkage across heterogeneous datasets
    1. Linkage in the context of big data
    2. Social science approaches
    3. Computer science approaches
    4. Strengths and weaknesses

8. MACHINE LEARNING (RAYID GHANI AND MALTE SCHIERHOLZ)

    The goal of this chapter is to show students how to apply machine learning ideas, processes and methods and how to build a conceptual framework within the context of the goals and data available for the class.
    1. What is machine learning
    2. Examples, process and methods
    3. Advanced topics
    4. Application to text data

9. TEXT ANALYSIS (JORDAN BOYD GRABER AND EVGENY KLOCHIKHIN)

    The goal of this chapter is to introduce students to the potential for using text analysis to identify topics and themes.
    1. Value of text data
    2. Different text analytics paradigms
    3. Discovering topics and themes in large quantities of text data

10. NON-RANDOM SAMPLES AND STATISTICAL INFERENCE (PAUL BIEMER)

    This chapter will provide an overview of using data from a non-randomly selected sample for inference.
    1. Review of total error measurement for surveys (literary digest ex.)
    2. Discussion of error measurement with big data (Mick Couper and Paul Biemer)
    3. The role of weighting and missing conditionally at random; benefit cost
    4. Specific examples in this context:

        1. Defining a population/frame (scientists; research organizations; funding vehicles, networks..)
        2. Thinking about measurement issues (ex. Education vs. human capital)
        3. Developing weights (IPW approach; Manski Horowitz bounds; multiple imputations; hotdecking)

11. Privacy and Confidentiality (Frauke Kreuter, Julia Lane and Stefan Bender)

    This chapter will provide an overview of the privacy and confidentiality issues associated with big data
    1. Legal Framework
    2. Statistical Framework
    3. Practical approaches

## References

- Couper, M. (2013). Is the sky falling? New technology, changing media, and the future of surveys. Survey Research Methods.
- Cukier, K., & Schoenberger, V. (2014). The Rise of Big Data. Foreign Affairs.
- Groves, R. M. (2011). Three eras of survey research. Public Opinion Quarterly, 75(5), 861–871.
- Halevy, A., Norvig, P., & Pereira, F. (2009). The unreasonable effectiveness of data. Intelligent Systems, IEEE 24, 8–12.
- Hey, T., Tansley, S., & Tolle, K. (2009). The Fourth Paradigm: Data Intensive Scientific Discovery. Microsoft Research.
- Kahneman, D. (2011). Thinking Fast and Slow. Farrar, Straus and Giroux.
- Karr, A., & Reiter, J. P. (2014). Analytical Frameworks for Data Release: A Statistical View. In J. Lane, V. Stodden, H. Nissenbaum, & S. Bender (Eds.), Privacy, Big Data, and the Public Good: Frameworks for Engagement. Cambridge University Press.
- Lane, J., Stodden, V., Bender, S., & Nissenbaum, H. (2014). Privacy, big data and the public good: Frameworks for engagement. Cambridge University Press.
- Nielsen, M. (2012). Reinventing discovery: the new era of networked science. Princeton University Press.
