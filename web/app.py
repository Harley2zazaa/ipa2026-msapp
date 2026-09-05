import os
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

mongo_uri = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")
db_name = os.environ.get("DB_NAME", "ipa2026")

client = MongoClient(mongo_uri)
mydb = client[db_name]
mycol = mydb["router"]
status_col = mydb["interface_status"]
data = []

@app.route("/")
def main():
    data = list(mycol.find()) 
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_comment():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")
    
    if ip and username and password:
        mycol.insert_one({
            "ip": ip,
            "username": username,
            "password" : password,
        })
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete_comment():
    ip = request.form.get("ip")
    
    if ip:
        mycol.delete_one({"ip": ip})
        
    return redirect("/")

@app.route("/router/<ip>")
def router_detail(ip):
    history = list(status_col.find({"router_ip": ip}))
    return render_template("router_detail.html", ip=ip, history=history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)