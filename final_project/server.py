from machinetranslation import translator
from flask import Flask, render_template, request
import json
from machinetranslation import english_to_french, french_to_english
app = Flask("Web Translator")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french_translation():
    english_text = request.form['english_text']
    french_text = english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english_translation():
    french_text = request.form['french_text']
    english_text = french_to_english(french_text)
    return english_text
    
@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
