from random import choice, sample, shuffle

# The list of words (french)
WORDS = [
    "Visage", "Laser", "Marque", "Tambour", "Pouce", "Aile", "Courant", 
    "Mode", "Mort", "Ballon", "Feu", "Lettre", "Roi", "Tube", "Brique", 
    "Rome", "Chef", "Canard", "Bouchon", "Temple", "Vert", "Microscope", 
    "Vase", "Coeur", "Enceinte", "Noel", "Entrée", "Satellite", "Lien", 
    "Poisson", "Bon", "Raie", "Moule", "Carte", "Farce", "Soleil", 
    "Poêle", "Paille", "Français", "Dinosaure", "Police", "Chateau", 
    "Sorcière", "Balle", "Grèce", "Plat", "Table", "Remise", "Opération", 
    "Cheval", "Corde", "Camembert", "Science", "Terre", "Plante", "Cellule", 
    "Bateau", "Araignée", "Noir", "Nain", "Bûche", "Soldat", "Chapeau", "Marron", 
    "Chance", "Lit", "Grenade", "Révolution", "Vol", "Vampire", "Machine", "Coton", 
    "Plage", "Pirate", "Droit", "Droite", "Grue", "Casino", "Mine", "Kangourou", 
    "Point", "Licorne", "Liquide", "Boîte", "Carton", "Couronne", "Cycle", "Bouche", 
    "Partie", "Facteur", "Roulette", "Danse", "Requin", "Alien", "Parachute", "Tokyo", 
    "Canon", "Étoile", "Sardine", "Vent", "Rouge", "Air", "Mouche", "Amour", "Éponge", 
    "Sirène", "Baguette", "Canne", "Charge", "Coq", "Pièce", "Avocat", "Chine", "Scène", 
    "Rose", "Égypte", "Jeu", "Appareil", "Trait", "Uniforme", "Champ", "Tête", "Formule", 
    "Mineur", "Pomme", "Argent", "Verre", "Patron", "Phare", "Rouleau", "Boulet", "Zéro", 
    "Cadre", "Bombe", "Oiseau", "Bête", "Pied", "Course", "Pyramide", "Mars", "Miel", 
    "Rat", "Alpes", "Palme", "Barre", "Prêt", "Toile", "Poisson", "Clé", "Paris", "Chou", 
    "Princesse", "Plume", "Prise", "Place", "Dragon", "Note", "Bâton", "Afrique", "Passé", 
    "Rame", "Espagne", "Vision", "Physique", "Champagne", "Ange", "Pilote", "Résistance", 
    "Histoire", "Tableau", "Cuisine", "Page", "Tour", "Café", "Fuite", "Corne", "Banque", 
    "Noeud", "Cochon", "Ampoule", "Banane", "Front", "Poire", "Centre", "Essence", "Plateau", 
    "Tennis", "Iris", "Journal", "Orange", "Chausson", "Esprit", "Serpent", "Pôle", "New-York", 
    "Langue", "Atout", "Rayon", "Couteau", "Livre", "Somme", "Himalaya", "Solution", "Bière", 
    "Espion", "Atlantique", "Garde", "Banc", "Russie", "Louche", "Astérix", "Queue", 
    "Cirque", "Fer", "Menu", "Eclair", "Pétrole", "Classe", "Lunettes", "Hiver", "Plan", 
    "Arc", "Bouteille", "Bouton", "Pensée", "Oeil", "Jumelles", "Temps", "Coupe", 
    "Talon", "Mousse", "Cinéma", "Main", "Allemagne", "Règle", "Sol", "Étude", "Grain", 
    "Majeur", "Quartier", "Fin", "But", "Vague", "Campagne", "Botte", "Londres", "Maladie", 
    "Cercle", "Don", "Héros", "Club", "Nuit", "Anneau", "Oeuf", "Voiture", "Gorge", "Bretelle", 
    "Égalité", "Gel", "Guide", "Vin", "Carreau", "Lumière", "Foyer", "Millionnaire", "Court", 
    "Couverture", "Balance", "Neige", "Trou", "Sortie", "Échelle", "Bar", "Cafard", "Reine", 
    "Bougie", "Baie", "Branche", "Fantôme", "Restaurant", "Timbre", "Commerce", "Numéro", "Flûte", 
    "Jour", "Schtroumpf", "Gauche", "Chemise", "Kiwi", "Ronde", "Sens", "Bourse", "Pompe", "Radio", 
    "Critique", "Jet", "Chaîne", "Ninja", "Trésor", "Chat", "Pendule", "Pingouin", "Cabinet", "Fou", 
    "Souris", "Maîtresse", "Docteur", "Feuille", "Poste", "Opéra", "Ordre", "Jungle", "Marin", 
    "Volume", "Lentille", "Vaisseau", "Blé", "Base", "Guerre", "Fort", "Baleine", "Colle", 
    "Lion", "Fraise", "Chasse", "Aiguille", "Lune", "Eau", "Mémoire", "Or", "Europe", "Voile", 
    "Molière", "Lait", "Napoléon", "Berlin", "Angleterre", "Recette", "Ceinture", "Palais", 
    "Chevalier", "Canada", "Meuble", "Portable", "Religieuse", "Pile", "Magie", "Robot", "Chien", 
    "Perle", "Glace", "Ligne", "Géant", "Génie", "Col", "Hôtel", "Forêt", "Charme", "Asile", "Tuile", 
    "Code", "Pêche", "Voleur", "Peste", "Citrouille", "Filet", "Manche", "Hôpital", "Sept", 
    "Moustache", "Boeuf", "Manège", "Herbe", "Hollywood", "Abbabaaababab", "Ensemble", "Amérique", 
    "École", "Australie", "Indien", "Pigeon", "Siège", "Piano", "Bande", "Crochet", "Titre", "Luxe", 
    "Figure", "Carrière", "Bureau", "Espace", "Avion", "Papier", "Chocolat", "Robe", "Marche", 
    "Ferme", "Membre", "Vie",
]

