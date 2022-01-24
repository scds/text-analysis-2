---
layout: default
title: Creating the NLP Object
parent: Lesson
nav_order: 3
---

# Creating the NLP Object

SpaCy takes an object-oriented approach to NLP instead of treating text as strings, in contrast to NLTK. With Spacy, a `Doc` object contains a sequence of `Token` objects. The `Language` class is a text processing pipeline that contains resources like the and  used to process the `Doc` object, which allows the ; we the .

```

# Import SpaCy

import spacy

# Instantiate NLP pipeline object

nlp = spacy.load('en_core_web_trf')

```

Run the script (`F5`) and note the results in the console. Nothing much will happen but let us have a look at the top-right pane in Spyder that we have been ignoring thus far. Refresh the variables (`Ctrl` or `cmd` + `R`) and notice that we now have three new variable names and associated values: "doc," "filename" and "ner_text." T

In the console, you may receive a warning about CUDA device which is [a known issue with the transformer pipeline (*en_core_web_trf*)](https://github.com/explosion/spaCy/discussions/9571)

![](assets/img/spyder-variables1.png)

## Set up the environment

Before we start working with SpaCy, we will first save the Python script in Spyder to get a sense of where .  Save the file with the document. Move the "wollstonecraft.txt" file and any other text files you may be working with to the same directory (folder). While not a best practice from a file management standpoint, it simplifies having to specify the file path for the purposes of the lesson. In a production setting.

## Process the text



<br />
Next --> [Visualizing Named Entities](visualize.html)

