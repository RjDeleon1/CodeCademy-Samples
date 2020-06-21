class Pokemon:
  def __init__(self, name, level,  types, is_knocked_out):
    self.name = name
    self.level = level
    self.max_health = level * 7
    self.health = self.max_health
    self.types = types
    self.is_knocked_out = is_knocked_out
    self.type_weakness = {'Thunder': ['Ground'], 'Water': ['Grass', 'Thunder'], 'Fire': ['Water', 'Ground'], 'Grass': ['Fire', 'Lightning'], 'Ground': ['Water', 'Grass'] }
    self.weak = self.type_weakness[self.types]
  
  def __repr__(self):
    return f"{self.name}"

  def lose_health(self, health_lost):
    if self.health > 0:
      self.health -= health_lost
      print(f"\n{self.name} lost {health_lost} hp, his health now equals {self.health}")
      if self.health <= 0:
        print(f"\n{self.name}'s health is currently {self.health}")
        self.knock_out()
    else:
      print(f"\n{self.name}'s health is currently {self.health}, he has fainted")
      self.knock_out()
  
  def gain_health(self, gained_health):
    if self.health > 0 and self.health < self.max_health:
      self.health += gained_health
      if self.health > self.max_health:
        self.health = self.max_health
        print(f"\n{self.name} gained {gained_health} health \n{self.name}'s health is now {self.health}")
        print(f"\n{self.name} cannot gain more health than it's max health, it's health will be rounded down to it's original max health")
      else:
        print(f"\n{self.name} gained {gained_health} health \n{self.name}'s health is now {self.health}")

      
    elif self.health > 0 and self.health >= self.max_health:
      print(f"\n{self.name} cannot gain more health")
    
    else:
      print(f"\n{self.name}'s health is {self.health}, it has fainted and cannot gain health. Use a revival item!")
  
  def knock_out(self):
      if self.health <= 0:
        print(f"\n{self.name} has fainted")
        self.is_knocked_out = True
      else:
        print(f"\n{self.name}'s health is higher than zero, this pokemon has not fainted")
        if self.is_knocked_out == True:
          self.is_knocked_out = False

  def revive(self):
    if self.health <= 0:
      print(f"\nYou have applied a revive to {self.name}")
      self.is_knocked_out = False
      self.health = 1
      print(f"\n{self.name}'s health is: {self.health}, this pokemon is no longer fainted")
    else:
        print(f"{self.name}'s health is {self.health}, a revive can't be used")

  def battle(self, enemy):
    print(f"\nBattle will now begin: \n{self.name} a {self.types} type Vs. {enemy.name} a {enemy.types} type")
    if self.health > 0 and enemy.health > 0:
      if enemy.types in self.weak:
        self.lose_health(self.level*2)
      else:
        self.lose_health(self.level)
    else:
      print("One or more pokemon cannot battle, they have fainted")

class Trainer:
  def __init__(self, pokemons, name, potions, current_pokemon):
    self.pokemons = pokemons
    self.name = name
    self.potions = potions
    self.current_pokemon = self.pokemons[current_pokemon]

  def __repr__(self):
    return f"\n\tTrainer info: \n\tTrainer Name: {self.name} \n\tPokemon: {self.pokemons} \n\tPotions in hand: {self.potions} \n\tCurrent Pokemon: {self.current_pokemon}"
  
  def use_potion(self):
    print(f"\nUsing a potion on {self.current_pokemon}")
    self.potions -=1
    self.current_pokemon.gain_health(self.current_pokemon.max_health/2)

  def fight(self, trainer):
    print(f"\n\tStarting Fight... \n{self.name} Vs. {trainer.name}")
    trainer.current_pokemon.battle(self.current_pokemon)

  def switch_pokemon(self, index):
    if self.pokemons[index].health > 0:
      print(f"Now Switching Pokemon...")
      print(f"Switching {self.current_pokemon} for {self.pokemons[index]}")
      self.current_pokemon = self.pokemons[index]
      print(f"Current pokemon is now: {self.current_pokemon}")
    else:
      print("Cannot change pokemon, one or more pokemon have fainted")

pikachu = Pokemon('Pikachu', 5, 'Thunder', False)

groudon = Pokemon('Groudon', 5, 'Ground', False)

ash = Trainer([pikachu, groudon], "Ash Ketchum", 4, 0)
gary = Trainer([groudon, pikachu], "Gary", 4, 0)
print(ash)
print(gary)

gary.fight(ash)
gary.fight(ash)
gary.fight(ash)
gary.fight(ash)
ash.fight(gary)

ash.switch_pokemon(1)
print(ash)
ash.switch_pokemon(0)
