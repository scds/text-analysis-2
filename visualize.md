---
layout: default
title: Visualizing Named Entities
parent: Lesson
nav_order: 4
---

# Visualizing Named Entities with SpaCy

## Creating HTML output

## Interpreting the results

If you would like to see the full list of entities, type the following command in the console:

`
print(nlp.pipe_labels['ner'])
`

It will return a list of 18 entity types:

| Entity Type | Type Description |
| ----------- | ---------------- |
| CARDINAL | Numerals that do not fall under another type |
| DATE | Absolute or relative dates or periods |
| EVENT | Named hurricanes, battles, wars, sports events, etc. |
| FAC | Buildings, airports, highways, bridges, etc. |
| GPE | Countries, cities, states |
| LANGUAGE | Any named language |
| LAW | Named documents made into law |
| LOC | Non-GPE locations, mountain ranges, bodies of water |
| MONEY | Monetary values, including unit |
| NORP | Nationalities or religious or political groups |
| ORDINAL | "first", "second", etc. |
| ORG | Companies, agencies, institutions, etc. |
| PERCENT | Percentage, including "%" |
| PERSON | People, including fictional |
| PRODUCT | Objects, vehicles, foods, etc. (not services) |
| QUANTITY | Measurements, as of weight or distance |
| TIME | Times smaller than a day |
| WORK_OF_ART | Titles of books, songs, etc. |


SpaCy also allows you to create your own entity types.

<br />
Next --> [Identifying Key Terms](key.html)
