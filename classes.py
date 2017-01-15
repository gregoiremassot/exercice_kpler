class Trajet:
    def __init__(self, portDepart, portArrivee, cargaison):
        self.portDepart = portDepart
        self.portArrivee = portArrivee
        self.cargaison = cargaison

class Cargaison:
    def __init__(self, produit, quantite, unite):
        self.produit = produit
        self.quantite = quantite
        self.unite = unite

class Navire:
    def __init__(self, nom, imo, nationalite,taille, tonnage, type, tanker, cargo, soustype):
        self.nom = nom
        self.imo = imo
        self.nationalite = nationalite
        self.tonnage = tonnage
        self.type = type
        self.tanker = tanker
        self.cargo = cargo
        self.soustype = soustype





