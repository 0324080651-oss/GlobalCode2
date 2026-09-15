from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return{'message': 'Hello, World!',
           'message': "This is a simple Flask application."
    }

@app.route('/about')
def about():
    return  '<h1>About</h1><p>This is a simple Flask application </p>'

# @app.route('/whereami/<name>')
# def whereami(name):
#     return f'Hello {name}, you are in Ho Ghana'


@app.route('/greet/<name>')
def greet(name):
    return render_template('main.html', user_name=name, fruits=['apple','banana','orange'] ,is_admin=False)

@app.route('/index/<name>', methods=['GET', 'POST'])
def index(name):
    if request.method == 'POST':
        return f'Hello {name}, you submitted a POST request!'
    elif request.method == 'GET':
        return f'Hello {name}, you submitted a GET request!'
    else:
        return f'Hello {name}, you submitted a {request.method} request!'
    


@app.route('/greet')
def greet2():
    return render_template ('main.html')




@app.route('/contact')
def contact():
    return 'contact me'


if __name__ == '__main__':
    app.run(debug= True)


