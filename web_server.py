from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Tanta luz parece um aeroporto!!"

def run():
  app.run(host='0.0.0.0',port=8080)

def web_server():
    t = Thread(target=run)
    t.start()