from flask import Flask, render_template, request, jsonify
import os
import random
from dotenv import load_dotenv
import google.generativeai as genai

# .env dosyasını yükle
load_dotenv()
API = os.getenv("API_KEY")
genai.configure(api_key=API)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

def load_kotusozy(txt_file):
    """Kötü sözleri yükle"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, txt_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def load_kotukufurler(txt_file):
    """Küfürleri yükle"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, txt_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    """Ana sayfa render"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Kullanıcıdan gelen mesajı işleyip yanıt döner"""
    user_input = request.form.get('user_input', '').strip()
    if not user_input:
        return jsonify({'response': "Lütfen bir mesaj girin."}), 400

    # Kötü sözleri kontrol et
    kotusozy = load_kotusozy('bad_words.txt')
    if any(kot in user_input.lower() for kot in kotusozy):
        # Kötü söz varsa küfürleri yükle
        kotukufurler = load_kotukufurler('kufurler.txt')
        if kotukufurler:  # Eğer küfürler listesi boş değilse
            response = random.choice(kotukufurler)
        else:
            response = "Küfür listesi boş."
    else:
        if user_input.lower() == "çıkış":
            return jsonify({'response': "Çıkış Yapıldı..."})
        else:
            # Model ile yanıt oluşturma
            try:
                # Türkçe örnek bir cümle ekleyin
                model_response = model.generate_content(f"Türkçe yanıt ver: {user_input}")
                response = model_response.text
            except Exception as e:
                response = f"Hata: {str(e)}"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
