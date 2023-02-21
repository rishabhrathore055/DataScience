from flask import Flask, render_template, request
from rake_nltk import Rake

app = Flask(__name__) # __name__ is the name of the current python module

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['GET', 'POST'])
def process(text):
    if request.method == 'POST':
        text = request.form.get('text')
        print(text)
    r = Rake()
    r.extract_keywords_from_text(text)
    result = r.get_ranked_phrases()
    num_of_keywords = result.count()
    return render_template('index.html', results=result, num_of_keywords=num_of_keywords)

if __name__ == '__main__':
    app.run(debug=True)















# from rake_nltk import Rake
# def keywordExtrator(text):
#     r = Rake()
#     r.extract_keywords_from_text(text)
#     return r.get_ranked_phrases()


# def keywords(text):
#     r = Rake()
#     r.extract_keywords_from_text(text)
#     return r.get_ranked_phrases()
# print(keywords("This article was published as a part of the Data Science Blogathon.IntroductionKeyword extraction is commonly used to extract key information from a series of paragraphs or documents. Keyword extraction is an automated method of extracting the most relevant words and phrases from text input. It is a text analysis method that involves automatically extracting the most important words and expressions from a page. It assists in the summarization of a text's content and the identification of key issues being discussed For example, meeting minutes (MOM)."))