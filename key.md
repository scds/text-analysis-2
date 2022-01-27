---
layout: default
title: Identifying Key Terms
parent: Lesson
nav_order: 5
---

# Identifying Key Terms

We have an overall sense of the named entities in our document - but which ones appear most frequently? We can draw from an existing Python module, `collections`, to count our named entities.

## Counting named entities

The `collections` module is built in to Python, so we do not need to install it as we did with SpaCy. We do, however, need to let Python know that we want to use it. Underneath `from spacy import displacy`, write:

```
from collections import Counter
```

Then, at the end of the ner.py script:

```
# Return a list of named entities and print the 15 most commonly occurring values
entities = [(ent.text, ent.label_) for ent in doc.ents]
print(Counter(entities).most_common(15))
```

Again, we can comment out the code from the previous step where we created an HTML file visualizing named entities for the time being. In Spyder, you may receive a code analysis warning next to `from spacy import displacy` because you are no longer using displaCy at all in the script. You can ignore it!

![](assets/img/spacy-key.png)

Run the script, which will return the 15 most frequently occurring entities. You can adjust the number of entities by changing the argument (value) of `.most_common()`.

![](assets/img/key-results.png)

You can also limit the scope of the count to a specific entity type - if you are only interested in persons mentioned, for example.

After `doc.ents`, add `if ent.label_ == 'PERSON'` to limit the results to named entities of the type 'PERSON' only. We will assign the returned values to the variable `persons` to more accurately reflect the output.

```
persons = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ == 'PERSON']    
print(Counter(persons).most_common(15))
```

![](assets/img/key-persons.png)

> ***Caveat: on the limits of counting in computational text analysis***
> 
> *Although counting terms in a corpus can point us towards avenues for further investigation, there are numerous points within the text analysis workflow that may lead to inaccurate counts: OCR errors, variations in spelling, mis- or missed classification by SpaCy and so on. Not to mention that we do not know the manner in which terms are used without verifying the context of their appearance. All to say: counts can be unreliable, so delve deeper into the corpus before making any claims about the text!

## Visualizing key terms

Visualizations are often used in exploratory data analysis as they can quickly convey information to sighted . In addition to  Matplotlib.

If you are using the Anaconda environment as the launchpad for Spyder, Matplotlib should already be installed.

The labels are quite tiny for the purpose, ironically, of being able to read them more easily. We can refer back to the Variable Explorer to .

You can also save the plot as a PNG file directly from the "Plots" tab in Spyder. Right click on the plot and select "Save plot as..." (`Ctrl` / `cmd` + `S`).

The plot output is unlikely to win any visualization beauty contests but useful enough for the purposes of exploratory data analysis. Styling the bar graph is out of the scope of the current lesson, but you can find out more by visiting the [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html).

## Try it with your own data

In less than 50 lines of code - spaces included - we have a script that identifies and visualizes names entities, counts them and plots the most frequently occurring terms. Working through the code step by step, you should now have an idea of what each part of the script does, so that you can uncomment the code you wish to use and run the full script with your own data. Try it out!

<br />
Next --> [Other NER Tools](tools.html)
