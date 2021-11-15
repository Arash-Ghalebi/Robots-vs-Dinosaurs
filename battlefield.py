from fleet import Fleet
from herd import Herd



class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        # When main is ran and an instance of Battlefield is created, run_game is the only method run in main. Within run_game, all these other methods are ran.
        self.fleet.create_fleet()
        self.herd.create_herd()
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to: \n \nROBOTS VS DINOSAURS\n\n")
        # The name, health, and attack power of each unit is displayed here.
        for robot in self.fleet.robots:
            print(f"{robot.name} - Health Points: {robot.health}   Equipped Weapon: {robot.weapon.name}   Weapon Attack Power: {robot.weapon.attack_power}" )

        print("\n\n")

        for dino in self.herd.dinosaurs:
            print(f"{dino.name} - Health Points: {dino.health}   Attack Power: {dino.attack_power}" )

        print("\n\n")

    def battle(self):
        robo_counter = 0
        dino_counter = 0

        # Once a robot or dinosaur's health reaches zero, the counter for their respective team goes up one. Once either team has a counter reach 3 (all of the units have died), then the loop will end and a winner is declared.
        while robo_counter < 3 and dino_counter < 3:
            # If the unit is still alive after the last attack, it will now attack this turn.
            if self.fleet.robots[robo_counter].health > 0:
                self.show_robo_opponent_options()
                self.robo_turn(self.fleet.robots[robo_counter], dino_counter)
            # If the health of the unit reached 0 after last attack, then the next unit in the fleet or herd will atttack this turn.    
            else:
                print(f'{self.fleet.robots[robo_counter].name} is destroyed.\n')
                robo_counter += 1
                # If all the robots have been destroyed, break out of the loop.
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

        # Message will be displayed based on which team destroyed all of the units of the other team first. Message displayed will indicate the winner.
        if robo_counter == 3:
            self.display_winners("Dinosaurs win!")
        elif dino_counter == 3:
            self.display_winners("Robots win!")


    def dino_turn(self, dinosaur, robo_counter):
        # Dinosaur will attack a robot and then display the new health of the robot.
        self.fleet.robots[robo_counter].health = dinosaur.attack(self.fleet.robots[robo_counter])
        print(f"{self.fleet.robots[robo_counter].name} Hit - Health Points: {self.fleet.robots[robo_counter].health}\n")

    def robo_turn(self, robot, dino_counter):
        # Same process, this time robot attacks dino, and dino health is displayed.
        self.herd.dinosaurs[dino_counter].health = robot.attack(self.herd.dinosaurs[dino_counter])
        print(f"{self.herd.dinosaurs[dino_counter].name} Hit - Health Points: {self.herd.dinosaurs[dino_counter].health}\n")
    
    def show_dino_opponent_options(self):
        # User interface for the player to choose what to do on their turn using number inputs.
        print("Team Dinosaurs Turn:")
        print("1 to Attack")
        num = input("What will you do?\n")

    def show_robo_opponent_options(self):
        print("Team Robots Turn:")
        print("1 to Attack")
        num = input("What will you do?\n")

    def display_winners(self, string):
        print(string)