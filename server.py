import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model
import numpy as np
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import base64



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appDatabase6.db'
db = SQLAlchemy(app)

petTypeArray = ["Dog", "Cat", "Hamster", "Bird", "Other"]
timeArray = ["0-2 Hours", "2-4 Hours", "4-8 Hours", "8+ Hours"]
energyArray = ["Lazy", "Playful", "Energetic"]
experienceArray = ["None", "1-3 Years", "3-5 Years", "5+ Years"]
fosternum=0
matchnum = 0
fosterArr = []

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base64Val = db.Column(db.String)
    description = db.Column(db.String)
    name = db.Column(db.String)
    

with app.app_context():
    db.create_all()

@app.route('/match', methods=['GET'])
def match():
    global matchnum
    petTypeIndex = int(request.args.get('petType'))
    petType = petTypeArray[petTypeIndex]
    timeIndex = int(request.args.get('time'))
    time = timeArray[timeIndex]
    energyIndex = int(request.args.get('energy'))
    energy = energyArray[energyIndex]
    experienceIndex = int(request.args.get('experience'))
    experience = experienceArray[petTypeIndex]
    
    global fosterArr
    # Make predictions on new data
    if (matchnum < 9):
        matchnum +=1
        fosterArr.append(model.predict([petTypeIndex, timeIndex, energyIndex, experienceIndex]))


    return 'Entry added successfully!'


@app.route('/foster', methods=['GET'])
def foster():
    global fosternum 
    entries = Entry.query.order_by(Entry.id).limit(10).all()
    result =["" +  entries[fosternum].description + ',' + entries[fosternum].name + ',' + str(entries[fosternum+1].id) +  ',' + (entries[fosternum].base64Val)[2:-1] + ",1"]
    if (fosternum < 9): 
        fosternum +=1
        return fosterArr[fosternum]
    else:
        fosternum = 0
    
    return result


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=False, host="172.20.10.2", port=5000)

request