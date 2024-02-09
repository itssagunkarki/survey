# Children's Behavior Questionnaire Analyzer

This is a Python Flask app that assesses the answers to CBQ. 

### How it Works
Not to make this too complicated with databases and such, it uses an excel file to store the data.

- The excel file is located in root of the project and is named `questions_template.xlsx`.
  - It has 4 sheets: `questions`, `details`, `abbrevations` and `results`.
- It creates a copy of `questions_template.xlsx` and names it `<timestamp>.xlsx`.
  - First it shows a webpage with the questions from that copy and asks the user to fill in the answers, by clicking option button `1-7 and N/A` for each question.
  - On the bottom of the page there is a `Next` button.
  -  When clicked, it then saves the data to the copy of the excel file i.e. `<timestamp>.xlsx` and marks it filled once in the `details` sheet.
  -  It again asks you to fill all the details again. This time there is a `update` button in each question. If you press different button then the previous one, it will show your previous answer in blue button, and new answer in orange color. and it will enable the `update` button. If you press the `update` button, it will note that answer. and when you finally press the `Next` button, it will save the data to the excel file with results calculated. 

- I have highlighted cells in the excel file that should not be modified.
  - If I have highlighted many cells in a row, you cannot add additional columns to that excel sheet. and same goes for columns, if I have highlighted many cells in a column, you cannot add additional rows to that excel sheet.
    - You can add things if you wish, but you need to modify the code to handle the new data.
- The `results` sheet has some default output categories listed, `do not add` or as it will be overwritten.
  
#### What you can do without modifying the code
- Add or remove or change question categories, numbers in the `question_template.xlsx` file. and the code will be able to produce the result accordingly.

### Installation
- Clone the repository
  ```bash
  git clone 
  ```
- Install the requirements
  ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
- Run the app
    
    Be in the root of the project and run 
- ```bash
  python app.py
  ```

