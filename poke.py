#create a pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp
    
    def __str__(self):
        return f"{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})"

    # feed them to increase health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} Hp.")
        else:
            print(f"{self.name} is full.")
    
    #make them battle and decide for a winner
    def battle(self, other):
        print("Battle : ", self.name, other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"{self.name} fought {other.name} and the result is a {result}")
        # call typewheel()
    
    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lost", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1], # grass
        ]
        # declare a winner
        game_map["fire"]
        wl_matrix[0][1]
        wl_result = wl_matrix[game_map[type1]] [game_map[type2]]
        return result[wl_result]



#take a look at it
if __name__ == '__main__':
    print(Pokemon(name="bulbasaur", primary_type="grass"))
    print(Pokemon(name="charmander", primary_type="fire"))

