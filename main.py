from flask import Flask
from flask import render_template
from flask import Response, request, redirect, url_for, jsonify

app = Flask(__name__)

quiz_questions = {
    "1": {
        "quiz_id": "1",
        "question":
        "in formal table setting, where is the bread plate located?",
        "options": {
            "a": "to the right of the charger",
            "b": "directly above the charger",
            "c": "to the top left of the charger",
            "d": "below the charger"
        },
        "correct_answer": "c",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "question":
        "drag and drop the items to practice setting casual table.",
        "next_question": "end"
    }
}

# ROUTES


@app.route('/')
def home():
  return render_template('home.html')


@app.route('/learn/basic')
def basic():
  return render_template('basic.html')


@app.route('/learn/casual')
def casual():
  return render_template('casual.html')


@app.route('/learn/formal')
def formal():
  return render_template('formal.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
  if request.method == 'POST':
    user_answer = request.form.get(
        'quiz_option').upper()  # Get the option selected by the user
    correct_answer = quiz_questions["1"]["correct_answer"].upper()
    return render_template('feedback.html',
                           user_answer=user_answer,
                           correct_answer=correct_answer)
  else:
    question = quiz_questions["1"]["question"]
    options = quiz_questions["1"]["options"]
    return render_template('quiz.html', question=question, options=options)


if __name__ == '__main__':
  app.run(debug=True)
