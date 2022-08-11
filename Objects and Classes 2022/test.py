class Party:
    def __init__(self):
        self.people = []

    def adding_people(self, name):
        self.people.append(name)


party = Party()
while True:
    input_data = input()
    if input_data == "End":
        break

    party.adding_people(input_data)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
