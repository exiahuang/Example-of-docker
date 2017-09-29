from flask import Flask, session, redirect, url_for, escape, request
from flask import abort, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

app.secret_key = '\x8c\x8e\xcdN%!\xda\xb4\x87\x92y&\xd3\xb2\x01\xce\xca\xd9\x1e[d&\xcf\xc0'

@app.route('/')
def index():
    username = ''
    if 'username' in session:
        username = escape(session['username'])

    redis.incr('hits')
    return 'Hello World! I have been seen %s times. %s' % (redis.get('hits'), username)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))









if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)