import pandas as pd


def get_questions(file_path, sheet_name):
    df_questions = pd.read_excel(file_path, sheet_name=sheet_name)
    questions_dict = {}
    
    for i, j in df_questions[['cbq_num', 'cbq_q']].iterrows():
        questions_dict[j['cbq_num']] = {
            "question_prompt": j['cbq_q'],
            "first_entry": 0,
            "last_entry": 0,
            "cba_a": 0, # cba_a this is the final response that will be updated when both first and last entry match.
            }
    
    return questions_dict