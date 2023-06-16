from flask import Flask, request, jsonify
from pydantic import BaseModel
from parser import getNewsBBC
from topics import Topics
from multiprocessing import Process
import json
import time
from typing import Literal



class Settings(BaseModel):
    topic: Topics = Topics.Companies

class NewsContainter:
    newsList = []

sett = Settings()
app = Flask(__name__)
newsssss = NewsContainter()

@app.route('/NewsBBC', methods=['GET'])
def request_NewsBBC(): 
    temp = []
    global sett
    sett = Settings.parse_raw(json.dumps(__UploadData('setting.json')))
    json_string = __UploadData('DbFile.json')
    return jsonify(json.dumps(json_string))

@app.route('/ch_topic', methods=['POST'])
def ch_topic(): 
    data = request.get_json()

    print('----------------------------------------------------------------------')
    print(data)

    sett = Settings.parse_raw(json.dumps(data))
    __LoadData('setting.json', json.dumps(sett.__dict__))
    return jsonify({'req' : 'OK'})


def asycGettingNews():
    while True:
        sett = Settings.parse_raw(json.dumps(__UploadData('setting.json')))
        print(sett.topic.name)
        json_string = json.dumps([news.__dict__  for news in getNewsBBC(sett.topic)])
        __LoadData("DbFile.json", json_string)

        time.sleep(20)


def startServer():
    Process(target=asycGettingNews).start()
    app.run(debug=False)


def __UploadData(fileName: str) -> str:
    with open(fileName) as f:
        return json.load(f)

def __LoadData(fileName: str, jsonData: any) -> None:
    with open(fileName, 'w') as f:
          f.write(jsonData)

    
