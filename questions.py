import pandas as pd
import json


def get_questions(file_path, sheet_name):
    '''
    Read all the questions from the excel file and return a dictionary of questions and variables to store first and last entry
    '''
    df_questions = pd.read_excel(file_path, sheet_name=sheet_name)
    questions_dict = {}
    
    for i, j in df_questions[['cbq_num', 'cbq_q']].iterrows():
        questions_dict[j['cbq_num']] = {
            "question_prompt": j['cbq_q'],
            "first_entry": 0,
            "last_entry": 0,
            }
    
    return questions_dict

def clean_entered_data(template_path, data_path):
    """
    Some questions, may need reverse scoring, there is a column in the template that indicates if the question needs to be reversed or not
    """
    data= json.loads(open(data_path).read())
    df_x = pd.DataFrame.from_dict(data['questionsCopy']).T.reset_index().rename(columns={'index':'cbq_num'})
    df_x['cbq_num'] = df_x['cbq_num'].astype(int)
    df_x['last_entry'] = df_x['last_entry'].astype(int)
    df_questions = pd.read_excel(template_path, sheet_name='questions')
    df_combined = pd.merge(df_x, df_questions, on='cbq_num')
    
    return df_combined

def reverse_score(df_combined):
    """
    For some questions if the score = 1 then it should be 7 and so on
    """
    ans = list(range(1, 8))
    rev_ans = list(range(7, 0, -1))


    rev_ans_dct = {x:y for x, y in zip(ans, rev_ans)}
    rev_ans_dct[0] = 0

    # separate the "R" type and non R questions
    df_rev = df_combined[df_combined['reverse'] == "R"].copy()
    df_normal = df_combined[df_combined['reverse'] != "R"].copy()

    #Map the reversed score using precomputed dict of "prev_score" = "new_score"
    df_rev['last_entry'] = df_rev['last_entry'].map(rev_ans_dct)

    # map all the -1 entries to 0, we want the count of NA not the value of NA
    df_normal['last_entry'] = df_normal['last_entry'].apply(lambda x: None if x == -1 else x)

    #combine both dict
    df_final = pd.concat([df_normal, df_rev])

    return df_final


def save_data_as_sheet(data, result, file_path):
    data = data.sort_values(by='cbq_num')
    df_result = pd.DataFrame.from_dict(result, orient='index')
    # save result as a sheet
    with pd.ExcelWriter(file_path) as writer:
        data.to_excel(writer, sheet_name="questions", index=False)
        df_result.to_excel(writer, sheet_name="result", index=True)


def process_data(template_path, data_path, timestamp):
    df_combined = clean_entered_data(template_path, data_path)
    df_final = reverse_score(df_combined)

    result_dct = {}

    #Group by CBQ SCALE ASSIGNMENTS
    for i, j in df_final.groupby(['cbq_scale_cat']):
        res = {}
        
        # Since for N/A and does not apply, we left data blank, those values are 0
        # we can sum all the values of the column to get the sum for that type
        res['sum_ans'] = j['last_entry'].sum()

        # Based on Number 2 condition on scoring chart,
        # we can count the total number of valid responses
        j_filtered = j[j['last_entry'] != 0].copy()

        res['num_ans'] = j_filtered['last_entry'].shape[0]

        result_dct[i[0]] = res

    # Calculate the average score for each group of questions
    for i in result_dct:
        result_dct[i]['mean_score'] = round(result_dct[i]['sum_ans'] / result_dct[i]['num_ans'], 3)

    save_data_as_sheet(df_final, result_dct, f'output/results/{timestamp}.xlsx')

    return result_dct