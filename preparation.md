---
layout: default
title: Preparation
nav_order: 2
---

# Workshop Preparation 

Preparation for this tutorial consists of two steps: [Getting the data](#get-the-data) and [Getting the software](#get-the-software). Please follow the steps below before beginning the lesson.

<hr />
  
## Get the data

The document we will be working with in the lesson is "[Letters Written During a Short Residence in Sweden, Norway, and Denmark](https://www.gutenberg.org/ebooks/3529)" by Mary Wollstonecraft from Project Gutenberg: 

1. Go to the [Plain Txt UTF-8](https://www.gutenberg.org/ebooks/3529.txt.utf-8) version of the document,
2. You can either 
   - save the page as a text (.txt) file or, 
   - copy the text (ctrl / cmd + A to select all, then ctrl / cmd + C to copy) and paste into a text file (create one using Notepad on a Windows OS or TextEdit on a Mac and then ctrl / cmd + V to paste) and save with a .txt extension as wollstonecraft.txt.
3. Delete the preamble and license terms added by Project Gutenberg from the text file to exclude them from the analysis.

Alternatively, you can download [a copy of the same document](assets/wollstonecraft.txt) with the preamble and the license terms removed.

<hr />

## Get the software

This workshop uses the [Python programming language](https://www.python.org/), and the [SpaCy](https://spacy.io/) natural language processing library for Python. We will be working with Python through the Spyder integrated development environment (IDE) to access tools that will make our tasks easier. Although Spyder can be downloaded as a standalone application, we are going to use the Anaconda platform to simplify some of the set-up tasks so that we can get up and running quickly.

[Download Anaconda](https://www.anaconda.com/products/individual) 

The Anaconda platform contains numerous other software applications used in research computing, such as Jupiter Notebook and RStudio, that you may also want to explore. Its size on disk, however, is quite large as a result - about 3GB. 

**If you are unable to download and/or install Anaconda,** you can alternatively follow along in the [Jupyter notebook version of the workshop](https://colab.research.google.com/drive/1a2tt05ijDuSrNDQ0G-9XfsYijONt8Eeg?usp=sharing) in Google Colab. You will need to upload the Wollstonecraft.txt file to the file area in Google Colab as described in [Jay Brodeur's "Basic Text Prep with Python" Colab notebook](https://colab.research.google.com/drive/1ynkHM3WOQUGj9mj8R060p3BYqI6ThbAj), step 3. Run the code cell by cell using the "play" button at the left of each cell.

**If you have programming experience with Python,** you are welcome to use the IDE you are familiar with as an alternative. The lesson instructions use `pip` to install SpaCy. 

Please contact the [Sherman Centre](mailto:scds@mcmaster.ca) if you have any difficulties downloading or opening the software.

<hr />

### Software versions

For the lesson as it is currently written, the software versions are as follows:

**Python:** 3.9

**Anaconda Navigator:** 2.1.1

**Spyder:** 5.1.5

If the versions differ from your own, that's ok! There's no need to track down older versions of the software to complete the lesson. The steps should remain the same, but there might be some small variations that can be attributed to using a later version (with the exception of your Python version, which *might* break the code; Python 3.9 will be supported until October 2025).

<hr />

## Assemble your own corpus (optional)

In advance of the lesson, we also recommend that you assemble a collection of documents to work with for the *Try it with your data* sections. We will use the text  provided above to practice the techniques demonstrated in the lesson but each dataset brings its own unique features. Even if you are not going through the lesson with a specific project in mind, having a different corpus to experiment with will help to reinforce the concepts and enrich your knowledge of the topic.

If you have not already gone through your corpus to get a sense of what errors it might contain, now is a good time! If proper names are misspelled, they may not be identified through named entity recognition or counted with other instances of the same (correctly spelled) name.


<br />
Next --> Start the [Named Entity Recognition](instructions.html) Lesson
