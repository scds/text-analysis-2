---
layout: default
title: Visualizing Named Entities
parent: Lesson
nav_order: 4
---

# Visualizing Named Entities with SpaCy

To render the output from spaCy in a form more amenable to analysis, we will use spaCy's built-in visualizer: displaCy.

## Creating HTML output

DisplaCy uses JavaScript, SVG and CSS - web design and programming languages - to render visualizations of entities and dependencies in a web browser.

To begin, we will comment out the code we previously wrote which printed entities to the console as we do not need it at the moment. You can precede each of the lines with the "#" symbol or you can wrap the three lines of code in triple-quotes as demonstrated in the example below. We are not *technically* commenting out the code but we are turning it into a string that Python will ignore. 

```
"""
# Run NER on the Doc object
for ent in doc.ents:    
    print(ent.text, ent.start_char, ent.end_char, ent.label_, 
          spacy.explain(ent.label_))
"""
```

Next, we will import displaCy just as we did with the SpaCy library. Under our initial import statement, add `from space import displacy`. That is:

```
# Import SpaCy library
import spacy
from spacy import displacy
```

With displaCy imported, we can now make use of it to visualize named entities by adding the following at the end of our ner.py script:

`
# Create a visualization of entities in context
displacy.serve(doc, style='ent')
`
![](assets/img/spacy-displacy.png)

DisplaCy will 

When the console returns:

> Using the 'ent' visualizer
> Serving on http://0.0.0.0:5000 ...

Open a web browser, and visit the following URL:

`http://localhost:5000/`

You should have a web page with the 

![](assets/img/displacy-server.png)

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
