[Documentation](https://pypi.org/project/rake-nltk/#description)
RAKE (Rapid Automatic Keyword Extraction) is a well-known keyword extraction method that finds the most relevant words or phrases in a piece of text using a set of stopwords and phrase delimiters. Rake nltk is an expanded version of RAKE that is supported by NLTK. The steps for Rapid Automatic Keyword
# Uses stopwords for english from NLTK, and all puntuation characters by
# default
```
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text(<text to process>)

# Extraction given the list of strings where each string is a sentence.
r.extract_keywords_from_sentences(<list of sentences>)

# To get keyword phrases ranked highest to lowest.
r.get_ranked_phrases()

# To get keyword phrases ranked highest to lowest with scores.
r.get_ranked_phrases_with_scores()
```
