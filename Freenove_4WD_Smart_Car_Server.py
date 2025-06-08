# Freenove_4WD_Smart_Car_Server.py adaptado para integração com painel externo
# Este é um exemplo simplificado. Substitua chamadas de GPIO conforme necessário.

from flask import Flask
import time

app = Flask(__name__)

@app.route('/frente')
def frente():
    print("Movendo para frente")
    # Aqui você colocaria motor.forward()
    return "Frente"

@app.route('/tras')
def tras():
    print("Movendo para trás")
    return "Trás"

@app.route('/esquerda')
def esquerda():
    print("Virando para esquerda")
    return "Esquerda"

@app.route('/direita')
def direita():
    print("Virando para direita")
    return "Direita"

@app.route('/parar')
def parar():
    print("Parando os motores")
    return "Parar"

@app.route('/camera')
def camera():
    # Este endpoint seria usado para stream MJPEG
    return "Camera stream em outro serviço"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
