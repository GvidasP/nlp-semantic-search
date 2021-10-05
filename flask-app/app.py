from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from os.path import join, dirname

from universal_sentence_encoding import search_articles

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, template_folder="./dist", static_folder="./dist/static")
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def serve():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def search():
    search_text = request.args.get('search')

    articles = search_articles(search_text)
    articles.columns = articles.columns.str.lower()

    return articles.to_json(orient='records')


if __name__ == '__main__':
    app.run()
