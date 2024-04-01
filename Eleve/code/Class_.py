from random import*

class Pokemon:

    def __init__(self, nom, type_pokemon, points_de_vie):
        
        self.nom = nom
        self.type = type_pokemon
        self.points_de_vie = points_de_vie

    def afficher_info(self):
        """
        Affiche les pokemons présents au tournoi
        
        Returns
        -------
        None.

        """
        print(f"{self.nom} est de type {self.type} avec {self.points_de_vie} pv ")
        
    def attaquer(self, cible):
        """
        permets d'effectuer l'attaque de base de chaque pokemon en verifiant que les PV ne deviennent pas negatifs

        Parameters
        ----------
        cible : list
            Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        
        print(f"{self.nom} attaque {cible.nom}!")
        if cible.points_de_vie >= 10:
            cible.points_de_vie -= 10
        elif cible.points_de_vie<10:
            cible.points_de_vie = 0
            
        print(f"{cible.nom} a perdu 10 pv, il lui reste {cible.points_de_vie}")
            
        
class PokemonElectrique(Pokemon):
    
    def __init__(self, nom, type_pokemon, points_de_vie):
        super().__init__(nom, "electrik", points_de_vie)
    
    def attaque_speciale(self,cible):
        """
        permets d'effectuer l'attaque spéciale d'un pokemon electrique avec un nombre de chance de la realiser

        Parameters
        ----------
       cible : list
           Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        x = randint(0,6)
        if x == 1:
            
            if cible.points_de_vie >= 15:
                cible.points_de_vie -= 15
            elif cible.points_de_vie<15:
                cible.points_de_vie = 0
                
            print(f"{self.nom} attaque {cible.nom} avec Poing Eclair. {cible.nom} perd 15PV.Il lui reste {cible.points_de_vie}.")
            
            
        else:
            super().attaquer(cible)

class PokemonEau(Pokemon):
    def __init__(self, nom, type_pokemon, points_de_vie):
        super().__init__(nom, "eau", points_de_vie)
    
    def attaque_speciale(self,cible):
        """
        permets d'effectuer l'attaque spéciale d'un pokemon eau avec un nombre de chance de la realiser

        Parameters
        ----------
       cible : list
           Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        x = randint(0,5)
        if x == 1:
        
            if cible.points_de_vie >= 15:
                cible.points_de_vie -= 15
            elif cible.points_de_vie<15:
                cible.points_de_vie = 0
            
            print(f"{self.nom} attaque {cible.nom} avec Hydrocanon. {cible.nom} perd 15PV.Il lui reste {cible.points_de_vie}.")
            
        
        else:
            super().attaquer(cible)

class PokemonFeu(Pokemon):
    def __init__(self, nom, type_pokemon, points_de_vie):
        super().__init__(nom, "feu", points_de_vie)
    
    def attaque_speciale(self,cible):
       
        """
        permets d'effectuer l'attaque spéciale d'un pokemon feu avec un nombre de chance de la realiser

        Parameters
        ----------
       cible : list
           Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        
        x = randint(0,4)
        if x == 1:
            
            if cible.points_de_vie >= 15:
                cible.points_de_vie -= 15
            elif cible.points_de_vie<15:
                cible.points_de_vie = 0
            print(f"{self.nom} attaque {cible.nom} avec Lance Flamme. {cible.nom} perd 15PV.Il lui reste {cible.points_de_vie}.")
            
        else:
            super().attaquer(cible)            

