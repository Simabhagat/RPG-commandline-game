import random

class Character:
    """
    Represents a game character with basic combat attributes.

    Class Attributes:
        character_count (int): Tracks the number of Character instances created.
        MAX_HEALTH (int) : Max health character can have
        MAX_ARMOUR (int) : Max armour character can have
        MAX_HEAL (int)   : Max heal character can receive
        MAX_PENETRATION (int) : Max penetration character can have

    Instance Attributes:
        name (str): The character's name.      
        health (int): The character's health points.
        armour (int) : The character''s armour
        attack_power (int): The character's attack strength.
        penetration (int) : The character's penetration, starts at 0
    """
    MAX_HEALTH = 4000
    MAX_ARMOUR = 200
    MAX_HEAL = 700
    MAX_ATTACK_POWER = 600
    MAX_PENETRATION = 80  #40 percent of max armour
    character_count = 0

    def __init__(self, name, health, armour, attack_power, penetration):
        """
            accepts parameters : name : (str), : health : (int), arnour : (int), attack_power : (int), penetration : (int)
        """
        
        self.name = name
        self.health = health
        self.armour =armour
        self.attack_power = attack_power
        self.penetration = penetration
        # type(self).character_count += 1 
        self.__class__.character_count += 1
        print(f"{self.name} created")
        self.get_stats()


    def get_stats(self):
        
        """
            Display the character's current instance attributes.

            Iterates through the instance dictionary and prints
            each attribute name with its corresponding value.
        """

        for key, value in self.__dict__.items():
            print(f'{key} : {value}')
           
    def calc_net_damage(self, target ):
        """calculates damage after armour reduction"""
        damage = self.attack_power + self.penetration
        return damage
        
    def attack(self,target):
        """
            Attack another character and reduce their health.

            Args:
                target (Character) : The character being attacked.
                raw_damage (int)   : The attack_power of the attacker
                penetration (int)  : The penetration stat of the receiver
            Target health cannot go below zero.
        """
        
        print(f"Attacking {target.name}")
        
        damage = self.calc_net_damage(target)
        
        if target.health - damage < 0:
            damage = target.health
            target.health = 0  
        else:
            target.health -= damage 
                     
        print(f"Dealt {damage} damage")
        
        if not target.is_alive():
            print(f"{target.name} slain!")
            
        print(f"{target.name}'s health : {target.health}") 
        
    """ This section introduces mechanics buffs and debuffs """
    
    def damage_buff_debuffs (self, attack_boost, pen_boost):
        """
            increase decrease attack stats
        """
        
        self.attack_power += attack_boost
        self.penetration += pen_boost
        
    def defence_buf_debuffs(self, armour):
        """
            Increase decrease defence stats
        """        
        self.armour += armour
    
    def heal(self, heal_value = 0):
        """
            Restore 10 percent max health to the character.

            Healing cannot increase health beyond max_health.
        """
        if heal_value == 0 :
            heal_value= 0.1 * self.MAX_HEALTH
        
        if self.health + heal_value > self.MAX_HEALTH:
            heal_value = self.MAX_HEALTH-self.health
            self.health = self.MAX_HEALTH
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
    
class Warrior (Character):
    """
        Derived from Character class, introduces rage mechanic exclusive to warriors
    """
    
    def __init__(self, name, health, attack_power, armour, penetration):
        
        """
            calls __init__() of Parent class (Character) and then initialise max_armour and armour attributes
        """
        
        super().__init__( name, health, attack_power, armour, penetration)
        self.is_rage_bar_full = False
        self.rage_bar = 0
        
    def rage (self):
        """Gives a significant stat boost during rage
            1. adds 30 percent of original attack, 20 percent of Max_penetration
            2. Heals 20 percent of max hp
            3. 20 percent armour boost
        """
        print("---Rage Active---")
        self.damage_buff_debuffs(0.3*self.attack_power, 0.2*self.MAX_PENETRATION)
        self.defence_buf_debuffs(0.2 * self.armour)
        self.heal(0.2 * self.MAX_HEALTH)
        
    def attack(self, target):
        if self.is_rage_bar_full and self.rage_bar != 0:
            self.rage()
            self.rage_bar -= 1
            if self.rage_bar == 0:
                self.is_rage_bar_full = False
        elif not self.is_rage_bar_full or self.rage_bar != 0:
            self.rage_bar += 1
            if self.rage_bar == 3:
                self.is_rage_bar_full = True
        return super().attack(target)
        

character1 = Warrior("jio", 2000, 50, 150, 15)  
character2 = Warrior("airtel", 1800, 50, 165,  15)  

print("----------------Turn 1:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 1: -----------------")

print("----------------Turn 2:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")

print("------------------end of turn 2: -----------------")

print("----------------Turn 3:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")

print("------------------end of turn 3: -----------------")

print("----------------Turn 4:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 4: -----------------")

print("----------------Turn 5:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 5: -----------------")

print("----------------Turn 6:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 6: -----------------")

print("----------------Turn 7:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 7 -----------------")

print("----------------Turn 8:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 8: -----------------")

print("----------------Turn 9:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 9: -----------------")

print("----------------Turn 10:---------------------------")
character1.attack(character2)
print(f"Rage bar: {character1.rage_bar}  is rage bar full: {character1.is_rage_bar_full}")
print("------------------end of turn 10: -----------------")


# class Warrior( Character ):
    
#     """
#         Warrior class derived from Character introduces new attribute and methods 
#         as well as override the existing character methods
        
#         new attributes:
#             Rage (int) : A parameter for warrior, rage is unleased after 3 attacks
#     """ 
    
#     def __init__(self, name, max_health, attack_power, max_armour, penetration=0):
        
#         """
#             calls __init__() of Parent class (Character) and then initialise max_armour and armour attributes
#         """
        
#         super().__init__( name, max_health, attack_power, max_armour, penetration)
#         self.rage = 0 

              
#     def attack(self, target):
#         damage = super().calc_net_damage(target, self.attack_power, rage = self.rage)
#         super().attack(target, damage)
#         if self.rage == 3:
#             self.rage = 0
#         else:
#             self.rage += 1 
   
        
# class Mage( Character ):
#     def __init__(self, name, max_health, attack_power, max_armour, penetration=0):
#         super().__init__(name, max_health, attack_power, max_armour, penetration)
#         self.mana = 100
    
#     def attack(self, target):
#         """Mage has abilities:
#             Random buffs (weaken, fireball, shield) depending on random values of int 0 to 3.
#         """
        
#         buffs = ["weaken", "fireball", "shield"]
#         buff = buffs[random.randint(1,4)]
#         damage = super().calc_net_damage(target, self.attack_power, active_buff = buff)
#         self.mana -= 10
        
#         super().attack(target, damage)


# warrior = Warrior("warrior", 5000, 450, 100)
# mage = Mage("mage", 5000, 500, 80)
# # mage.attack(warrior)
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)

# # mage.get_stats()
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# # mage.get_stats()
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# # mage.get_stats()
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# # mage.get_stats()
# print(mage.armour)
# # warrior.get_stats()
# # mage.get_stats()
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# print(mage.armour)
# warrior.attack(mage)
# print("pen" ,warrior.penetration)
# print(mage.armour)

# warrior.attack(mage)
# print(mage.armour)
# warrior.attack(mage)

# print(mage.armour)

# mage.get_stats()