# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:35:20 2019

@author: 10649929
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph="""I have three visions for India.
             In 3000 years of our history people from all over the world have come and invaded us,
             captured our lands, conquered our minds. From Alexander onwards the Greeks, 
             the Turks, the Moguls, the Portuguese, the British, the French, the Dutch,
             all of them came and looted us, took over what was ours.
             Yet we have not done this to any other nation. We have not conquered anyone.
             We have not grabbed their land, their culture and their history and tried to 
             enforce our way of life on them. Why? Because we respect the freedom of others. 
             That is why my FIRST VISION is that of FREEDOM. 
             I believe that India got its first vision of this in 1857,
             when we started the war of Independence. It is this freedom 
             that we must protect and nurture and build on. 
             If we are not free, no one will respect us."""

sentences= nltk.sent_tokenize(paragraph)
stemmer= PorterStemmer()

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=''.join(words)
    