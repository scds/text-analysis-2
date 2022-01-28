---
layout: default
title: Fine-tuning SpaCy
parent: Lesson
nav_order: 6
---

# Fine-tuning SpaCy

Although SpaCy does an impressive job of recognizing named entities, it falls short of being perfect. In fact, the first few lines of the "wollstonecraft.txt" document contains several obvious named entities - "SWEDEN", "MARY WOLLSTONECRAFT", "CASSEL & COMPANY Limited" and so on - that SpaCy misses entirely. And yet, it is able to recognize those same entities at other points in the document. 

Although we can expect the small margin of error implied by an accuracy score of 0.90 given for the *en_core_web_trf* language model, there are steps we can take in our script to fine-tune our results. 

![](assets/img/ner-misses.png)

## Adjusting stopwords

## Adding entity names

## Establish ground truth

<br />
Next --> [Other NER Tools](tools.html)
