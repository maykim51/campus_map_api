from werkzeug.security import safe_str_cmp
from resources.user import User, UserList

def authenticate(username, password):
    user = UserList.get_username_mapping().get(username, None)
    if user and safe_str_cmp(password, user.password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserList.get_userid_mapping().get(user_id, None)


if __name__ == "__main__":
    print(UserList.get_userid_mapping())
    print(UserList.get_username_mapping()) 