# Convert a list of words into a padded text box with 5 columns
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

    # Add a new player and return True if there are 4 after
    def add_player(self, player):
        self.players += [player]
        return len(self.players) == 4

    # Reset the game's state but not the player list
    def reset(self):
        self.turn = choice([0, 2])

        self.words = sample(WORDS, 25)
        
        shuffle(self.words)

        p = 9 if self.turn == 0 else 8
        self.red_words = self.words[0:p]
        self.blue_words = self.words[p:17]

        self.gray_words = self.words[17:24]
        self.black_word = self.words[24]

        shuffle(self.words)

        self.clue = None
        self.done_guess = None

    # Return the team name of the currently playing user
    def fmt_team_name(self):
        return "red :red_circle:" if self.turn in [0, 1] else "blue :blue_circle:"

    # Return a formatted text box of all requested players, with idx a list of ids
    # of the desired players
    def fmt_players(self, idx):
        return "" if len(idx) == 0 else "```\n{}\n```".format("\n".join((self.players[i].display_name for i in idx)))
    
    # Return a formatted text box containing all words
    def fmt_words(self):
        return _words_str(self.words)

    # Return a formatted text box containing all lists of words, ordered along
    # the team of the currently playing user and the switch argument
    def fmt_words_lists(self, switch):
        all = _words_str(self.words)
        ours = _words_str(self.red_words)
        theirs = _words_str(self.blue_words)
        gray = _words_str(self.gray_words)
        black = "`{}`".format(self.black_word) 

        if (self.turn in [2, 3]) ^ switch:
            ours, theirs = theirs, ours

        return (all, ours, theirs, gray, black)

    # Return a formatted text box with the compositions of the teams
    def fmt_teams(self):
        fmt = lambda i: "{} {}".format(">" if i == self.turn else " ", self.players[i].display_name)
        return ":red_circle: Red team ({} words to go):```\n{}\n{}\n```:blue_circle: Blue team ({} words to go):```\n{}\n{}\n```".format(
            str(len(self.red_words)), 
            fmt(0), 
            fmt(1), 
            str(len(self.blue_words)), 
            fmt(2), 
            fmt(3),
        )

    # Return the number of players
    def num_players(self):
        return len(self.players)

    # Return the player corresponding to that id
    def get_player(self, i):
        return self.players[i]

    # Return True if the player is actually in the game
    def in_game(self, user):
        return user in self.players

    # Return the index of that palyer
    def index_of_player(self, player):
        return self.players.index(player)

    # Return two players in the list by their ids
    def switch_players(self, i, j):
        self.players[i], self.players[j] = self.players[j], self.players[i]

    # Return the player whose turn it is
    def get_playing(self):
        return self.players[self.turn]

    # Return the user that will be playing in i turns
    def get_next_playing(self, i):
        return self.players[(self.turn + i) % 4]

    # Advances to the next turn
    def next_turn(self):
        self.turn += 1
        self.turn %= 4

    # Sets the clue
    def set_clue(self, clue):
        self.clue = clue

    # Gets the clue
    def get_clue(self):
        return self.clue

    # Sets the boolean done_guess
    def set_done_guess(self, done_guess):
        self.done_guess = done_guess

    # Return the boolean done_guess
    def has_done_guess(self):
        return self.done_guess

    # Return the words list as they are, ordered along the team currently playing
    def words_lists(self):
        ours = self.red_words
        theirs = self.blue_words

        if self.turn in [2, 3]:
            ours, theirs = theirs, ours

        return (self.words, ours, theirs, self.gray_words, self.black_word)

    # Remove a player from the list
    def remove_player(self, player):
        self.players.remove(player)