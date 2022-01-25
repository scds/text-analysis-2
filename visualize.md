---
layout: default
title: Visualizing Named Entities
parent: Lesson
nav_order: 4
---

# Visualizing Named Entities with SpaCy

To render the output from SpaCy in a form more amenable to analysis, we will use SpaCy's built-in visualizer: displaCy.

## Using the displaCy server

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

Next, we will import displaCy just as we did with the SpaCy library. Under our initial import statement, add `from space import displacy`:

```
# Import SpaCy library
import spacy
from spacy import displacy
```

With displaCy imported, we can now make use of it to visualize named entities by adding the following lines of code to the end of our ner.py script:

```
# Create a visualization of entities in context
displacy.serve(doc, style='ent')
```

![](assets/img/spacy-displacy.png)

DisplaCy will start up a simple web server on your local machine to produduce a visualization that you can access through your web browser.

After running the script (`F5`), wait until the console returns:

> Using the 'ent' visualizer
> 
> Serving on http://0.0.0.0:5000 ...

Because SpaCy has to process the entire `Doc` object, it might take a few minutes for the message to appear! When te server is ready, open a web browser and go to the following URL:

```
http://localhost:5000/
```

You should now have a web page with the contents of the "wollstonecraft.txt" document marked up to show named entities.

![](assets/img/displacy-server.png)

## Interpreting the results

Some of the named entity labels may be obvious - such as PERSON - but others are more cryptic. If you would like to see the full list of entities that SpaCy recognizes, type the following command in the console:

```
print(nlp.pipe_labels['ner'])
```

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


In reviewing your results, you will likely notice some errors - named entities that SpaCy has missed or misclassified. Recall that the *en_core_web_trf* model has an accuracy evaluation score of about 0.90 - which is better than SpaCy's other trained English models, but not perfect!

## Stopping the displaCy server

The server that displaCy creates will continue to run until we stop the process in the console. To stop the command, use the small square icon at the top right of the console - which will be red when a command is running - or from Spyder's menu area: Consoles > Interrupt kernel.

![](assets/img/console-stop.png)

## Outputting displaCy visualizations to HTML and SVG

Although using the displaCy server may suffice for exploratory data analysis, you may want to create a more permanent representation to present or easily refer to later. Adding the next few lines of code to the end of your ner.py script will create an HTML file called "wollstonecraft.html" in the same directory as your Python script. Comment out or delete the previous `displacy.serve` code as we do not need the server to create the file.

```
# Render displaCy visualization as HTML output
html = displacy.render(doc, style='ent', page=True)

# Create a new file and write contents of html variable to it
f = open('wollstonecraft.html', 'w')
f.write(html)
f.close()
html = displacy.render(doc, style="ent", page=True)
```
![](assets/img/displacy-html.png)

<br />
Next --> [Identifying Key Terms](key.html)
