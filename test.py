import random

class Character:
    """
    Represents a game character with basic combat attributes.

    Class Attributes:
        character_count (int): Tracks the number of Character instances created.

    Instance Attributes:
        name (str): The character's name.
        max_health (int) : The character''s max health
        health (int): The character's health points.
        max_armour (int) : The character''s max armour
        armour (int) : The character''s armour
        attack_power (int): The character's attack strength.
        armour 
        penetration (int) : The character's penetration, starts at 0
    """
    character_count = 0

    def __init__(self, name, max_health, attack_power, max_armour, penetration):
        self.name = name
        self.max_health = self.health = max_health
        self.max_armour = self.armour = max_armour
        self.attack_power = attack_power
        self.penetration = penetration
        
        # type(self).character_count += 1 
        self.__class__.character_count += 1
        print(f"{self.name} created")


    def get_stats(self):
        
        """
            Display the character's current instance attributes.

            Iterates through the instance dictionary and prints
            each attribute name with its corresponding value.
        """

        for key, value in self.__dict__.items():
            print(f'{key} : {value}')
    
    @classmethod        
    def calc_net_damage(cls, target, raw_damage, **buffs_debuffs_dict ):
        
        """
            It will calculate various buffs and debuffs and then return the net damage after.
            defence buffs: armour(for warrior), shield(mages can deploy shield instead of attack in his turn)
            Attack buffs : Penetration
            Attack debuffs : Weaken (can be cast along side attack by mage only)
            other buffs/ debuffs: strength(+/- attack and armour), rage(+penetration)
        """
        #calculate buffs_debuffs
        """
        valid buffs debuffs:
            penetration, shield, rage, strength
        """
        damage = raw_damage
        if buffs_debuffs_dict:
            if  buffs_debuffs_dict.get("rage") == 3:
                print("rage active")
                damage = raw_damage + 0.3 * target.armour
            else:
                match buffs_debuffs_dict.get("active_buff"):
                    case "fireball":
                        damage = raw_damage + 500 #fireball damage = 500
                    case "weaken":
                        target.attack_power -= 30
                        target.armour -= 10
                        target.health -= 100
                    case "shield":
                        """50 percent damage reduction when another character attack him"""
                        pass 
            
        print("raw damge ", raw_damage)
        print("test ", 0.2 * target.max_armour, target.armour)
        if target.armour > 0.4 * target.max_armour:
            
            damage = damage - 0.2 * target.max_armour
            target.armour -= 0.2 *  target.max_armour
        else: 
            damage = raw_damage - target.armour
            target.armour = 0 
            
        return damage       
    
        
    def attack(self,target, damage):
        """
            Attack another character and reduce their health.

            Args:
                target (Character): The character being attacked.

            Damage dealt is based on the attacker's attack_power.
            Target health cannot go below zero.
        """
        
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
        
        heal_value= 0.1 * self.max_health
        
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
    
    

class Warrior( Character ):
    
    """
        Warrior class derived from Character introduces new attribute and methods 
        as well as override the existing character methods
        
        new attributes:
            Rage (int) : A parameter for warrior, rage is unleased after 3 attacks
    """ 
    
    def __init__(self, name, max_health, attack_power, max_armour, penetration=0):
        
        """
            calls __init__() of Parent class (Character) and then initialise max_armour and armour attributes
        """
        
        super().__init__( name, max_health, attack_power, max_armour, penetration)
        self.rage = 0 

              
    def attack(self, target):
        damage = super().calc_net_damage(target, self.attack_power, rage = self.rage)
        super().attack(target, damage)
        if self.rage == 3:
            self.rage = 0
        else:
            self.rage += 1 
   
        
class Mage( Character ):
    def __init__(self, name, max_health, attack_power, max_armour, penetration=0):
        super().__init__(name, max_health, attack_power, max_armour, penetration)
        self.mana = 100
    
    def attack(self, target):
        """Mage has abilities:
            Random buffs (weaken, fireball, shield) depending on random values of int 0 to 3.
        """
        
        buffs = ["weaken", "fireball", "shield"]
        buff = buffs[random.randint(1,4)]
        damage = super().calc_net_damage(target, self.attack_power, active_buff = buff)
        self.mana -= 10
        
        super().attack(target, damage)


warrior = Warrior("warrior", 5000, 450, 100)
mage = Mage("mage", 5000, 500, 80)
# mage.attack(warrior)
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)

# mage.get_stats()
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
# mage.get_stats()
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
# mage.get_stats()
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
# mage.get_stats()
print(mage.armour)
# warrior.get_stats()
# mage.get_stats()
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
print(mage.armour)
warrior.attack(mage)
print("pen" ,warrior.penetration)
print(mage.armour)

warrior.attack(mage)
print(mage.armour)
warrior.attack(mage)

print(mage.armour)

mage.get_stats()