from flask import Flask, render_template, session, redirect
import flask
from news import save_news, get_news, get_len, get_task, add_new, generate_dewey, user_get, user_get_tasks
from user import register_user, user_validate, get_tasks, user_get_commits, get_requests
try:
    import mysql.connector
except:
    pass

app = Flask(__name__)
app.secret_key = '123'


def check_login():
    if not ('logined' in session) or session['logined'] == False:
        return redirect('/')
    return None

@app.route('/')
def home():
    if not ('logined' in session) or session['logined'] == False:
        return render_template('login.html',
                               page_title="Авторизация")
    if not ('user_name' in session):
        session['user_name'] = 'admin'
    try:
        user = user_get(session['email'])
    except:
        user = {"name": "admin",
                "abilities": "JavaScript, PHP, Java, Python, Ruby, Java, Node.js, etc.",
                "finished_tasks": 13,
                "created_tasks": 37}
    return render_template('index.html',
                           page_title="Лента",
                           user=user,
                           news=get_news(),
                           count=get_len())


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def not_found(path):
    ans = check_login()
    if ans:
        return ans
    return render_template('404.html',
                           page_title="Ошибка 404",
                           user={"name": session['user_name']})


@app.route('/create_task', methods=["GET", "POST"])
def create_task():
    ans = check_login()
    if ans:
        return ans
    if flask.request.method == 'GET':
        if not ('user_name' in session):
            session['user_name'] = 'admin'
        try:
            user = user_get(session['email'])
        except:
            user = {"name": "admin",
                    "abilities": "JavaScript, PHP, Java, Python, Ruby, Java, Node.js, etc.",
                    "finished_tasks": 13,
                    "created_tasks": 37}
        return render_template('create_task.html',
                               page_title="Создать задание",
                               user=user,
                               taked_tasks=get_tasks(user_get_tasks(session['email'])))
    name = flask.request.form['name']
    description = flask.request.form['description']
    deadline_date = flask.request.form['deadline_date']
    category = flask.request.form['category']
    cost = flask.request.form['cost']
    owner = session['email']
    parent = flask.request.form['parent']
    add_new(name, description, deadline_date, category, cost, owner, parent)
    return redirect('/create_task')


@app.route('/task_list')
def task_list():
    ans = check_login()
    if ans:
        return ans
    return render_template('task_list.html',
                           page_title="Список заданий",
                           user={"name": session['user_name']},
                           news=get_news(),
                           count=get_len())


@app.route('/current_list')
def current_list():
    ans = check_login()
    if ans:
        return ans
    return render_template('current_list.html',
                           page_title="Текущие задания",
                           user={"name": session['user_name']},
                           tasks=get_tasks(user_get_tasks(session['email'])),
                           dewey=generate_dewey(user_get_tasks(session['email'])))


@app.route('/profile')
def profile():
    ans = check_login()
    if ans:
        return ans
    return render_template('profile.html',
                           page_title="Профиль",
                           user={"name": session['user_name']})


@app.route('/statistics')
def statistics():
    ans = check_login()
    if ans:
        return ans
    try:
        user = user_get(session['email'])
    except:
        user = {"name": "admin",
                "abilities": "JavaScript, PHP, Java, Python, Ruby, Java, Node.js, etc.",
                "finished_tasks": 13,
                "created_tasks": 37,
                "taked_tasks": 37}
    return render_template('statistics.html',
                           page_title="Статистика",
                           user=user)


@app.route('/requests')
def events():
    ans = check_login()
    if ans:
        return ans
    return render_template('requests.html',
                           page_title="Запросы",
                           user={"name": session['user_name']},
                           users=get_requests(get_tasks(user_get_commits(session['email']))))


@app.route('/task/<task_id>')
def task(task_id):
    ans = check_login()
    if ans:
        return ans
    task_id = int(task_id)
    return render_template('task.html',
                           page_title="Задание #" + str(task_id),
                           user={"name": session['user_name']},
                           task=get_task(task_id))


@app.route('/registration', methods=["POST", "GET"])
def registration():
    ans = check_login()
    if ans:
        return ans
    if flask.request.method == "POST":
        email = flask.request.form['email']
        password = flask.request.form['pwd']
        abilities = flask.request.form['abilities']
        name = flask.request.form['name']
        surname = flask.request.form['surname']
        bio = flask.request.form['bio']
        if register_user(email, password, abilities, name, surname, bio) is True:
            session['logined'] = True
            session['email'] = email
            return redirect('/')
    return render_template('registration.html',
                           page_title="Регистрация")


@app.route('/login', methods=["POST"])
def login():
    ans = check_login()
    if ans:
        return ans
    if flask.request.form['submit'] == 'sign_up':
        return redirect("/registration")
    elif flask.request.form['submit'] == 'sign_up':
        return redirect("/123")
    email = flask.request.form['login']
    password = flask.request.form['pwd']
    try:
        if user_validate(email, password):
            session['logined'] = True
            session['email'] = email
    except:
        if email == "admin@admin.admin" and password == "1234":
            session['logined'] = True
            session['email'] = email
    return redirect('/')


@app.route('/request/<task_id>')
def request(task_id):
    ans = check_login()
    if ans:
        return ans
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootUser@1234",
            database="worker"
        )
        cursor = db.cursor()
        cursor.execute("SELECT requests FROM task WHERE id = " + str(task_id))
        result = cursor.fetchone()[0]
        if result is None or result == '':
            result = ''
        else:
            result = str(result) + ','
        cursor.execute("UPDATE task SET requests='" +
                       result +
                       str(user_get(session['email'])['id']) +
                       "' WHERE id = " + str(task_id))
        db.commit()
    except:
        pass
    return redirect('/task_list')


@app.route('/logout')
def logout():
    session['logined'] = False
    return redirect('/')


if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        save_news()
