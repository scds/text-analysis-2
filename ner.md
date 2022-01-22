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

## A quick introduction to the computational text analysis workflow (pipeline)

How does an NER tool like CoreNLP or SpaCy go about identifying named entities within an unstructured text corpus, then?

### Tokenization

Most computational text analysis methods, including NER, first involve tokenizing the data - or segmenting the text into words based on the position of whitespace characters - so that each word can be examined individually. If you completed the “[Pre-processing Digitized Texts](https://scds.github.io/text-analysis-1)” workshop, you manually tokenized a text document in OpenRefine to make it possible to correct multiple errors with one operation. When performing computational text analysis, tokenization is done by the natural language processing system.

Once we can approach texts at the level of the word, other processing tasks in the text analysis workflow can then be performed such as:

### Stop word removal

Commonly used words - such as *the*, *of* and *its* in the English language - are typically filtered out from the corpus for the sake of efficiency because they are not likely to be of interest. With many NLP tools, it is possible to either add stop words that you may wish to ignore in your analysis or omit existing stop words from the list which are, in fact, relevant to your analysis.

### Part of speech (PoS or POS) tagging

PoS tagging is a form of annotation that evaluates each word to determine its correspondence to grammatical parts of speech such as nouns, pronouns, verbs, adverbs, adjectives and so on. Unlike the previous two tasks, which can be explicitly programmed with formal rules - like "create a new token each time a whitespace character is encountered" - PoS tagging and the other tasks that follow rely instead on machine learning to make generalized predictions about what tag is most appropriate. For example, whether "saw" is a verb or a noun given its context. 

NLP tools use trained language models to make their predictions, which are "taught" through many examples of the various categories being modelled. Often - and in the current lesson - you will be working with a model trained by someone else, like the developers of the tool. It is usually possible - if time-consuming - to train your own model if the tool's supplied model is inadequate for your purposes. 

As we might expect, how the tool arrives at its predictions can be utterly opaque to the user; we will discuss training data bias further in "[Behind the Interface](behind.html)." 

### Stemming or lemmatization


<br />
Next --> [Installing SpaCy](install.html)
