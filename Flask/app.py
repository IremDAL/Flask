from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def insert_score(name, score):
    conn = get_db_connection()
    conn.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()

def get_personal_high_score(name):
    conn = get_db_connection()
    row = conn.execute('SELECT MAX(score) as max_score FROM scores WHERE name = ?', (name,)).fetchone()
    conn.close()
    return row['max_score'] if row['max_score'] is not None else 0

def get_global_high_score():
    conn = get_db_connection()
    row = conn.execute('SELECT MAX(score) as max_score FROM scores').fetchone()
    conn.close()
    return row['max_score'] if row['max_score'] is not None else 0

@app.route('/')
def quiz():
    name = request.args.get("name", "")
    personal_high = get_personal_high_score(name) if name else 0
    global_high = get_global_high_score()

    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()
    conn.close()

    return render_template('quiz.html', questions=questions, personal=personal_high, global_high=global_high, name=name)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('username', 'Anonim')
    conn = get_db_connection()
    questions = conn.execute('SELECT * FROM questions').fetchall()

    score = 0
    total = len(questions)
    for question in questions:
        user_answer = request.form.get(str(question['id']))
        if user_answer == question['correct_option']:
            score += 1

    percentage = int((score / total) * 100)
    insert_score(name, percentage)

    personal_high = get_personal_high_score(name)
    global_high = get_global_high_score()

    conn.close()

    return render_template('result.html', score=percentage, personal=personal_high, global_high=global_high, name=name)


if __name__ == '__main__':
    app.run(debug=True)