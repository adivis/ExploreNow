from flask import Flask, request, render_template, redirect, session
import mysql.connector
import os

app = Flask(__name__)
# app.secret_key = os.urandom(24)
# conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="users")
# cursor = conn.cursor()


# @app.route("/")
# def login():
#     return render_template('login.html')
#

@app.route("/")
def home():
    return render_template("index.html")
    # if 'sno' in session:
    #     return render_template("index.html")
    # else:
    #     return render_template("login.html")


# @app.route("/register")
# def register():
#     return render_template("register.html")


# @app.route("/logout")
# def logout():
#     session.pop('sno')
#     return redirect('/')


# @app.route("/login_validation", methods=['POST'])
# def login_validation():
#     email = request.form.get("email")
#     password = request.form.get("password")
#     cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
#                    .format(email, password))
#     users = cursor.fetchall()
#     if len(users) > 0:
#         session['sno'] = users[0][0]
#         return redirect('/home')
#     else:
#         return redirect('/')
#

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form.get('uname')
#     email = request.form.get('uemail')
#     password = request.form.get('upassword')
#
#     cursor.execute("""INSERT INTO `users` (`sno`,`name`,`email`,`password`) VALUES
#     (NULL,'{}','{}','{}')""".format(name, email, password))
#     conn.commit()
#     cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
#     myuser = cursor.fetchall()
#     session['sno'] = myuser[0][0]
#     return redirect('/home')
#

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/field")
def field():
    return render_template('field.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/technologies")
def technologies():
    return render_template('technology.html')



@app.route("/web-resources")
def webresources():
    return render_template('webresources.html')


@app.route("/business")
def business():
    return render_template('business.html')



@app.route("/industry-trends")
def trends():
    return render_template('trends.html')


@app.route("/law")
def law():
    return render_template('law.html')


@app.route("/commerce")
def commerce():
    return render_template('commerce.html')


@app.route("/medicine")
def medicine():
    return render_template('medicine.html')


@app.route("/arts")
def arts():
    return render_template('arts.html')


@app.route("/website-development")
def webdev():
    return render_template('webdev.html')


@app.route("/management")
def management():
    return render_template('management.html')


@app.route("/general")
def general():
    return render_template('general.html')


app.run(debug=True)
