# coding: utf-8
try:
    import mysql.connector
except:
	print("Mysql error")

DATA_FILE = 'news.data'
DATA_ENCODING = 'utf-8'


def user_get(email):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT name FROM user_info WHERE email = '" + email + "'")
    result = cursor.fetchone()
    result = str(result)
    result = result[2:len(result)-3]
    cursor.execute("SELECT abilities FROM user_info WHERE email = '" + email + "'")
    result1 = cursor.fetchone()
    result1 = str(result1)
    result1 = result1[2:len(result1)-3]
    cursor.execute("SELECT finished_tasks FROM user_info WHERE email = '" + email + "'")
    result2 = cursor.fetchone()
    result2 = str(result2)
    result2 = result2[1:len(result2)-2]
    cursor.execute("SELECT created_tasks FROM user_info WHERE email = '" + email + "'")
    result3 = cursor.fetchone()
    result3 = str(result3)
    result3 = result3[1:len(result3)-2]
    cursor.execute("SELECT id FROM user WHERE login = '" + email + "'")
    id = cursor.fetchone()[0]
    return {
        "name": result,
        "abilities": result1,
        "finished_tasks": result2,
        "created_tasks": result3,
        "taked_tasks": user_get_tasks_count(email),
        "id": id
    }


def get_user_with_id(id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT name FROM user_info WHERE id = '" + id + "'")
    result = cursor.fetchone()[0]
    return result


def user_get_tasks_count(email):
    to_parse = user_get_tasks(email)
    if to_parse[0] == '':
        return 0
    return len(to_parse)


def user_get_tasks(email):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT taked_tasks FROM user_info WHERE email = '" + email + "'")
    result = cursor.fetchall()
    result = str(result)
    result = result[3:len(result) - 4]
    if len(result) == 0:
        return []
    ret = result.split(',')
    i = int(0)
    for x in ret:
        ret[i] = int(x)
        i += 1
    return ret


def load_news_():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="worker"
        )
        cursor = db.cursor()
        ret = []
        cursor.execute('SELECT id FROM task')
        result = cursor.fetchall()
        for x in result:
            x = str(x)[1:len(str(x)) - 2]
            cursor.execute('SELECT name, desciption, const FROM task WHERE id=' + x)
            get = cursor.fetchone()
            ret.append({"name": get[0],
                        "description": get[1],
                        "cost": get[2],
                        "id": x})
        ret.reverse()
        return ret
    except:
        try:
            with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
                return eval(data_file.read())
        except BaseException:
            return []


def save_news():
    if not changed:
        return
    with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr(news_), file=data_file)


def generate_dewey(bid):
    ret = []
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    id = int
    need = False
    try:
        id = bid[0]
        need = True
    except:
        id = bid
    cursor.execute("SELECT name FROM task WHERE id = " + str(id))
    c_name = cursor.fetchone()[0]
    cursor.execute("SELECT child FROM task WHERE id = " + str(id))
    result = cursor.fetchone()[0]
    if need:
        ret.append({
            "name": c_name,
            "prevname": ''
        })
    try:
        result = result.split(',')
        for x in result:
            x = int(x)
            cursor.execute("SELECT name FROM task WHERE id = " + str(x))
            name = cursor.fetchone()[0]
            ret.append({
                "name": name,
                "prevname": c_name
            })
            ret += generate_dewey(x)
    except:
        pass
    return ret


news_ = load_news_()
changed = False


def get_news():
    return news_


def get_len():
    return len(news_)


def get_task(task_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task WHERE id = '" + str(task_id) + "'")
    result = cursor.fetchall()[0]
    return {
        "id": result[0],
        "name": result[1],
        "description": result[2],
        "category": result[3],
        "cost": result[4],
        "deadline": result[5],
        "owner": result[6]
    }


def get_request(task_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT requests FROM task WHERE id = '" + str(task_id) + "'")
    result = cursor.fetchall()[0]
    if len(str(result)) <= 5:
        return None
    ret = []
    for x in result:
        try:
            ret.append({
                "user_name": get_user_with_id(x),
                "task_name": get_task(task_id)['name']
            })
        except:
            pass
    return ret


def add_parent(ind, to_add):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    cursor.execute("SELECT child FROM task WHERE id = " + str(ind))
    result = cursor.fetchone()[0]
    if result is None:
        result = ''
    else:
        result = str(result) + ','
    cursor.execute("UPDATE task SET child = '" + str(result) + str(to_add) + "' WHERE id = " + str(ind))
    db.commit()
    return result


def add_new(name, description, deadline_date, category, cost, owner, parent):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootUser@1234",
        database="worker"
    )
    cursor = db.cursor()
    if parent == 'Нету родительской задачи':
        cursor.execute("INSERT INTO task (name, desciption, deadline, category, const, owner) VALUES (" +
                       "'" + str(name) + "', " +
                       "'" + str(description) + "', " +
                       "'" + str(deadline_date) + "', " +
                       "'" + str(category) + "', " +
                       "'" + str(cost) + "', " +
                       "'" + str(owner) + "')")
        cursor.execute("SELECT id FROM task WHERE name = '" + name + "'")
        to_add = cursor.fetchone()[0]
        db.commit()
    else:
        cursor.execute("SELECT id FROM task WHERE name = '" + parent + "'")
        parent = cursor.fetchone()[0]
        cursor.execute("INSERT INTO task (name, desciption, deadline, category, const, owner, parent) VALUES (" +
                       "'" + str(name) + "', " +
                       "'" + str(description) + "', " +
                       "'" + str(deadline_date) + "', " +
                       "'" + str(category) + "', " +
                       "'" + str(cost) + "', " +
                       "'" + str(owner) + "', " +
                       "'" + str(parent) + "')")
        cursor.execute("SELECT id FROM task WHERE name = '" + name + "'")
        to_add = cursor.fetchone()[0]
        db.commit()
        add_parent(parent, to_add)
    cursor.execute("SELECT commits FROM user_info WHERE email = '" + owner + "'")
    result = cursor.fetchone()[0]
    if result is None:
        result = ''
    else:
        result = str(result) + ','
    news_.reverse()
    news_.append({"name": name,
                  "description": description,
                  "cost": cost,
                  "id": to_add
                  })
    news_.reverse()
    cursor.execute("UPDATE user_info SET commits = '" + str(result) + str(to_add) + "' WHERE email = '" + owner + "'")
    db.commit()
