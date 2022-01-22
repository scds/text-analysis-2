---
layout: default
title: Installing SpaCy
parent: Lesson
nav_order: 2
---

# Installing SpaCy

## What is SpaCy?

[SpaCy](https://spacy.io/usage/spacy-101/) is a Python library for advanced natural language processing. We will be using SpaCy within the Python script we create to save us the time and labour of writing hundreds or thousands of lines of code. 

Another widely used platform for natural language processing with Python is NLTK, or Natural Language Toolkit, which connects you to a suite of resources and libraries to work with language data. SpaCy's pre-built workflow automates much of what you have to write explicitly in NLTK, such as tokenizing words and PoS tagging. Because SpaCy's developers have made design decisions for us, they have been able to optimize the workflow so that it performs many - but not all - NLP tasks more quickly than NLTK. 

The trade-off, of course, is that you have less control over what occurs in the workflow. While you can adjust some parameters in SpaCy, you may find that NLTK is a better for certain tasks. If you are interested in finding out more about NLTK, we encourage you to explore Alex Provo and Jay Brodeur's [text analysis lesson using NLTK](https://jasonbrodeur.github.io/dsi-text-prep/python.html#6-removing-stop-words-with-nltk--putting-it-all-together).

## Installing the SpaCy library

We will begin by installing the SpaCy library so that we can use it in our script.

To install SpaCy, in the console area of Spyder (the bottom-right pane in the default Spyder layout), type:

`pip install -U pip setuptools wheel
pip install spacy`

The first line of code updates , while the second installs SpaCy.

Hit `Enter` (Windows) / `Return` (Mac) to run the commands. The most recent version of SpaCy should be installed with the above command. 

## Installing language models

SpaCy provides trained language models, again saving us the time of training our own models. Be aware that .

You can [train your own model](https://spacy.io/usage/training) with SpaCy, but 

<br />
Next --> [Create the NLP object](object.html)
