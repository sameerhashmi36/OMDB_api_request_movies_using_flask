from flask import Flask, session, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, requests
from requests.api import post

app = Flask(__name__)

app.secret_key = 'thisismysecretkey'


#       connect to MySQL Database

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


#       login function
#       Use postman to login using your username and password

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        users = cursor.fetchone()

        if users:
            session['loggedin'] = True
            session['u_id'] = users['u_id']
            session['username'] = users['username']
            msg = 'Logged in Successfully :)'
            return redirect(url_for('profile'))
        
        else:
            msg = 'Incorrect username/password!!!!'
    return msg


#       loggout function

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('u_id', None)
    session.pop('username', None)
    return "You are successfully Logged Out!!"


#       Register yourself by username and password in mysqldb

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
        users = cursor.fetchone()

        if users:
            msg = 'Account already exit'
        elif not re.match(r'^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$', username):
            msg = 'Username must contain one upper case character and number'
        elif not username or not password:
            msg = 'Please fill up the form!'
        else:
            cursor.execute('INSERT INTO users VALUES(NULL, % s, % s)', (username, password,))
            mysql.connection.commit()
            msg = 'You have successfully registered'
    elif request.method == 'POST':
        msg = 'Please fill up the form'
    return msg


#       add movies in your profile by searching from omdb api
#       Use your user_id and movie's title to add that movie

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    msg = ''
    if request.method == 'POST':
        text = request.form['title']
        user_id = request.form['user_id']
        url = "http://www.omdbapi.com/?apikey=127fa5e7&t="+text
        movies = requests.get(url).json()
        # print("--------", movies)
        # for i, t in enumerate(text):
            # with open(t+'.txt', 'w') as json_file:
                # json.dump(movies[i], json_file)
        
        title = movies['Title']
        year = movies['Year']
        actors = movies['Actors']
        awards = movies['Awards']
        box_office = movies['BoxOffice']
        country = movies['Country']  
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM movies_list WHERE movie_title = % s', (title, ))
        movie = cursor.fetchone()
        if movie:
            msg = 'Movie is already in list'
        else:
            cursor.execute('INSERT INTO movies_list(user_id, movie_title, year_released, actors, awards, box_office, country) VALUES(%s, %s, %s, %s, %s, %s, %s)', (user_id, title, year, actors, awards, box_office, country,))
            mysql.connection.commit()
            # print("00000000000000000",type(movies))
            msg = 'Movie has been successfully added'
            return movies
        return msg
    return msg


#       View your added movies through user_id

@app.route('/view', methods=['GET', 'POST'])
def view():
    if request.method == 'POST':
        user_id = request.form['user_id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM movies_list WHERE user_id = %s", (user_id, ))
        results = cursor.fetchall()
        # return dict(results)
        view_dict = {}
        for idx in range(len(results)):
            # print(view_dict)
            view_dict[idx] = results[idx]
            # return view_dict
        return view_dict


#       Delete movies from mysqldb
#       using title and user_id

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    msg = ''
    if request.method == 'POST':
        text = request.form['title']
        user_id = request.form['user_id']
        url = "http://www.omdbapi.com/?apikey=127fa5e7&t="+text
        movies = requests.get(url).json()
        title = movies['Title']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM movies_list')
        movie = cursor.fetchone()
        if movie:
            cursor.execute('DELETE FROM movies_list WHERE user_id = %s AND movie_title = %s', (user_id, title))
            mysql.connection.commit()
            msg = 'Movie has been successfully deleted'
        else:
            msg = 'Movie is not in list'
            return msg
        return msg
    return msg


#       run the app

if __name__ == '__main__':
    app.run(debug=True)

