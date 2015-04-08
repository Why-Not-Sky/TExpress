#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# -*- coding: iso-8859-15 -*-
https://www.safaribooksonline.com/library/view/natural-language-processing/9780596803346/ch03s05.html
"""
import re

word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)

#Let’s look for all sequences of two or more vowels in some text, and determine their relative frequency
import nltk

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
print fd.items()

