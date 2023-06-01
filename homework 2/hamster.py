class Hamster:
    def __init__(self, name="", age=0.0, weigh=0.0, color=""):
        self.Name=name
        self.Age=age
        self.Weigh=weigh
        self.Color=color
    def __str__(self):
        return f"Name: {self.Name}\n" \
               f"Age: {self.Age}\n" \
               f"Weigh: {self.Weigh}\n" \
               f"Color: {self.Color}\n"