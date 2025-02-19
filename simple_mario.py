import random

class Mario:
    def __init__(self):
        self.position = 0
        self.coins = 0
        self.is_jumping = False

    def move_right(self):
        self.position += 1
        print(f"Mario moved to position {self.position}")

    def move_left(self):
        if self.position > 0:
            self.position -= 1
            print(f"Mario moved to position {self.position}")
        else:
            print("Mario can't move left, he's at the start!")

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            print("Mario is jumping!")
            # Simulate jump time
            import time
            time.sleep(1)
            self.is_jumping = False
            print("Mario landed.")
        else:
            print("Mario is already jumping!")

    def collect_coin(self):
        self.coins += 1
        print(f"Mario collected a coin! Total coins: {self.coins}")

def game():
    mario = Mario()
    print("Welcome to Text Mario!")
    print("Commands: 'right', 'left', 'jump', 'coin', 'quit'")

    while True:
        action = input("What would Mario do? ").lower()

        if action == 'right':
            mario.move_right()
        elif action == 'left':
            mario.move_left()
        elif action == 'jump':
            mario.jump()
        elif action == 'coin':
            # Simulate finding a coin randomly
            if random.random() < 0.3:  # 30% chance to find a coin
                mario.collect_coin()
            else:
                print("No coin here.")
        elif action == 'quit':
            print(f"Game Over. Mario collected {mario.coins} coins.")
            break
        else:
            print("Invalid command. Try again!")

if __name__ == "__main__":
    game()
