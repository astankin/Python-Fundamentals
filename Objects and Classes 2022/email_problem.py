class Emai:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
line = input()
while line != "Stop":
    sender, receiver, content = line.split()
    email = Emai(sender, receiver, content)
    emails.append(email)
    line = input()
send_emails = list(map(int, input().split(", ")))
for i in send_emails:
    emails[i].send()
for email in emails:
    print(email.get_info())
