import random

class Character:
    def __init__(self, name, gear, race, character_class):
        self.name = name
        self.gear = gear
        self.race = race
        self.character_class = character_class
        self.health = random.randint(50, 100)
        self.strength = random.randint(10, 20)
        self.initiative = random.randint(1, 10)

    def attack(self, opponent):
        if self.is_alive() and opponent.is_alive():
            hit_strength = random.randint(1, self.strength)
            print(f"{self.name} attacks {opponent.name} with strength {hit_strength}.")
            if hit_strength >= opponent.strength:
                opponent.health -= hit_strength
                if opponent.is_alive():
                    print(f"{opponent.name} now has {opponent.health} health left.")
                else:
                    print(f"{opponent.name} has died.")
            else:
                print("The attack missed.")

    def is_alive(self):
        return self.health > 0

def main():
    hero = Character("Hero", "Sword", "Human", "Warrior")
    enemy = Character("Enemy", "Claws", "Orc", "Barbarian")

    while hero.is_alive() and enemy.is_alive():
        if hero.initiative >= enemy.initiative:
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
        else:
            if enemy.is_alive():
                enemy.attack(hero)
            if hero.is_alive():
                hero.attack(enemy)

    if hero.is_alive():
        print("The hero is victorious!")
    else:
        print("The enemy has triumphed!")

if __name__ == "__main__":
    main()