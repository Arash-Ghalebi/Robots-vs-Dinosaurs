from fleet import Fleet
from herd import Herd
from weapon import Weapon



class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.ores = 1

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to: \n \nROBOTS VS DINOSAURS\n\n")
        for robot in self.fleet.robots:
            print(f"{robot.name} - Health Points: {robot.health}   Equipped Weapon: {robot.weapon.name}   Weapon Attack Power: {robot.weapon.attack_power}   Crit Chance: {robot.weapon.crit_chance}" )

        print("\n\n")

        for dino in self.herd.dinosaurs:
            print(f"{dino.name} - Health Points: {dino.health}   Attack Power: {dino.attack_power}" )

        print("\n\n")

    def battle(self):
        robo_counter = 0
        dino_counter = 0

        while robo_counter < 3 and dino_counter < 3:
            if self.fleet.robots[robo_counter].health > 0:
                robo_action = self.show_robo_opponent_options()
                if robo_action == '1':
                    self.robo_attack(self.fleet.robots[robo_counter], dino_counter)
                elif robo_action == '2':
                    if self.ores > 0:
                        self.forge()
                    else:
                        print("You do not have any ores.")
                        continue
                elif robo_action == '3':
                    robo_counter, dino_counter = self.self_destruct(self.fleet.robots[robo_counter], dino_counter, robo_counter)
                    if robo_counter == 3:
                        break
            else:
                print(f'\n{self.fleet.robots[robo_counter].name} is destroyed.\n')
                robo_counter += 1
                if robo_counter == 3:
                    break
                robo_action = self.show_robo_opponent_options()
                if robo_action == '1':
                    self.robo_attack(self.fleet.robots[robo_counter], dino_counter)
                elif robo_action == '2':
                    if self.ores > 0:
                        self.forge()
                    else:
                        print("You do not have any ores.")
                        continue
                elif robo_action == '3':
                    robo_counter = self.self_destruct(self.fleet.robots[robo_counter], dino_counter, robo_counter)

            if self.herd.dinosaurs[dino_counter].health > 0:
                dino_action = self.show_dino_opponent_options()
                if dino_action == '1':
                    self.dino_attack(self.herd.dinosaurs[dino_counter], robo_counter)
                #elif dino_action == '2':
                    #self.roar()
                elif dino_action == '3':
                    self.rest(self.herd.dinosaurs[dino_counter])
            else: 
                print(f'\n{self.herd.dinosaurs[dino_counter].name} is destroyed.\n')
                dino_counter += 1
                self.ores += 1
                if dino_counter == 3:
                    break
                dino_action = self.show_dino_opponent_options()
                if dino_action == '1':
                    self.dino_attack(self.herd.dinosaurs[dino_counter], robo_counter)
                #elif dino_action == '2':
                    #self.roar()
                elif dino_action == '3':
                    self.rest(self.herd.dinosaurs[dino_counter])

        if robo_counter == 3 and dino_counter == 3:
            print("It's a tie!")
        elif robo_counter == 3:
            self.display_winners("Dinosaurs win!")
        elif dino_counter == 3:
            self.display_winners("Robots win!")


    def dino_attack(self, dinosaur, robo_counter):
        self.fleet.robots[robo_counter].health = dinosaur.attack(self.fleet.robots[robo_counter])
        print(f"\n{self.fleet.robots[robo_counter].name} Hit - Health Points: {self.fleet.robots[robo_counter].health}\n")

    #def roar(self):

    def rest(self, dinosaur):
        dinosaur.health += 20

    def robo_attack(self, robot, dino_counter):
        self.herd.dinosaurs[dino_counter].health = robot.attack(self.herd.dinosaurs[dino_counter])
        print(f"\n{self.herd.dinosaurs[dino_counter].name} Hit - Health Points: {self.herd.dinosaurs[dino_counter].health}\n")

    def forge(self):
        self.ores = self.ores - 1
        num = input("Which upgrade would you like to forge? ('1' for 10% Crit Chance and '2' for 3 Attack Power)\n")
        if num == '1':
            for robot in self.fleet.robots:
                robot.weapon.crit_chance += 10
        elif num == '2':
            for robot in self.fleet.robots:
                robot.weapon.attack_power += 3
        print(f"\nForge complete: Weapon Attack Power: {robot.weapon.attack_power}   Crit Chance: {robot.weapon.crit_chance}\n" )

    def self_destruct(self, robot, dino_counter, robo_counter):
        robot.health = 0
        self.herd.dinosaurs[dino_counter].health = self.herd.dinosaurs[dino_counter].health - 75
        print(f"\n{self.herd.dinosaurs[dino_counter].name} Hit - Health Points: {self.herd.dinosaurs[dino_counter].health}\n")
        print(f'\n{self.fleet.robots[robo_counter].name} is destroyed.\n')
        robo_counter += 1
        if self.herd.dinosaurs[dino_counter].health <= 0:
            dino_counter += 1
        return robo_counter, dino_counter

    
    def show_dino_opponent_options(self):
        print("Team Dinosaurs Turn:")
        print("1 to Attack")
        print("2 to Roar")
        print("3 to Rest")
        num = input("What will you do?\n")
        return num

    def show_robo_opponent_options(self):
        print(f"Team Robots Turn (Current Ore Count - {self.ores}):")
        print("1 to Attack")
        print("2 to Forge")
        print("3 to Self-Destruct")
        num = input("What will you do?\n")
        return num

    def display_winners(self, string):
        print(string)