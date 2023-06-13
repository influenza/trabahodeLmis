from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS, cross_origin
import Conectio
number=None
arr=0;
pj="";
app=Flask(__name__)
cors = CORS(app)
@app.route("/my-datas", methods=["POST"])
@cross_origin(origins=['http://localhost:5173'])
def my_endpoint2():
    plusone = request.json['plusone']
    print(plusone)
    arr = Conectio.my_connetion()
    pj=f"{arr[0][0]}"
    print(pj)
    return pj

@app.route("/members", methods=["GET"])
def members():
  return{"members": pj}

if __name__ =="__main__":
    app.run(debug=True)