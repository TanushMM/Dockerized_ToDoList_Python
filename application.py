from flask import Flask, url_for, redirect, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://db:27017/')
db = client['todo']
collection = db['list']

application = Flask(__name__)

@application.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        heading = request.form['heading']
        content = request.form['content']
        
        collection.insert_one(
            {"heading":heading, "content":content}
        )
        
    data = collection.find()
    return render_template('index.html', data=data)

@application.route('/delete/<id>', methods=["POST"])
def delete(id):
    collection.delete_one(
        {"_id": ObjectId(id)}
    )
    return redirect(url_for('home'))


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)