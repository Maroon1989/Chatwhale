from flask import Flask,render_template,request,jsonify
import demo_code
from demo_code.demo_1 import GLM
import requests
glm_list = []
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html")
@app.route('/ocr',methods=['POST'])
def handle_ocr():
    # if request.method == 'POST';
    pdf = request.files['pdf']
    return jsonify(message="PDF processed successfully.")

@app.route('/qa',methods=['POST'])
def get_question():
    data = request.get_json()
    question = data['question']
    return jsonify(answer=f"Answer to '{question}'.")

@app.route('/glm<int:dialog_id>',method=['POST'])
def create_new_window(dialog_id):
    glm = GLM()
    model = glm.model
    glm_list.appned(model)
    return jsonify(message=f"New dialog {dialog_id} created.")
