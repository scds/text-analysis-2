# -*- coding: utf-8 -*-

"""

Script developed for the Sherman Centre for Digital Scholarship's "Do More with Digital Scholarship"
workshop series on computational text analysis:

* Reads a document
* Passes it through SpaCy's transformer English pipeline
* Identifies named entities in the document, visualizes them in the context of the document and returns the most frequently used entities

Kludged together by Devon Mordell (mordelld@mcmaster.ca).

"""

# Import Counter to count named entities
from collections import Counter

# Import SpaCy library
import spacy
from spacy import displacy

# Import matplotlib.pyplot to create bar graph
import matplotlib.pyplot as plt

# Instantiate NLP pipeline
nlp = spacy.load('en_core_web_trf')

""" FINE TUNING THE MODEL
# Remove specific words from stop words list
nlp.Defaults.stop_words -= {"term1", "term2"}

# Add the Entity Ruler component to the pipeline
ruler = nlp.add_pipe('entity_ruler')

# Specify entities to recognize
patterns = [{'label': 'PERSON', 'pattern': 'Kingston'}, 
            {'label': 'LOC', 'pattern': [{'LOWER': 'continent'}]}]
ruler.add_patterns(patterns)

"""

# Assign the filename to a variable
filename = 'wollstonecraft.txt'

# Make the text of the file available to our script
ner_text = open(filename).read()

# Create the Doc object by passing it through the text pipeline (nlp)
doc = nlp(ner_text)

""" ADDITIONAL NER TASKS
# Run NER on the Doc object
for ent in doc.ents:    
    print(ent.text, ent.start_char, ent.end_char, ent.label_, spacy.explain(ent.label_))

# Create a visualization of entities in context  
displacy.serve(doc, style='ent')

"""

# Render displaCy visualization as HTML output
html = displacy.render(doc, style='ent', page=True)


# Create a new file and write contents of html variable to it
f = open('wollstonecraft.html', 'w')
f.write(html)
f.close()

# Return a list of persons and print the 15 most commonly occurring values
persons = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ == 'PERSON']
print(Counter(persons).most_common(15))

# Assign 10 most common named entities to variables for plotting
entities = [ent.text for ent in doc.ents]
labels, values = zip(*(Counter(entities).most_common(10)))

# Plot the most common entities
plt.bar(labels, values)
plt.xticks(fontsize=7.5, rotation=45)
plt.show()




