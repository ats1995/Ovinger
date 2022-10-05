class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something_cool(self):
        print("Sign up to Lightrun " + self._namee)

    def __str__(self):
        return self._name + " , " + self._email

    users = [User("Lightrun Demo", "help@lightrun.com"),
        User("Debugger", "debugger@debugger.com")]

    for user in users:
        user.do_something_cool()