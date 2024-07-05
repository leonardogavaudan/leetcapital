class Logger:

    def __init__(self):
        self.message_to_last_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if (
            message not in self.message_to_last_timestamp
            or timestamp - self.message_to_last_timestamp[message] >= 10
        ):
            self.message_to_last_timestamp[message] = timestamp
            return True
        else:
            return False
