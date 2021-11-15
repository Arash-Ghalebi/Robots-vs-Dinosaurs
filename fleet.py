from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):

        robot1 = Robot("Eva Unit-00")
        robot2 = Robot("Eva Unit-01")
        robot3 = Robot("Eva Unit-02")

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)