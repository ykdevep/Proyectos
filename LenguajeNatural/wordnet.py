##
## Cargando librerías necesarias
##
import nltk
from nltk.corpus import wordnet

##
## Palabras a determinar similaridad
##
book = wordnet.synset('book.n.01')
magazine = wordnet.synset('magazine.n.01')
manuscript = wordnet.synset('manuscript.n.01')

##
## Usando path_similarity con 1. book, 2. magazine, 3. manuscript
##
print ("   ")
print ("Usando path_similarity para dos palabras (1. book, 2. magazine)")
print ("La similitud entre las palabras es " + str(wordnet.path_similarity(book, magazine)))
print ("   ")
print ("Usando path_similarity para dos palabras (1. book, 2. manuscript)")
print ("La similitud entre las palabras es " + str(wordnet.path_similarity(book, manuscript)))
print ("   ")
print ("Usando path_similarity para una misma palabra (1. book)")
print ("La similitud entre las palabras es " + str(wordnet.path_similarity(book, book)))
print ("   ")

##
## Usando lch_similarity con 1. book, 2. magazine, 3. manuscript
##
print ("Usando lch_similarity para dos palabras (1. book, 2. magazine)")
print ("La similitud entre las palabras es " + str(wordnet.lch_similarity(book, magazine)))
print ("   ")
print ("Usando lch_similarity para dos palabras (1. book, 2. manuscript)")
print ("La similitud entre las palabras es " + str(wordnet.lch_similarity(book, manuscript)))
print ("   ")
print ("Usando lch_similarity para una misma palabra (1. book)")
print ("La similitud entre las palabras es " + str(wordnet.lch_similarity(book, book)))
print ("   ")

##
## Usando wup_similarity con 1. book, 2. magazine, 3. manuscript
##
print ("Usando wup_similarity para dos palabras (1. book, 2. magazine)")
print ("La similitud entre las palabras es " + str(wordnet.wup_similarity(book, magazine)))
print ("   ")
print ("Usando wup_similarity para dos palabras (1. book, 2. manuscript)")
print ("La similitud entre las palabras es " + str(wordnet.wup_similarity(book, manuscript)))
print ("   ")
print ("Usando wup_similarity para una misma palabra (1. book)")
print ("La similitud entre las palabras es " + str(wordnet.wup_similarity(book, book)))
print ("   ")