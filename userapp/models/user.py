class UserModel(object):
    user = {
        1: {'name': 'zhang', 'age': 18},
        2: {'name': 'wang', 'age': 19},
        3: {'name': 'li', 'age': 20},
        4: {'name': 'zhao', 'age': 21},
    }

    @classmethod
    def get(cls, user_id):
        return cls.user[user_id]

    @classmethod
    def get_all(cls):
        return list(cls.user.values())

    @classmethod
    def create(cls, name, age):
        user_dict = {'name' : name, 'age' : age}
        max_id = max(cls.user.keys()) + 1
        cls.user[max_id] = user_dict

    @classmethod
    def update(cls, user_id, age):
        cls.user[user_id]['age'] = age

    @classmethod
    def delete(cls, user_id):
        if user_id in cls.user:
            return cls.user.pop(user_id)

