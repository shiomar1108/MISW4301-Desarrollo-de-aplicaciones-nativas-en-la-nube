from flask import Flask
import requests
import time
import threading
from os import environ as env


app = Flask(__name__)

@app.route('/poll/ping', methods=['GET'])
def health():
    return "pong"

def estado_solicitud():
    RF006_PATH = env['RF006_PATH']
    TRUENATIVE_PATH = env['TRUENATIVE_PATH']
    TRUENATIVE_TOKEN = env['TRUENATIVE_TOKEN']
    resp_tarjetas_por_verificar = requests.get(f"{RF006_PATH}/credit-cards/on-process")
    for tarjeta in resp_tarjetas_por_verificar.json():
        ruv = tarjeta['ruv']
        resp_trueNative = requests.get(f'{TRUENATIVE_PATH}/native/cards/{ruv}', headers={"Authorization":f"Bearer {TRUENATIVE_TOKEN}"})
        print(resp_trueNative.status_code)
        if resp_trueNative.status_code == 200:
            tarjeta_id = tarjeta['id']
            new_status = resp_trueNative.json()['status']
            data = {'id':tarjeta_id, 'status':new_status}            
            resp_actualizar_tarjeta = requests.post(f"{RF006_PATH}/credit-cards/update", json=data)            
        elif resp_trueNative.status_code == 202:
            resp_actualizar_tarjeta = "Solicitud en proceso"
        elif resp_trueNative.status_code == 404:
            resp_actualizar_tarjeta = "No existe una verificación en proceso con ese RUV"
        return resp_actualizar_tarjeta
    
    
def timer():
    while True:
        try:
            respuesta = estado_solicitud()
            if respuesta is None:
                print(f'Connection established --> No hay solicitudes en proceso', flush=True)
            elif isinstance(respuesta, requests.Response):
                print(f'Connection established --> card id: {respuesta.json()["id"]}, new status: {respuesta.json()["status"]}', flush=True)
            else:
                print(f'Connection established --> {respuesta}', flush=True)
        except:
            print('Connection NOT established', flush=True)           
        time.sleep(5)   

t = threading.Thread(target=timer)
t.start()