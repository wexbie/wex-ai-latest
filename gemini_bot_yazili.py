from flask import Flask, render_template, request, jsonify, session
import os
from dotenv import load_dotenv
import google.generativeai as genai
import markdown

load_dotenv()
API = os.getenv("API_KEY")
genai.configure(api_key=API)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
app.secret_key = os.urandom(24)

def kufurleri_yukle(txt_file):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, txt_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input', '').strip()
    if not user_input:
        return jsonify({'response': "Lütfen bir mesaj girin."}), 400
    kufurler = kufurleri_yukle('kufurler.txt')
    if any(kufur in user_input.lower() for kufur in kufurler):
        response = "Lütfen daha uygun bir dil kullanalım. Yardımcı olabileceğim bir şey var mı?"
    else:
        if user_input.lower() == "çıkış":
            session.pop('history', None)
            return jsonify({'response': "Çıkış Yapıldı..."})
        history = session.get('history', [])
        if len(history) > 10:
            history = history[-10:]
        history.append(f"Kullanıcı: {user_input}")
        try:
            prompt = f"Türkçe yanıt ver: {user_input}\nKonuşma Geçmişi: {history}"
            model_response = model.generate_content(prompt)
            response = model_response.text
            history.append(f"Bot: {response}")
            session['history'] = history
            response = markdown.markdown(response, extensions=['fenced_code', 'tables', 'nl2br', 'footnotes'])
            response = f'<div class="markdown-response" style="margin: 1em 0; line-height: 1.6;">{response}</div>'
        except Exception as e:
            response = f"Hata: {str(e)}"
    return jsonify({'response': response})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)