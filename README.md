# Customer Review Text Analysis using NLTK 📝🔍

This project demonstrates basic Natural Language Processing (NLP) techniques using the `nltk` library in Python. The script processes customer reviews by performing sentence and word tokenization, removing stopwords, performing Part-of-Speech (POS) tagging, and extracting nouns.

## 📌 Features
- Tokenizes text into sentences and words
- Removes common stopwords
- Tags words with their respective POS
- Extracts and lists all nouns from the text

## 📜 Sample Input

"The product quality is amazing! I received my order on time, and the packaging was great. However, the customer support was not very responsive."

## 📊 Expected Output
Tokenized Sentences: ['The product quality is amazing!', 'I received my order on time, and the packaging was great.', 'However, the customer support was not very responsive.']

Tokenized Words: ['The', 'product', 'quality', 'is', 'amazing', ...]

Filtered Words (after removing stopwords): ['product', 'quality', 'amazing', ...]

POS Tagged Words: [('product', 'NN'), ('quality', 'NN'), ...]

Extracted Nouns: ['product', 'quality', 'order', 'time', 'packaging', 'customer', 'support']

