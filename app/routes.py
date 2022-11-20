from app import app
from flask import render_template, request, jsonify
import json
from main import main

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#Recieves the text and sends back image
@app.route('/imagegen', methods=['POST'])
def generate_image():

    #extract text,style and return generated image
    data = request.get_json()
    text = (data["text"])
    style = data["style"]
    if text != "" and len(text) > 20:
        #gen the image
        imagelink,soundLink = main(text,style)
        returnValue = {"imagelink":imagelink,"soundLink":soundLink}
        #TODO: return sound as well if it is not none 
        return jsonify(returnValue)
        

  
    
    


    #return error thing 
    return jsonify("https://thumbs.dreamstime.com/z/error-sign-13724053.jpg")
