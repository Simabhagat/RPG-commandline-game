class Character:
    """
    Represents a game character with basic combat attributes.

    Class Attributes:
        character_count (int): Tracks the number of Character instances created.

    Instance Attributes:
        name (str): The character's name.
        health (int): The character's health points.
        attack_power (int): The character's attack strength.
    """
    character_count = 0

    def __init__(self, name, max_health, attack_power, health=0):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        # type(self).character_count += 1 
        self.__class__.character_count += 1
        print(f"{self.name} created")


    def get_stats(self):
        
        """
            Display the character's current instance attributes.

            Iterates through the instance dictionary and prints
            each attribute name with its corresponding value.
        """

        print(f"{self.name}'s stats:")
        for key, value in dict(self.__dict__).items():
            print(f'{key} : {value}')
            
            
    def attack(self,target):
        """
            Attack another character and reduce their health.

            Args:
                target (Character): The character being attacked.

            Damage dealt is based on the attacker's attack_power.
            Target health cannot go below zero.
        """
        
        damage = self.attack_power
        
        print(f"Attacking {target.name}")
        
        if target.health - damage < 0:
            damage = target.health
            target.health = 0  
        else:
            target.health -= damage 
                     
        print(f"Dealt {damage} damage")
        
        if not target.is_alive():
            print(f"{target.name} slain!") 
    
    
    def heal(self):
        """
            Restore health to the character.

            Healing cannot increase health beyond max_health.
        """
        
        heal_value=500
        
        if self.health + heal_value > self.max_health:
            heal_value = self.max_health -self.health
            self.health = self.max_health
        else:
             self.health += heal_value
             
        print(f"Healed {heal_value} hp")
    
    
    def is_alive(self):
        """
            Check whether the character is alive.

            Returns:
                bool: True if health is greater than zero, otherwise False.
        """
        return self.health > 0


    