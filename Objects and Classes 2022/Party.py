class Party:
    def __init__(self):
        self.people = []

    def adding_people(self, line):
        self.people.append(line)


party = Party()
line = input()
while line != "End":
    party.adding_people(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
