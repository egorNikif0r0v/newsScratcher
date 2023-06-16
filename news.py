import hashlib


class News:
    def __init__(self, link: str, head: str,\
                 discription: str, time: str, theme: str) -> None:
        self.link = link
        self.head = head
        self.discription = discription
        self.time = time
        self.theme = theme

    def is_cheked() -> bool:
        pass

    def log(self) -> None:
       print(   f'|  link           -> {self.link}\n'\
                f'|  head           -> {self.head}\n'\
                f'|  discription    -> {self.discription}\n'\
                f'|  time           -> {self.time}\n'\
                f'|  theme          -> {self.theme}\n')
       
    def getHash(self) -> str:
        sha = hashlib.sha1(self.link.encode('utf-8') +\
                           self.discription.encode('utf-8'))
        return sha.hexdigest()