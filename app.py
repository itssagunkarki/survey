from flask import Flask, render_template, request, jsonify, redirect, url_for
import questions
import os
import json
from datetime import datetime

app = Flask(__name__)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_folder = os.path.join(os.getcwd(), 'output')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

def delete_folder(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def clear_temp_folder():
    temp_first_folder = os.path.join(output_folder, 'temp_first_entry')
    temp_last_folder = os.path.join(output_folder, 'temp_last_entry')
    delete_folder(temp_first_folder)
    delete_folder(temp_last_folder)


@app.route('/')
def home():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clear_temp_folder()
    questions_dict = questions.get_questions('questions_template.xlsx', 'questions')
    return render_template('home.html', questions=questions_dict)

@app.route('/submit_first_entry', methods=['POST'])
def submit_first_entry():
    if request.method == 'POST':
        data = request.get_json()
        # Process the received data as needed
        # Generate timestamp for the filename
        filename = f"output_{timestamp}.json"
        # Save the data to a file with the generated filename
        with open(os.path.join(output_folder, "temp_first_entry", filename), 'w') as f:
            json.dump(data, f)
        # Redirect the user to the next screen
        return redirect(url_for('next_screen', filename=filename))
    else:
        # Handle other HTTP methods (optional)
        return jsonify({'error': 'Method Not Allowed'}), 405

@app.route('/next_screen/<filename>')
def next_screen(filename):
    # Read the data from the file using the provided filename
    with open(os.path.join(output_folder, "temp_first_entry",filename), 'r') as f:
        data = json.load(f)
    return render_template('next_screen.html', data=data)

@app.route('/submit_last_entry', methods=['POST'])
def submit_last_entry():
    if request.method == 'POST':
        data = request.get_json()
        # Process the received data as needed
        # Generate timestamp for the filename
        filename = f"output_last_{timestamp}.json"
        # Save the data to a file with the generated filename
        with open(os.path.join(output_folder, "temp_last_entry", filename), 'w') as f:
            json.dump(data, f)
        # Redirect the user to the next screen
        return redirect(url_for('result', filename=filename))
    else:
        # Handle other HTTP methods (optional)
        return jsonify({'error': 'Method Not Allowed'}), 405
    
@app.route('/result/<filename>')
def result(filename):
    # Read the data from the file using the provided filename
    with open(os.path.join(output_folder, "temp_last_entry",filename), 'r') as f:
        data = json.load(f)

    final_output = questions.process_data('questions_template.xlsx', os.path.join(output_folder, "temp_last_entry",filename))
    return render_template('result.html', data=final_output)




if __name__ == '__main__':
    app.run(debug=True)
