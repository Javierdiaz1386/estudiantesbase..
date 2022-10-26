from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from waitress import serve



app=Flask(__name__)

if __name__=='__main__':
    app.run('127.0.0.1',8080)