from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    
    # Contoh respon sederhana
    if "hukum pidana" in user_input.lower():
        response = "Hukum pidana adalah cabang hukum yang mengatur tentang perbuatan-perbuatan yang dianggap sebagai tindak pidana..."
    elif "unsur" in user_input.lower():
        response = "Unsur-unsur Hukum Pidana yaitu: Perbuatan, Melawan hukum, Kesalahan, Dipertanggungjawabkan..."
    elif "asas" in user_input.lower():
        response = "Asas-asas Hukum Pidana dalam KHUP: Asas Legalitas, Asas Wilayah atau Teritorial..."
    else:
        response = "Maaf, saya belum bisa menjawab pertanyaan itu."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
