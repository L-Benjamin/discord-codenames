from random import choice, sample, shuffle

WORDS = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
]

WORDS.sort()

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
        self.turn = choice([0, 2])

        self.words = sample(WORDS, 25)

        shuffle(self.words)

        self.red_words = self.words[0:8]
        self.blue_words = self.words[8:16]
        self.gray_words = self.words[16:24]
        self.black_word = self.words[24]

        shuffle(self.words)

        self.red_score = 0
        self.blue_score = 0

        self.clue = None
        self.nguess = None

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
        return "Red team ({}/8):```\n{}\n{}\n```Blue team ({}/8):```\n{}\n{}\n```".format(
            self.red_score, player(0), player(1), self.blue_score, player(2), player(3),
        )

    def playing(self):
        return self.players[self.turn]

    def lists(self):
        ours = self.red_words
        theirs = self.blue_words

        if self.turn == 2:
            ours, theirs = theirs, ours

        return (ours, theirs)

    def lists_str(self):
        ours = self.red_words
        theirs = self.blue_words

        if self.turn == 2:
            ours, theirs = theirs, ours

        return (_words_str(ours), _words_str(theirs))