from news import get_task, get_request
try:
    import mysql.connector
except:
    pass


def check_user(email):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE login = '" + email + "'")
    result = cursor.fetchall()
    result = str(result)
    if len(result) <= 4:
        return False
    return True


def user_get_commits(email):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT commits FROM user_info WHERE email = '" + email + "'")
    result = cursor.fetchall()
    if len(str(result)) <= 7:
        return []
    result = (str(result)[3:len(str(result)) - 4]).split(',')
    ret = []
    for x in result:
        ret.append(int(x))
    return ret


def get_tasks(ids):
    result = []
    for x in ids:
        result.append(get_task(x))
    return result


def get_requests(ids):
    result = []
    for x in ids:
        result += get_request(int(x['id']))
    return result


def register_user(email, password, abilities, name, surname, bio):
    if check_user(email):
        return False
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO user (login, password) VALUES (" +
                   "'" + str(email) + "', " +
                   "'" + str(password) + "')")
    db.commit()
    cursor.execute("INSERT INTO user_info (email, abilities, name, surname, bio) VALUES (" +
                   "'" + str(email) + "', " +
                   "'" + str(abilities) + "', " +
                   "'" + str(name) + "', " +
                   "'" + str(surname) + "', " +
                   "'" + str(bio) + "')")
    db.commit()
    return True


def user_parse_name(email):
    result = email.split('@')
    return result[0]


def user_validate(email, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute('SELECT password FROM user WHERE login=\'' + email + '\'')
    result = cursor.fetchone()
    result = str(result)
    result = result[2:len(result) - 3]
    return password == result
