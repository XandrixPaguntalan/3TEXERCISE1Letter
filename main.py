class letter:
    def __init__(self, letterFrom, letterTo):
        self.receiver = letterTo
        self.sender = letterFrom
        self.body = []

    def addLine(self, Line):
        self.body.append(Line)

    def getText(self):
        text = "Dear " + self.receiver + ":\n"
        text = text + "\n"

        for Line in self.body:
            text = text + Line + "\n"

        text = text + "\nSincerely, \n"
        text = text + "\n" + self.sender

        return text
