from flask import Flask, render_template, request, jsonify
import json
import questions
import os

app = Flask(__name__)

output_folder = os.path.join(os.getcwd(), 'output')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

@app.route('/')
def home():
    questions_dict = questions.get_questions('questions_template.xlsx', 'questions')
    return render_template('home.html', questions=questions_dict)



if __name__ == '__main__':
    app.run(debug=True)
