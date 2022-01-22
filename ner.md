---
layout: default
title: How does NER work?
parent: Lesson
nav_order: 1
---

# How Does Named Entity Recognition (NER) Work?

## Recognizing named entities in texts

Named entity recognition (NER) identifies features of interest - such as names of people, places and organizations, in addtion to dates, currency and other special categories of nouns - within language data (e.g. unstructured text).

The best way to grasp NER is to try it out! Visit the [CoreNLP demo](https://corenlp.run/) and paste a short passage of text containing at least some proper names into the "--Text to annotate--" field (the maximum number of characters in the online demo is 5000).

![](assets/img/coreNLP-interface.png)

Remove the "parts-of-speech" and "dependency parse" options from the "Annotations" field to limit our results to named entities and submit the text for analysis.

![](assets/img/coreNLP-ner.png)

In the screenshot above, CoreNLP has annotated the text from a [Wikipedia article on the American-Canadian anti-slavery activist Mary Ann Shadd](https://en.wikipedia.org/wiki/Mary_Ann_Shadd), tagging words (tokens) with labels like "Person," "Country," "Organization," and "Date." 

Although we can appreciate the utility of CoreNLP annotations in analyzing texts, the 5000 character maximum of the web-based version makes it impractical to scale up for larger corpora. You can download the full version of [CoreNLP](https://stanfordnlp.github.io/CoreNLP/) to experiment with but we will be using a different NLP tool, SpaCy, for the lesson.




<br />
Next --> [Installing SpaCy](install.html)
