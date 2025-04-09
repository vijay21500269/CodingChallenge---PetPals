from entity.pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed

    def get_dog_breed(self): return self.dog_breed
    def set_dog_breed(self, breed): self.dog_breed = breed
