from flask import Flask, redirect, render_template, url_for, request, redirect, jsonify
import pandas as pd
import os

app = Flask(__name__)


# Current directory for Flask app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(APP_ROOT, 'word_data_created.csv')
df = pd.read_csv(file_path)

# main solver function
def wordle_solver_split(import_df, must_not_be_present: str, 
    present1: str, present2: str, present3: str, present4: str, present5: str,
    not_present1: str, not_present2: str, not_present3: str, not_present4: str, not_present5: str):

    must_not_be_present = must_not_be_present.lower()
    present1 = present1.lower()
    present2 = present2.lower()
    present3 = present3.lower()
    present4 = present4.lower()
    present5 = present5.lower()
    not_present1 = not_present1.lower()
    not_present2 = not_present2.lower()
    not_present3 = not_present3.lower()
    not_present4 = not_present4.lower()
    not_present5 = not_present5.lower()

    final_out2 = must_not_be_present + present1 + present2 + present3 + present4 + present5 + \
        not_present1 + not_present2 + not_present3 + not_present4 + not_present5

    # split individual letters into lists
    must_not_be_present = list(must_not_be_present)
    present = [present1, present2, present3, present4, present5]
    not_present = [not_present1, not_present2, not_present3, not_present4, not_present5]
    must_be_present = (''.join(not_present))

    places = ['one', 'two', 'three', 'four', 'five']
    # df = pd.read_excel(import_df)
    df = import_df.copy()
    total_len = len(df)

    # process the 'must be present' letters
    for j in must_be_present:
        drop_list = []
        for i in range(len(df)):
            drop_list.append(df['word'][i].find(j))
        df['drop_no_' + j] = drop_list
    for j in must_be_present:
        df = df[df['drop_no_' + j] != -1]

    # process the 'must not be present' letters
    for i in places:
        for j in must_not_be_present:
            df = df[df[i] != j]

    # process the 'specific values must be present' letters
    for i, v in enumerate(places):
        if present[i] != '':
            df = df[df[v] == present[i]]

    # process the 'specific values not must be present' letters
    for j, k in enumerate(places):
        if len(not_present[j]) > 0:
            for i in not_present[j]:
                df = df[df[k] != (','.join(i))]

    # pick the best (aka reasonably good) choice by sorting on the highest 'word_score'
    df = df.sort_values(by = 'word_score', ascending =  False)

    try:
        final_out1 = 'Pick 1: ' + df.iat[0, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out1 = 'No words found'
    try:
        final_out2 = 'Pick 2: ' + df.iat[1, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out2 = ''
    try:
        final_out3 = 'Pick 3: ' + df.iat[2, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out3 = ''
    try:
        final_out4 = 'Pick 4: ' + df.iat[3, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out4 = ''
    try:
        final_out5 = 'Pick 5: ' + df.iat[4, 0] # print top 5 in case you get trapped in a narrow path of replacing just 1 letter at a time
    except:
        final_out5 = ''
    final_out_end = f'Options remaining: {len(df)}/{total_len} ({round(len(df)/total_len*100,2)}%)'

    return final_out1, final_out2, final_out3, final_out4, final_out5, final_out_end

def find_word_with_letters(import_df, must_be_present: str):

    must_be_present = must_be_present.lower()

    df = import_df.copy()

    count_list = []
    for i in range(len(df)):
        counting = 0
        for j in must_be_present:
            if df['word'][i].find(j) == -1:
                counting += 0
            else:
                counting += 1
        count_list.append(counting)
            
    df['char_match_count'] = count_list

    df = df.sort_values(by = ['char_match_count', 'word_score'], ascending =  False)
    df = df[['word', 'char_match_count']]

    try:
        final_out1 = f"Pick 1: {df.iat[0, 0]} ({df['char_match_count'].iloc[0]} match)"
    except:
        final_out1 = 'No words found'
    try:
        final_out2 = f"Pick 2: {df.iat[1, 0]} ({df['char_match_count'].iloc[1]} match)"
    except:
        final_out2 = ''
    try:
        final_out3 = f"Pick 3: {df.iat[2, 0]} ({df['char_match_count'].iloc[2]} match)"
    except:
        final_out3 = ''
    try:
        final_out4 = f"Pick 4: {df.iat[3, 0]} ({df['char_match_count'].iloc[3]} match)"
    except:
        final_out4 = ''
    try:
        final_out5 = f"Pick 5: {df.iat[4, 0]} ({df['char_match_count'].iloc[4]} match)"
    except:
        final_out5 = ''

    return final_out1, final_out2, final_out3, final_out4, final_out5


@app.route("/", methods=["POST", "GET"])
def run_wordle():
    if request.method == "POST":
        must_not_be_present = request.form["must_not_be_present"]
        present1 = request.form["present1"]
        present2 = request.form["present2"]
        present3 = request.form["present3"]
        present4 = request.form["present4"]
        present5 = request.form["present5"]
        not_present1 = request.form["not_present1"]
        not_present2 = request.form["not_present2"]
        not_present3 = request.form["not_present3"]
        not_present4 = request.form["not_present4"]
        not_present5 = request.form["not_present5"]
        final_out1, final_out2, final_out3, final_out4, final_out5, final_out_end = wordle_solver_split(df, must_not_be_present, \
            present1, present2, present3, present4, present5, not_present1, not_present2, not_present3, not_present4, not_present5)
        return render_template("index.html", final_out1=final_out1, final_out2=final_out2, final_out3=final_out3, final_out4=final_out4, final_out5=final_out5, final_out_end=final_out_end, \
            must_not_be_present_val=must_not_be_present, present1_val=present1, present2_val=present2, present3_val=present3, present4_val=present4, present5_val=present5, \
            not_present1_val=not_present1, not_present2_val=not_present2, not_present3_val=not_present3, not_present4_val=not_present4, not_present5_val=not_present5)
    else:
        return render_template("index.html")

@app.route("/fixer", methods=["POST", "GET"])
def run_wordle_fixer():
    if request.method == "POST":
        must_be_present = request.form["must_be_present"]
        final_out1, final_out2, final_out3, final_out4, final_out5 = find_word_with_letters(df, must_be_present)
        return render_template("fixer.html", final_out1=final_out1, final_out2=final_out2, final_out3=final_out3, final_out4=final_out4, final_out5=final_out5, must_be_present=must_be_present)
    else:
        return render_template("fixer.html")




if __name__ == "__main__":
    app.run(debug=True)