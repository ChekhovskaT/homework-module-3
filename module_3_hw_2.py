import random

def get_numbers_ticket(min, max, quantity):
    #Checking the correctness of the parameters
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []
    
    #Generration of unique randon numbers
    random_numbers = random.sample(range(min, max + 1), quantity)

    #Sorting the result
    return sorted(random_numbers)

#Examples
lottery_numbers = get_numbers_ticket(1, 54, 7)
lottery_num = get_numbers_ticket (1, 10001, 5)
lot_numbers = get_numbers_ticket (1, 36, 40)

print(f"Your lottery numbers are: {lottery_numbers}")
print(f"Your lottery numbers are: {lottery_num}")
print(f"Your lottery numbers are: {lot_numbers}")