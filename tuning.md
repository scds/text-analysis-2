---
layout: default
title: Fine-tuning SpaCy
parent: Lesson
nav_order: 6
---

# Fine-tuning SpaCy

Although SpaCy does an impressive job of recognizing named entities, it falls short of being perfect. In fact, the first few lines of the "wollstonecraft.txt" document, when visualized with displaCy, contains several obvious named entities - "SWEDEN", "MARY WOLLSTONECRAFT", "CASSEL & COMPANY Limited" and so on - that SpaCy misses entirely. And yet, it is able to recognize those same entities at other points in the document. 

Although we can expect the small margin of error implied by an accuracy score of 0.90 for the *en_core_web_trf* language model, there are steps we can take in our script to fine-tune our results. 

![](assets/img/ner-misses.png)

## Restoring removed stop words

Stop words, as described in "[How Does NER Work?](ner.html)", are commonly occurring words that SpaCy and other NLP tools drop from the `Doc` object to economize on computing resources. [A full list of stop words](https://github.com/explosion/spaCy/blob/master/spacy/lang/en/stop_words.py) is listed on SpaCy's GitHub repository. There may, however, be cases in which we want to preserve the stop words within the corpus if they belong to named entites, like musicians with numbers in their names.

You can remove stopword from SpaCy's list by including the code below in your ner.py script (ensure that you wrap the term in quotation marks so that the console knows you are referring to a string):

```
nlp.Defaults.stop_words -= {"term1", "term2"}
```

Verify your results by typing into the console, which creates a variable called "stopwords" that contains SpaCy's stopwords:

```
stopwords = nlp.Defaults.stop_words
```

Followed by a command to print the contents of the *stopwords* variable:

```
print(stopwords)
```
![](assets/img/console-stopwords)

## Adding entity names

## Establish ground truth

<br />
Next --> [Other NER Tools](tools.html)
