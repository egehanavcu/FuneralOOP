class CondolenceMessage:
    def __init__(self, sender, message):
        self.sender = sender
        self.message = message

    def __str__(self):
        return f'{self.sender.name} said: "{self.message}"'