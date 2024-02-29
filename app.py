from flask import Flask, render_template, request
import random

# DB 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class RSP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_result = db.Column(db.String(100), nullable=False)
    computer_result = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


RSP_list = ['가위', '바위', '보']
record = {
    'win' : 0,
    'lose' : 0,
    'tie' : 0
}

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/RS')
def RS():
    user_index = int(request.args.get('user_index'))
    #print(user_index)
    user_answer = RSP_list[user_index]

    computer_index = random.randint(0, 2)
    computer_answer = RSP_list[computer_index]
    Cal_record(record)
    # print(user_answer+computer_answer)
    return render_template('RSP.html',data=rsp_result(user_answer,computer_answer),record=Cal_record(record))


def rsp_result(user_answer, computer_answer):
    if user_answer == computer_answer:
        rsp_db = RSP(user_result=user_answer, computer_result=computer_answer, result='무')
    elif (user_answer == '가위' and computer_answer == '보') or (user_answer == '바위' and computer_answer == '가위') or (user_answer == '보' and computer_answer == '바위'):
        rsp_db = RSP(user_result=user_answer, computer_result=computer_answer, result='승')
    else:
        rsp_db = RSP(user_result=user_answer, computer_result=computer_answer, result='패')
    db.session.add(rsp_db)
    db.session.commit()
    #print(RSP.query.all()[-1].user_result)
    return RSP.query.all()

def Cal_record(record):
    record['win']=len(RSP.query.filter_by(result='승').all())
    record['lose']=len(RSP.query.filter_by(result='패').all())
    record['tie']=len(RSP.query.filter_by(result='무').all())
    return record

if __name__ == '__main__':
    app.run()
