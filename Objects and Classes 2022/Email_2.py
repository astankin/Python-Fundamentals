class Email:
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
input_data = input()

while not input_data == "Stop":
    sender, receiver, content = input_data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    input_data = input()

sent_emails = [int(num) for num in input().split(", ")]
for index in sent_emails:
    emails[index].send()
for email in emails:
    print(email.get_info())