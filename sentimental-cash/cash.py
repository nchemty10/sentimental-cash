from cs50 import get_float

# Prompt the user for amount of change owed until non -ve value provide
while True:
    change_due = get_float("Change Due: ")
    if change_due >= 0:
        break

# Convert the change due to cents (multiply by 100 and round to the nearest integer)
change_due_cents = round(change_due * 100)

# Initialised number of coins to 0
num_coins = 0

# Calc num of coins needed
while change_due_cents > 0:
    if change_due_cents >= 25:
        change_due_cents -= 25
        num_coins += 1
    elif change_due_cents >= 10:
        change_due_cents -= 10
        num_coins += 1
    elif change_due_cents >= 5:
        change_due_cents -= 5
        num_coins += 1
    else:
        change_due_cents -= 1
        num_coins += 1

# Print num of coins
print(num_coins)