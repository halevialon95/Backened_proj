from flask import redirect, render_template
from flask import Blueprint,request
from my_db import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10',
                         template_folder='templates')

message = ""

@assignment10.route("/assignment10", methods=['GET', 'POST'])
def assignment10():
    global message

    message = ""
    return render_template('assignment10.html')



@assignment10.route('/insert_user', methods=['POST'])
def create_user():
    name = request.form['NAME']
    email = request.form['EMAIL']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s')" % (name, email)
    interact_db(query=query, query_type='commit')
    global message
    message = name + " was created!"
    return redirect('/list')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user():
    name = request.form['NAME']
    query = "DELETE FROM users WHERE name='%s'" % name
    interact_db(query, query_type='commit')

    global message
    message = name + " - User has been deleted"

    return redirect('/list')


@assignment10.route('/update_user', methods=['POST'])
def update_user():
    name = request.form['NAME']
    new_email = request.form['NEW_MAIL']
    query = "update users set email = '%s' where name = '%s'" % (new_email, name)
    interact_db(query=query, query_type='commit')

    global message
    message = name + "user updated successfully"

    return redirect('/list')



@assignment10.route('/list')
def users_list():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')

    return render_template('assignment10.html', list=query_result, message=message)
