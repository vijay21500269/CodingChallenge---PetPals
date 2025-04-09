from entity.pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        self.cat_color = cat_color

    def get_cat_color(self): return self.cat_color
    def set_cat_color(self, color): self.cat_color = color
