---
layout: default
title: Creating the Doc Object
parent: Lesson
nav_order: 3
---

# Creating the Doc Object

SpaCy takes an object-oriented approach to NLP instead of treating text as strings the way NLTK does. With Spacy, the `Doc` object contains a sequence of `Token` objects. The `Language` class is a text processing pipeline that contains resources like a shared vocabulary and the various workflow components, and is used to create the `Doc` object from text (usually via the *nlp* variable). The `Doc` object is what we work with when we ask SpaCy to return candidates for named entities (`ents`), as an example. We will come across these concepts as we write our Python script. 

## Set up the environment

Before we start working with SpaCy, we will first save the Python script in Spyder (File > Save or `Ctrl` / `cmd` + `S`). Spyder will choose a default location which you can change if you would like to keep your Python scripts in an easier-to-locate spot. Going forward, Spyder will continue to save any new files to the folder you choose. You can choose your own name for the Python script, but we will refer to it as "ner.py" for consistency.

**IMPORTANT**: Move the "wollstonecraft.txt" file and any other text files you may be working with to the same directory (folder) as the Python script you are creating. While not a best practice from a file management standpoint, it simplifies having to specify the file path in our script for the purposes of the lesson.

## Process the text

Although we have installed the SpaCy library, we need to let Python know to call it up for our use. Just as downloading all Python packages would result in a giant file size, so too would loading them all at once slow Python down to an imperceptible crawl.

Copy and paste the code below in the ner.py file, or write it out for additional practice. If you receive an error when you run the code in the console, compare what is in your file with the code below - programming languages are very particular!

```

# Import SpaCy library
import spacy

# Instantiate NLP pipeline object
nlp = spacy.load('en_core_web_trf')

```

![](assets/img/spacy-nlp.png)

Next, we create the `Doc` object.

```

# Assign the filename to a variable
filename = 'wollstonecraft.txt'

# Make the text of the file available to our script
ner_text = open(filename).read()

# Create the Doc object by passing it through the text pipleine (nlp)
doc = nlp(ner_text)

```

![](assets/img/spacy-doc.png)

In the above code, we create the `Doc` object as described earlier and assign it to the *doc* variable. If you would like to work with your own documents, simply change the *filename* variable to the name of your text file (verifying that it is also in the same folder as the ner.py script).

Run the script (`F5`) and note the results in the console. Nothing much will happen but let us have a look at the top-right pane in Spyder that we have been ignoring thus far. Select the "Variable Explorer" tab and notice that we have three variable names and associated values: "doc," "filename" and "ner_text" that we created by running the script.

![](assets/img/spyder-variables1.png)

Checking the status of our variables let us know that we have successfully connected to our document, as evidenced by the *filename* and *ner_text* variables, and that we now have a `Doc` object, *doc*, to work with.

We are now ready to

```
# Run NER on the Doc object
for ent in doc.ents:    
    print(ent.text, ent.start_char, ent.end_char, ent.label_, spacy.explain(ent.label_))
```

When running the code in the console, be patient! It will likely take a few minutes for your results to appear but they will print out in the console.

Refresh the variables (`Ctrl` / `cmd` + `R`) and notice that we now have three new variable names and associated values: "doc," "filename" and "ner_text."



In the console, you may receive a warning about CUDA device which is [a known issue with the transformer pipeline (*en_core_web_trf*)](https://github.com/explosion/spaCy/discussions/9571).




<br />
Next --> [Visualizing Named Entities](visualize.html)

