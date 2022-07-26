import json, time

LOG_PATH = 'static/data/server_log.json'
CHAT_PATH = 'static/data/chat.json'
TIMEFORMAT = '%Y-%m-%d, %H:%M:%S'


# log = {'username': '', 'msg': '', 'time': ''}
def write(type, username, msg):
    if type == 'log':
        path = '/Users/yui/PycharmProjects/flaskSocketTest/static/data/server_log.json'
    elif type == 'chat':
        path = '/Users/yui/PycharmProjects/flaskSocketTest/static/data/chat.json'
    log = {
        'username': username,
        'msg': msg,
        'time': time.strftime(TIMEFORMAT)
    }
    try:
        with open(path, 'r') as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        with open(path, 'w') as f:
            json.dump([], f)
    data.append(log)
    with open(path, 'w') as f:
        json.dump(data, f)

def read():
    try:
        with open(LOG_PATH, 'r') as f:
            data = json.load(f)
            return data
    except json.decoder.JSONDecodeError:
        with open(LOG_PATH, 'w') as f:
            json.dump([], f)
        return []

