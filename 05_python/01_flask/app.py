from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
   #return 'Hello World!'
    return render_template('index.html')

@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY'


@app.route('/dday')
def dday():
    today = datetime.now()
    end = datetime(2020, 8, 8)
    td = end -today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>this is hteml h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    """
    <h1>여러줄을 보내 봅시다.</h1>
    <ul>
        <li>1</li>
        <li>2</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    #return f'반갑습니다! {name}님'
    return render_template('greeting.html', html_name=name)

##<>STRING이 기본값
@app.route('/cube/<int:number>')
def cube(number):
    #return f'{number}의 세 개의 곱{number**3}' 
    result = number**3
    return render_template("cube.html", result =result, number = number)

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밥','마파두부','초코우유', '솜사탕', '계란볶음밥','삼겹살', '맥주']
    order = random.sample(menu, people)
    return str(order)


@app.route('/movie')
def movie():
    movies = ['겨울왕국', '미니게임', '포드vs페라리', '슈퍼맨','미니언즈']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html = age)

@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/google')
def google():
 
    return render_template('google.html')


@app.route('/isitbirthday')
def isitbirthday():
    today = datetime.now()
    if today.month == 8 and today.day == 8:
        result = True
    else:
        result = False        
    return render_template('isitbirthday.html', result =result)


@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmade')
def godmade():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '어중간'] 
    
       
if __name__=='__main__':
    app.run(debug=True)