from random import choice, sample, shuffle

WORDS = ["Visage","Laser","Marque","Tambour","Pouce","Aile","Courant" ,"Mode" ,"Mort" ,"Ballon" ,"Feu" ,"Lettre" ,"Roi" ,"Tube" ,"Brique" ,"Rome" ,"Chef" ,"Canard" ,"Bouchon" ,"Temple" ,"Vert" ,"Microscope" ,"Vase" ,"Coeur" ,"Enceinte" ,"Noel" ,"Entrée" ,"Satellite" ,"Lien" ,"Poisson" ,"Bon" ,"Raie" ,"Moule" ,"Carte","Farce" ,"Soleil" ,"Poêle" ,"Paille" ,"Français" ,"Dinosaure" ,"Police" ,"Chateau" ,"Sorcière" ,"Balle" ,"Grèce" ,"Plat" ,"Table" ,"Remise" ,"Opération" ,"Cheval" ,"Corde","Camembert","Science","Terre","Plante","Cellule","Bateau","Araignée","Noir","Nain","Bûche" ,"Soldat","Chapeau" ,"Marron","Chance","Lit","Grenade","Révolution","Vol","Vampire","Machine","Coton","Plage","Pirate","Droit","Droite","Grue","Casino","Mine","Kangourou","Point","Licorne","Liquide","Boîte","Carton","Couronne","Cycle","Bouche","Partie","Facteur","Roulette","Danse","Requin","Alien","Parachute","Tokyo","Canon","Étoile","Sardine","Vent","Rouge","Air","Mouche","Amour","Éponge","Sirène","Baguette","Canne","Charge","Coq","Pièce","Avocat","Chine","Scène","Rose","Égypte","Jeu","Appareil","Trait","Uniforme","Champ","Tête","Formule","Mineur","Pomme","Argent","Verre","Patron","Phare","Rouleau","Boulet","Zéro","Cadre","Bombe","Oiseau","Bête","Pied","Course","Pyramide","Mars","Miel","Rat","Alpes","Palme","Barre","Prêt","Toile","Poisson","Clé","Paris","Chou","Princesse","Plume","Prise","Place","Dragon","Note","Bâton","Afrique","Passé","Rame","Espagne","Vision","Physique","Champagne","Ange","Pilote","Résistance","Histoire","Tableau","Cuisine","Page","Tour","Café","Fuite","Corne","Banque","Noeud","Cochon","Ampoule","Banane","Front","Poire","Centre","Essence","Plateau","Tennis","Iris","Journal","Orange","Chausson","Esprit","Serpent","Pôle","New-York","Langue","Atout","Rayon","Couteau","Livre","Somme","Himalaya","Solution","Bière","Espion","Atlantique","Garde","Banc","Russie","Louche","Astérix","Queue","Cirque","Fer","Menu","Eclair","Pétrole","Classe","Lunettes","Hiver","Plan","Arc","Bouteille","Bouton","Pensée","Oeil","Jumelles","Temps","Coupe","Talon","Mousse","Cinéma","Main","Allemagne","Règle","Sol","Étude","Grain","Majeur","Quartier","Fin","But","Vague","Campagne","Botte","Londres","Maladie","Cercle","Don","Héros","Club","Nuit","Anneau","Oeuf","Voiture","Gorge","Bretelle","Égalité","Gel","Guide","Vin","Carreau","Lumière","Foyer","Millionnaire","Court","Couverture","Balance","Neige","Trou","Sortie","Échelle","Bar","Cafard","Reine","Bougie","Baie","Branche","Fantôme","Restaurant","Timbre","Commerce","Numéro","Flûte","Jour","Schtroumpf","Gauche","Chemise","Kiwi","Ronde","Sens","Bourse","Pompe","Radio","Critique","Jet","Chaîne","Ninja","Trésor","Chat","Pendule","Pingouin","Cabinet","Fou","Souris","Maîtresse","Docteur","Feuille","Poste","Opéra","Ordre","Jungle","Marin","Volume","Lentille","Vaisseau","Blé","Base","Guerre","Fort","Baleine","Colle","Lion","Fraise","Chasse","Aiguille","Lune","Eau","Mémoire","Or","Europe","Voile","Molière","Lait","Napoléon","Berlin","Angleterre","Recette","Ceinture","Palais","Chevalier","Canada","Meuble","Portable","Religieuse","Pile","Magie","Robot","Chien","Perle","Glace","Ligne","Géant","Génie","Col","Hôtel","Forêt","Charme","Asile","Tuile","Code","Pêche","Voleur","Peste","Citrouille","Filet","Manche","Hôpital","Sept","Moustache","Boeuf","Manège","Herbe","Hollywood","Abbabaaababab","Ensemble","Amérique","École","Australie","Indien","Pigeon","Siège","Piano","Bande","Crochet","Titre","Luxe","Figure","Carrière","Bureau","Espace","Avion","Papier","Chocolat","Robe","Marche","Ferme","Membre","Vie"]

def _words_str(words):
    if len(words) < 5:
        return "```\n{}\n```".format(" ".join((w for w in words)))
    else:
        pads = [max((len(w) for w in words[x::5])) for x in range(5)]

    res = "```\n"
    for i, word in enumerate(words):
        x = i % 5
        res += "{}{}{}".format(word, " " * (pads[x] - len(word)), "\n" if x == 4 else " ")
    res += "\n```"

    return res

class Data:
    
    def __init__(self):
        self.players = []
        self.reset()

    def reset(self):
        self.turn = choice([0, 2])

        self.words = sample(WORDS, 25)

        shuffle(self.words)

        if self.turn == 0:
            self.red_words = self.words[0:9]
            self.blue_words = self.words[9:17]
        else:
            self.red_words = self.words[0:8]
            self.blue_words = self.words[8:17]
                 
        self.gray_words = self.words[17:24]
        self.black_word = self.words[24]

        shuffle(self.words)

        self.clue = None
        self.nguess = None
        self.done_guess = None

    def words_str(self):
        return _words_str(self.words)

    def red_words_str(self):   
        return _words_str(self.red_words)

    def blue_words_str(self):
        return _words_str(self.blue_words)

    def gray_words_str(self):
        return _words_str(self.gray_words)

    def players_str(self):
        player = lambda i: "{} {}".format(">" if i == self.turn else " ", self.players[i].display_name)
        return "Red team ({} words to go):```\n{}\n{}\n```Blue team ({} words to go):```\n{}\n{}\n```".format(
            str(len(self.red_words)), player(0), player(1), 
            str(len(self.blue_words)), player(2), player(3),
        )

    def playing(self):
        return self.players[self.turn]

    def lists(self):
        ours = self.red_words
        theirs = self.blue_words

        if self.turn in [2, 3]:
            return (theirs, ours)
        return (ours, theirs)

    def lists_str(self):
        ours = self.red_words
        theirs = self.blue_words

        if self.turn in [2, 3]:
            return (_words_str(theirs), _words_str(ours))
        return (_words_str(ours), _words_str(theirs))

    def team_str(self):
        return "red" if self.turn in [0, 1] else "blue"