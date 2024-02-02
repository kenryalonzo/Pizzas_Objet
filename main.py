class Pizzas:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredient = ingredients

    def Afficher(self):
        print(f"PIZZA {self.nom} : {self.prix}$")
        print(", ".join(self.ingredient))

# pizza1 = Pizzas("4 fromages", 8.5, ("brie", "emmental", "compte", "permesan"))
# pizza1.Afficher()

pizzas = (
    Pizzas("4 fromages", 8.5, ("brie", "emmental", "compte", "permesan")),
    Pizzas("Hawai", 9.5, ("tomate", "annanas", "oignons")),
    Pizzas("4 saisons", 11, ("oeuf", "emmental", "tomate", "janbon")),
    Pizzas("Vegetarienne", 7.5, ("champignons", "tomaate", "oignons", "poivrons"))
)

for i in pizzas:
    i.Afficher()