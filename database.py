import json

FILE = "data/users.json"

def load_users():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def save_city(user_id, city):
    users = load_users()
    users[str(user_id)] = city
    save_users(users)

def get_city(user_id):
    users = load_users()
    return users.get(str(user_id))