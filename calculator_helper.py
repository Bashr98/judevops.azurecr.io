import logger

class CalculatorHelper():
    log_properties = {
        'custom_dimensions': {
            'userId': 'Bashar'
        }
    }

    _instance = None
    _is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculatorHelper, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._user_list = []
            self._current_user = None
            admin = self.User('Bashar','test123499999')
            self._user_list.append(admin)
            self._is_initialized = True
            self.logger = logger.get_logger(__name__)

    class User():
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def __repr__(self):
            return f"User(username={self.username}, password={self.password})"

    def add(self, a, b):
        self.logger.debug(f"Addingme {a} + {b}", extra=self.log_properties)
        return a + b

    def subtract(self, a, b):
        self.logger.debug(f"sub {a} - {b}", extra=self.log_properties)
        return a - b

    def multiply(self, a, b):
        self.logger.debug(f"multiply {a} * {b}", extra=self.log_properties)
        return a * b    

    def divide(self, a, b):
     self.logger.debug(f"divide {a} / {b}", extra=self.log_properties)
     return a / b

    def register_user(self, username, password):
        for user in self._user_list:
            if(user.username == username):
                return None
        user = self.User(username, password)
        self._user_list.append(user)
        return username

    def login(self, username, password):
        for user in self._user_list:
            if(user.username == username and user.password == password):
                self._current_user = user
                self.logger.debug("User {username} is in", extra=self.log_properties)
                return username
        return None

    def logout(self):
        user = self._current_user
        self._current_user = None
        self.logger.debug("User {username} is out", extra=self.log_properties)

        return user

    def get_current_user(self):
        return self._current_user