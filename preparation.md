---
layout: default
title: Preparation
nav_order: 2
---

# Workshop preparation 

Preparation for this tutorial consists of two steps: [Getting the data](#get-the-data) and [Getting the software](#get-the-software). Follow the steps below. 
  
## 1. Get the data

The document we will be working with in the lesson is "[Letters Written During a Short Residence in Sweden, Norway, and Denmark](https://www.gutenberg.org/ebooks/3529)" by Mary Wollstonecraft from Project Gutenberg: 

1. Go to the [Plain Txt UTF-8](https://www.gutenberg.org/ebooks/3529.txt.utf-8) version of the document,
2. You can either 
   - save the page as a text (.txt) file or, 
   - copy the text (ctrl / cmd + A to select all, then ctrl / cmd + C to copy) and paste into a text file (create one using Notepad on a Windows OS or TextEdit on a Mac and then ctrl / cmd + V to paste) and save with a .txt extension as wollstonecraft.txt.
3. Delete the preamble and license terms added by Project Gutenberg from the text file to exclude them from the analysis.

Alternatively, you can download [a copy of the same document](assets/wollstonecraft.txt) with the preamble and the license terms removed.

## 2.  Get the software

This workshop uses the [Python programming language](https://www.python.org/), and the [SpaCy](https://spacy.io/) natural language processing library for Python. We will be working with Python through the Spyder integrated development environment (IDE) to access tools that will make our tasks easier. Although Spyder can be downloaded as a standalone application, we are going to use the Anaconda platform to simplify some of the set-up tasks so that we can get up and running quickly.

[Download Anaconda](https://www.anaconda.com/products/individual) 

The Anaconda platform contains numerous other software applications used in research computing, such as Jupiter Notebook and RStudio, that you may also want to explore. Its size on disk, however, is quite large as a result - about 3GB. 

**If you have programming experience with Python,** you are welcome to use the IDE you are familiar with as an alternative. The lesson instructions use `pip` to install SpaCy. 

Please contact the [Sherman Centre](mailto:scds@mcmaster.ca) if you have any difficulties downloading or opening the software.

### Software versions

As the lesson is written, the software versions are as follows:

**Python:** 3.9
**Anaconda Navigator:** 2.1.1
**Spyder:** 5.1.5

## 3. Assemble your own corpus (optional)

In advance of the lesson, we also recommend that you assemble a collection of documents to work with for the *Try it with your data* sections. We will use the text  provided above to practice the techniques demonstrated in the lesson but each dataset brings its own unique features. Even if you are not going through the lesson with a specific project in mind, having a different corpus to experiment with will help to reinforce the concepts and enrich your knowledge of the topic.

If you have not already gone through your corpus to get a sense of what errors it might contain, now is a good time! If proper names are misspelled, they may not be identified through named entity recognition or counted with other instances of the same (correctly spelled) name.


<br />
Next --> [Named Entity Recognition](instructions.html) (hands-on lesson)
