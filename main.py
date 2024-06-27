from flask import Flask, render_template, request
import google.generativeai as genai
import markdown

app = Flask(__name__)
genai.configure(api_key='API KEY')
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel('gemini-1.5-pro', generation_config=generation_config, system_instruction="You are the `recipe generator`.")

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    prompt = request.form['prompt']
    recipe = model.generate_content(prompt).text
    return render_template('index.html', recipe = markdown.markdown(recipe))    

if __name__ == '__main__': # Not imported, which means not WSGI
  app.run(debug=True)# 
