from flask import Flask, flash, request, render_template, redirect, session
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "SHHHHHHHHHHH"
responses = []
@app.route('/')
def home():
    survey = satisfaction_survey
    return render_template('home.html', survey=survey)

@app.route('/questions/<index>', methods=["GET","POST"] )
def getQuestion(index):
    session['answers'] = responses
    print(session['answers'])

    if request.method == "POST":
        responses.append(request.form['answer'])
        
        if int(index) >= len(satisfaction_survey.questions):
            return redirect('/completed')
        else:
            return redirect(f'/questions/{int(index)+1}')
    else:
        if len(responses) != int(index)-1:
            responses.clear()
            return redirect('/questions/1')
        else:
            question = satisfaction_survey.questions[int(index)-1]
    
            content = {'index':int(index), 'question':question}
            return render_template('question.html', content=content)
                                                                                                                                                                                                                                                                                
@app.route('/completed')
def completed():
    print(responses) 
    return render_template('thanks.html')


if __name__  == "__main__":
    app.run(debug=True)