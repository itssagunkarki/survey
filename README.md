# Children's Behavior Questionnaire Analyzer

### Installation
- Clone the repository
  ```bash
  git clone <repo link>
  ```
- Install the requirements
  ```bash
  # create a virtual environment
    python3 -m venv .venv
  # activate the virtual environment
    source .venv/bin/activate
  # install the requirements
    pip install -r requirements.txt
    ```
- Run the app
    
    Be in the root of the project and run 
- ```bash
  python app.py
  ```

### Quesiton_template.xlsx is the file for the questionnaire template.
- Add/remove question in that template and it will update the program.
- first run the app using 
  ```bash
    # you may need to activate the virtual environment
    source .venv/bin/activate

    # run the app
    python app.py
    ```
- If you refresh the homepage it will clear the cache and you need to start from beginning.
- First enter data for all question in the homepage.
- Then click on the `next` button to go to the next page.
- Start entering the same data, if you click different button than what you had entered in previous button it will display `updated` before that question and show previously pressed button as grey button. 
  - You can change the button by clicking on the button again. 
- After entering all the data, click on the `Next` button to submit the data.
- It will display the result of the data entered and also save the data and result in the `output/results/` folder with the name of the file as `<timestamp>.xlsx`. 
  - The result file will have two sheets, one for the data entered and the other for the result. 

### Result calculation

The logic for the result calculation is implemented in the `questions.py` file.

