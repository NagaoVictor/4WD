from flask import Flask, render_template
import requests

app = Flask(__name__)

CARRINHO_IP = "http://192.168.1.105:5001"  # Altere para o IP do seu Raspberry Pi 5
CAMERA_URL = f"{CARRINHO_IP}/camera"      # URL do stream de câmera MJPEG

@app.route('/')
def index():
    return render_template("index.html", camera_url=CAMERA_URL)

@app.route('/frente')
def frente():
    requests.get(f"{CARRINHO_IP}/frente")
    return "Avançando"

@app.route('/tras')
def tras():
    requests.get(f"{CARRINHO_IP}/tras")
    return "Recuando"

@app.route('/esquerda')
def esquerda():
    requests.get(f"{CARRINHO_IP}/esquerda")
    return "Virando à esquerda"

@app.route('/direita')
def direita():
    requests.get(f"{CARRINHO_IP}/direita")
    return "Virando à direita"

@app.route('/parar')
def parar():
    requests.get(f"{CARRINHO_IP}/parar")
    return "Parando"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
