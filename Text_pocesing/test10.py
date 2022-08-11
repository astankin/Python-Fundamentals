winn_symbols = ['@', '#', '$', '^']
data = [string.strip() for string in input().split(",")]


def half_ticket_check(half):
    counter1 = 0
    counter = 0
    for el in half:
        if el == symbol:
            counter += 1
        else:
            if counter >= counter1:
                counter1 = counter
                counter = 0
    if counter >= counter1:
        counter1 = counter
    return counter1


for ticket in data:
    if len(ticket) == 20:
        condition = False
        for symbol in winn_symbols:

            if symbol*20 in ticket:
                condition = True
                print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
                break
            else:
                left_side = ticket[:10]
                right_side = ticket[10:]
                if symbol in left_side and symbol in right_side:
                    condition = True
                    counter1 = half_ticket_check(left_side)
                    counter2 = half_ticket_check(right_side)
                    match_length = min(counter1, counter2)
                    if 10 > match_length >= 6:
                        print(f'ticket "{ticket}" - {match_length}{symbol}')
                    elif match_length < 6:
                        condition = False
        if not condition:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")

