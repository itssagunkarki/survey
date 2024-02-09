from flask import Flask, render_template, request, jsonify, redirect, url_for
import questions
import os
import json
from datetime import datetime

app = Flask(__name__)

output_folder = os.path.join(os.getcwd(), 'output')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

@app.route('/')
def home():
    questions_dict = questions.get_questions('questions_template.xlsx', 'questions')
    return render_template('home.html', questions=questions_dict)

@app.route('/submit_first_entry', methods=['POST'])
def submit_first_entry():
    if request.method == 'POST':
        data = request.get_json()
        # Process the received data as needed
        # Generate timestamp for the filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output_{timestamp}.json"
        # Save the data to a file with the generated filename
        with open(os.path.join(output_folder, filename), 'w') as f:
            json.dump(data, f)
        # Redirect the user to the next screen
        return redirect(url_for('next_screen', filename=filename))
    else:
        # Handle other HTTP methods (optional)
        return jsonify({'error': 'Method Not Allowed'}), 405

@app.route('/next_screen/<filename>')
def next_screen(filename):
    # Read the data from the file using the provided filename
    with open(os.path.join(output_folder, filename), 'r') as f:
        data = json.load(f)
    return render_template('next_screen.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
