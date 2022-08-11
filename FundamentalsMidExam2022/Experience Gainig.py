needed_experience = float(input())
battles_count = int(input())
total_experience = 0
for battle in range(1, battles_count + 1):
    earned_experience = float(input())
    total_experience += earned_experience
    if battle % 3 == 0:
        total_experience += earned_experience * 0.15
    if battle % 5 == 0:
        total_experience -= earned_experience * 0.10
    if battle % 15 == 0:
        total_experience += earned_experience * 0.5
    if total_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        exit()
print(f"Player was not able to collect the needed experience, {(needed_experience - total_experience):.2f} more needed.")