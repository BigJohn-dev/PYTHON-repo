
class Diary:
    def __init__(self, username:str, password:str, gmail:str) -> None:
        self.username = username
        self.password = password
        self.gmail = gmail
        self._is_locked = True

    def is_locked(self) -> bool:
        return self._is_locked

    def unlock(self, password:str) -> bool:
        if password != self.password:
            raise ValueError("Password does not match")
        self._is_locked = False