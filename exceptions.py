


class InvalidWebHookException(Exception):
    def __init__(self):
        super().__init__("Your webhook url is invalid!")
        
class InvalidWebHookParticulars(Exception):
    def __init__(self):
        super().__init__("Your webhook particulars do not match!")
        