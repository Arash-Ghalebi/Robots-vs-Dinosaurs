from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        #self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur("Jainosaurus", 25)
        dino2 = Dinosaur("Spinosaurus", 25)
        dino3 = Dinosaur("Triceratops", 25)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)