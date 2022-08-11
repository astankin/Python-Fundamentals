capacity = int(input())
data = input()
record = {}
while not data == "Statistics":
    data = data.split("=")
    command = data[0]
    if command == "Add":
        username = data[1]
        sent = int(data[2])
        received = int(data[3])
        if username not in record:
            record[username] = [sent, received]
    elif command == "Message":
        sender = data[1]
        receiver = data[2]
        if sender in record and receiver in record:
            record[sender][0] += 1
            record[receiver][1] += 1
            if record[sender][0] + record[sender][1] >= capacity:
                del record[sender]
                print(f"{sender} reached the capacity!")
            if record[receiver][1] + record[receiver][0] >= capacity:
                del record[receiver]
                print(f"{receiver} reached the capacity!")
    elif command == "Empty":
        username = data[1]
        if username == "All":
            record = {}
        else:
            if username in record:
                del record[username]

    data = input()

print(f"Users count: {len(record)}")
for username, value in record.items():
    number_of_messages = value[0] + value[1]
    print(f"{username} - {number_of_messages}")
