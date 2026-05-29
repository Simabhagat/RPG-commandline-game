from classes import Character

def main():
    
        print("Create character:")
        character1 = Character("Johm", 5000, 500)
        character1.get_stats()
        print()

        print("Create another character:")
        character2 = Character("Vivian", 4800, 600)
        character2.get_stats()
        print()
        
        character2.attack(character1)
        
        character1.get_stats()
        
        character1.heal()
        
        character1.get_stats()
        
        character1.heal()
        
        character1.get_stats()

        print(f"Total characters available: {Character.character_count}")
if __name__ == "__main__":
    main()