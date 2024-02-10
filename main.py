class Pizzas:
    def __init__(self, nom, prix, ingredients, vegetarien=False):
        self.nom = nom
        self.prix = prix
        self.ingredient = ingredients
        self.vegetarien = vegetarien

    def Afficher(self):
        veg_str = ""
        if self.vegetarien:
            veg_str = " - Vegetarienne"
        print(f"PIZZA {self.nom} : {self.prix}$" + veg_str)
        print(", ".join(self.ingredient))


class PizzaPersonalisee(Pizzas):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    dernier_numero = 0 
    def __init__(self):
        PizzaPersonalisee.dernier_numero += 1
        self.numero = PizzaPersonalisee.dernier_numero
        super().__init__("Personalisee " +str(self.numero), 0, [])
        self.demander_ingredient_user()
        self.calculer_prix()
        
        
    def demander_ingredient_user(self):
        print()
        print(f"Ingredients pour la pizza personnalisee : {self.numero}")
        while True:
            ingredient = input("Ajouter un ingredient (ou Entrer pour terminer) : ")
            if ingredient == "":
                return
            self.ingredient.append(ingredient)
            print(f"Ingredient {len(self.ingredient)} ajouté! : '{", ".join(self.ingredient)}'")
            
    def calculer_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredient) * self.PRIX_PAR_INGREDIENT
        

pizzas = [ 
    Pizzas("4 fromages", 8.5, ("brie", "emmental", "compte", "permesan"), True),
    Pizzas("Hawai", 9.5, ("tomate", "annanas", "oignons")),
    Pizzas("4 saisons", 11, ("oeuf", "emmental", "tomate", "janbon", "olive")),
    Pizzas("Vegetarienne", 7.5, ("champignons", "tomaate", "oignons", "poivrons"), True),
    PizzaPersonalisee(),
    PizzaPersonalisee()
]


def tri(e):
    return len(e.ingredient)

# pizzas.sort(key=tri,reverse=True)

for i in pizzas:
    i.Afficher()