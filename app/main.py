from flask import Flask, render_template
import requests
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    quote = data.get('content', 'No quote available')
    author = data.get('author', 'Unknown')
    quote_ru = translator.translate(quote, dest='ru').text
    author_ru = translator.translate(author, dest='ru').text
    return render_template('index.html', quote=quote_ru, author=author_ru)

if __name__ == '__main__':
    app.run(debug=True)