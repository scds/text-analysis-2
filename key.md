---
layout: default
title: Identifying Key Terms
parent: Lesson
nav_order: 5
---

# Identifying Key Terms

We have an overall sense of the named entities in our document - but which ones appear most frequently? We can draw from an existing Python module, *collections*, to count our named entities.

## Counting named entities

The *collections* module is built in to Python, so we do not need to install it as we did with SpaCy. We do, however, need to let Python know that we want to use it. Underneath `from spacy import displacy`, write:

```
from collections import Counter
```

And then at the end of the ner.py script:

```
# Return a list of named entities and print the 15 most numerous values
items = [(ent.text, ent.label_) for ent in doc.ents]
print(Counter(items).most_common(15))
```

Again, we can comment out the code from the previous step where we created an HTML file visualizing named entities for the time being. In Spyder, you may receive a code analysis warning next to `from spacy import displacy` because you are no longer using displaCy at all in the script. You can ignore it!

![](assets/img/spacy-key.png)

Run the script, which will return the 15 most frequently occurring entities.

![](assets/img/key-results.png)

Alternatively, you can limit the scope of the count to a specific entity type - if you are only interested in persons mentioned, for example.

After `doc.ents`, add `if ent.label_ == 'PERSON'` to limit the results to named entities of the type 'PERSON' only.

```
items = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ == 'PERSON']    
print(Counter(items).most_common(15))
```

![](assets/img/key-persons.png)

> ***Caveat: on the limits of counting in computational text analysis***
> *There are numerous points within the workflow that may lead to errors. Counts are unreliable.

## Visualizing key terms

##Caveats: on the limits of counting in computational text analysis

<br />
Next --> [Other NER Tools](tools.html)
