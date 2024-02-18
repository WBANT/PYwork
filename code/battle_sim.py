### Character class ###
class Character:

    Name = ["A", "B", "C", "D", "E"]
    Race = ["Red", "White", "Black", "Blue"]
    character_class = ["Barbarian", "Cleric", "Druid", "Knight", "Wizard"]
    Gear = ["Helmet", "Chestplate", "Boots"]

    def __init__(self, Name, Gear, Health, Strength, Initiative, Race, character_class):
        self.Name = random.choice(Name)
        self.Gear = random.choice(Gear)
        self.Health = random.randint(1,100)
        self.Strength = random.randint(1,100)
        self.Initiative = Initiative
        self.Race = Race
        self.character_class = character_class

    def objectstrength(self)


    def attack():
        self.Initiative = random.randint(1,10)
        hit_strength = random.randint(1, self.strength)
        print(f"{self.name} attacks [opponent.name] with strength {hit_strength}. ")
        if hit_strength >= opponent.strength:
            opponent.health -= hit_strength
            print(f"(opponent.name) now has {opponent.health} health left. ")
        else:
            print("The attack missed. ")
    
    def is_alive()
        return self.health > 0

### Main program ###

def main():
    Hero = character("Hero", "Sword", "Human", "Warrior")
    Enemy = character("Enemy", "Claws", "Orc", "Barbarian")

    while Hero.is_alive() and Enemy.is_alive():
        if Hero.Initiative >= Enemy.Initiative:
            Hero.attack(enemy)
            if Enemy.is_alive()
                Enemy.attack(hero)

        else: 
            if hero.is_alive

