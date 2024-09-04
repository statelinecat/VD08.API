from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    quote = data.get('content', 'No quote available')
    author = data.get('author', 'Unknown')
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)