class PokemonVol(Pokemon):
    def __init__(self, nom, type_pokemon, points_de_vie):
        super().__init__(nom, "vol", points_de_vie)
    
    def attaque_speciale(self,cible):
        
        """
        permets d'effectuer l'attaque spéciale d'un pokemon vol avec un nombre de chance de la realiser

        Parameters
        ----------
       cible : list
           Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        
        x = randint(0,4)
        if x == 1:
            
            if cible.points_de_vie >= 15:
                cible.points_de_vie -= 15
            elif cible.points_de_vie<15:
                cible.points_de_vie = 0
            print(f"{self.nom} attaque {cible.nom} avec Tranch'Air. {cible.nom} perd 15PV.Il lui reste {cible.points_de_vie}.")
            
        else:
            super().attaquer(cible)            

class PokemonNormal(Pokemon):
    def __init__(self, nom, type_pokemon, points_de_vie):
        super().__init__(nom, "normal", points_de_vie)
    
    def attaque_speciale(self,cible):
        
        """
        permets d'effectuer l'attaque spéciale d'un pokemon normal avec un nombre de chance de la realiser

        Parameters
        ----------
       cible : list
           Le pokemon qui va recevoir l'attaque

        Returns
        -------
        None.

        """
        
        x = randint(0,6)
        if x == 1:
            
            if cible.points_de_vie >= 15:
                cible.points_de_vie -= 15
            elif cible.points_de_vie<15:
                cible.points_de_vie = 0
            print(f"{self.nom} attaque {cible.nom} avec Ultralaser. {cible.nom} perd 15PV.Il lui reste {cible.points_de_vie}.")
            
        else:
            super().attaquer(cible)
            
#CREATION DE POKEMON:
    
pikachu = PokemonElectrique("Pikachu", "electrik",randint(40, 70))      
salameche = PokemonFeu("Salamèche","feu",randint(40, 70))    
carapuce = PokemonEau("Carapuce","eau",randint(40, 70))      
ouisticram = PokemonFeu("Ouisticram","feu",randint(40, 70))      
baudrive = PokemonVol("Baudrive","vol",randint(40, 70))
chinchidou = PokemonNormal("Chinchidou","normal",randint(40, 70))

equipe_rouge = (pikachu,carapuce,baudrive)
equipe_bleue = (ouisticram,salameche,chinchidou)
reste_r = len(equipe_rouge)
reste_b = len(equipe_bleue)

#PROGRAMME PRINCIPAL:
    
#AFFICHAGE DES PKEMONS PRESENTS DANS LE MATCH:

pikachu.afficher_info()
salameche.afficher_info()
carapuce.afficher_info()
ouisticram.afficher_info()
baudrive.afficher_info()
chinchidou.afficher_info()


#BOUCLE DU COMBAT:

print()
while reste_r != 0 and reste_b != 0: #tant qu'aucune longueur d'equipe est egale a 0
    while equipe_rouge[len(equipe_rouge) - reste_r].points_de_vie > 0 and equipe_bleue[len(equipe_bleue) - reste_b].points_de_vie > 0: #tant qu'aucun pokemon est mort 
        equipe_rouge[len(equipe_rouge) - reste_r].attaque_speciale(equipe_bleue[len(equipe_bleue) - reste_b])
        print()
        if equipe_bleue[len(equipe_bleue) - reste_b].points_de_vie > 0: # si le pokemon n'est pas mort peut faire l'attaque speciale
            equipe_bleue[len(equipe_bleue) - reste_b].attaque_speciale(equipe_rouge[len(equipe_rouge) - reste_r])
        print()
    if equipe_rouge[len(equipe_rouge) - reste_r].points_de_vie > 0 : #Si le pokemon de l'equipe rouge est vivant 
        reste_b -= 1
        if reste_b < 0:
            reste_b = 0
    elif equipe_bleue[len(equipe_bleue) - reste_b].points_de_vie > 0 : #Si le pokemon de l'equipe bleue
        reste_r -= 1
        if reste_r < 0:
            reste_r = 0
    
if reste_r == 0 : #Si il ne reste personne dans l'equipe rouge
    print("L'équipe bleue a gagné le combat !!")
elif reste_b == 0 : #Si il ne reste personne dans l'equipe rouge
    print("L'équipe rouge a gagné le combat !!")