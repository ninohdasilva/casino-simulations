import random

def draw_number():
    return random.randint(0,36)

class Config:
    
    def __init__(self, numbers, coefficient) -> None:
        self.numbers = numbers
        self.coefficient = coefficient
    
    def __repr__(self) -> str:
        return f"Numbers: {self.numbers}. Coefficient: {self.coefficient}"

# class Player : 

#     def __init__(self, initial_balance, initial_bet) -> None:
#         self.initial_balance = initial_balance # final
#         self.initial_bet = initial_bet # final 
#         self.
odd_config = Config(numbers=[i for i in range (37) if i%2 != 0], coefficient=2)
even_config = Config(numbers=[i for i in range (37) if i%2 == 0 and i!=0], coefficient=2)

first_column_config = Config(numbers=[i for i in range (37) if i%3 == 1 and i!=0], coefficient=3)
second_column_config = Config(numbers=[i for i in range (37) if i%3 == 2 and i!=0], coefficient=3)
third_column_config = Config(numbers=[i for i in range (37) if i%3 == 0 and i!=0], coefficient=3)

first_dozen_config = Config(numbers=[i for i in range (1,13)], coefficient=3)
second_dozen_config = Config(numbers=[i for i in range (13,25)], coefficient=3)
third_dozen_config = Config(numbers=[i for i in range (25,37)], coefficient=3)

def calculate_winnings(drawn_number, configs, bets):
    for config in configs : 
        if drawn_number in config.numbers : 
            