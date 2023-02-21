# import flask pada file app.py dan panggil fungsi flask 
# Setelah membuat homepage pada file index.html, untuk melakukan proses render aplikasi flask gunakan library yang bernama “render_template” dengan cara melakukan import.

from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


# tentukan route/alamat yang akan digunakan untuk halaman website
@app.route("/")
def index():
    foto = 'static/image/arda.jpeg'
    return render_template('index.html', foto=foto)
    

# buat conditional run dengan kondisi dimana program akan berjalan jika yang di running adalah function main/utama
if __name__ == "__main__":
    app.run(debug=True)


