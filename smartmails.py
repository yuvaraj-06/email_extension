from flask import Flask, render_template, request, jsonify, render_template, url_for
import json
import openai
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
 
API_KEY = "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"
DEFAULT_PROMPT = open("data.txt").read()

@app.route('/<string:page_name>/')
def render_static(page_name):
    url_for('static', filename = 'Chart.js')
    return render_template('popup.html')

@app.route('/postmethod', methods = ['POST'])
def get_post_email_data():
    print("-------------------------------------")
    jsdata = request.form['data']
    print(jsdata)
    data_mail=compute(jsdata)
    print(data_mail)
    return json.dumps({"present":data_mail,"mod":"yuvaraj isi goikdnjvidnjlifjdlibngflibnln"})


def compute(mail_prompt):
  openai.api_key = API_KEY
  p= DEFAULT_PROMPT.format(mail_prompt)     
  kwargs ={
           "engine":"davinci",
            "temperature":0.9,
            "max_tokens":74,
            "top_p":1,
            "frequency_penalty":0.36,
            "presence_penalty":0.75,
            "stop": ["Input:"]
        }
  return openai.Completion.create(prompt=p, **kwargs)["choices"][0]["text"].strip()
if __name__ == '__main__':
      app.run(debug = True)
print(compute("write a formal email as yuvaraj ,  thanking abbas for connecting and ask  hamet when can we meet according to his avaiblity"))