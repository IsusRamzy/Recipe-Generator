from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key='REPLACE WITH YOUR API KEY')
model = genai.GenerativeModel('gemini-1.5-pro')

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    prompt = request.form['prompt']
    recipe = model.generate_content(prompt)
    return render_template('index.html', recipe = recipe)    

if __name__ == '__main__': # Not imported, which means not WSGI
  app.run(debug=True)
