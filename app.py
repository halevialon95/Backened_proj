from flask import Flask, redirect, url_for
from flask import render_template, request, session
app = Flask(__name__)
app.secret_key = '123'
users =  { 'user_1': {'user_name': 'Amir', 'email': 'amir82@gmail.com'},
              'user_2': {'user_name': 'Yael', 'email': 'yael2243@gmail.com'},
              'user_3': {'user_name': 'Alon', 'email': 'alon95@gmail.com'},
              'user_4': {'user_name': 'Yonatan', 'email': 'amir82@gmail.com'},
              'user_5': {'user_name': 'Daniel', 'email': 'Daniel82@gmail.com'}
             }

@app.route('/')
def home():
    return render_template('CV1.html')


@app.route('/contact_us_page')
def contact_us():
    return render_template('CV2.html')


@app.route('/Assignment8')
def assignment_8_page():
    first_name = 'Alon'
    last_name = 'Halevi'
    return render_template('assignment8.html',name=first_name,family_name=last_name,
            hobbies=('Cheering for phili76ers','Playing Basketball','Hearing Music'))



@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_page():
    # defining the search form
    if 'email' in request.args:
        email = request.args['email']
        if email == '':
            return render_template('assignment9.html', users=users)

#check if user's details match according to dictionary
        for key, value in users.items():
            if value.get('email') == email:
                return render_template('assignment9.html', user_name=value.get( 'name' ), email=value.get('email'))
    # defining reg form
    if request.method == "POST":
        #post method is needed because the user wants to insert info and not only get it
        session['user_name'] = request.form['username']
    return render_template('assignment9.html')

@app.route("/logout", methods=['GET', 'POST'])
#defining a timely session for each user
def logout_func():
    session['user_name']=''
    return render_template('assignment9.html')


#assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':

    app.run(debug=True)
