from fleet import Fleet
from herd import Herd



class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to: \n \nROBOTS VS DINOSAURS\n\n")
        for robot in self.fleet.robots:
            print(f"{robot.name} - Health Points: {robot.health}   Equipped Weapon: {robot.weapon.name}   Weapon Attack Power: {robot.weapon.attack_power}" )

        print("\n\n")

        for dino in self.herd.dinosaurs:
            print(f"{dino.name} - Health Points: {dino.health}   Attack Power: {dino.attack_power}" )

        print("\n\n")

    def battle(self):
        robo_counter = 0
        dino_counter = 0

        while robo_counter < 3 and dino_counter < 3:
            if self.fleet.robots[robo_counter].health > 0:
                self.show_robo_opponent_options()
                self.robo_turn(self.fleet.robots[robo_counter], dino_counter)
            else:
                print(f'{self.fleet.robots[robo_counter].name} is destroyed.\n')
                robo_counter += 1
                if robo_counter == 3:
                    break
                self.show_robo_opponent_options()
                self.robo_turn(self.fleet.robots[robo_counter], dino_counter)

            if self.herd.dinosaurs[dino_counter].health > 0:
                self.show_dino_opponent_options()
                self.dino_turn(self.herd.dinosaurs[dino_counter], robo_counter)
            else: 
                print(f'{self.herd.dinosaurs[dino_counter].name} is destroyed.\n')
                dino_counter += 1
                if dino_counter == 3:
                    break
                self.show_dino_opponent_options()
                self.dino_turn(self.herd.dinosaurs[dino_counter], robo_counter)

        if robo_counter == 3:
            self.display_winners("Dinosaurs win!")
        elif dino_counter == 3:
            self.display_winners("Robots win!")


    def dino_turn(self, dinosaur, robo_counter):
        self.fleet.robots[robo_counter].health = dinosaur.attack(self.fleet.robots[robo_counter])
        print(f"{self.fleet.robots[robo_counter].name} Hit - Health Points: {self.fleet.robots[robo_counter].health}\n")

    def robo_turn(self, robot, dino_counter):
        self.herd.dinosaurs[dino_counter].health = robot.attack(self.herd.dinosaurs[dino_counter])
        print(f"{self.herd.dinosaurs[dino_counter].name} Hit - Health Points: {self.herd.dinosaurs[dino_counter].health}\n")
    
    def show_dino_opponent_options(self):
        print("Team Dinosaurs Turn:")
        print("1 to Attack")
        num = input("What will you do?\n")

    def show_robo_opponent_options(self):
        print("Team Robots Turn:")
        print("1 to Attack")
        num = input("What will you do?\n")

    def display_winners(self, string):
        print(string)