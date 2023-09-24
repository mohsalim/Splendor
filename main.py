from enum import Enum


class Gem(Enum):
    WHITE = 1
    BLUE = 2
    GREEN = 3
    RED = 4
    BLACK = 5


class Card:
    def __init__(self, gem, point, cost):
        self.gem = gem
        self.point = point
        self.cost = cost


class Cost:
    def __init__(self, white, blue, green, red, black):
        self.white = white
        self.blue = blue
        self.green = green
        self.red = red
        self.black = black


level_one_cards = [
    # Base copy/paste
    #    Card(Gem., 0, Cost(0, 0, 0, 0, 0)),

    # White cards
    Card(Gem.WHITE, 0, Cost(0, 2, 0, 0, 2)),
    Card(Gem.WHITE, 0, Cost(3, 1, 0, 0, 1)),
    Card(Gem.WHITE, 0, Cost(0, 0, 0, 2, 1)),
    Card(Gem.WHITE, 0, Cost(0, 1, 1, 1, 1)),
    Card(Gem.WHITE, 0, Cost(0, 1, 2, 1, 1)),
    Card(Gem.WHITE, 1, Cost(0, 0, 4, 0, 0)),
    Card(Gem.WHITE, 0, Cost(0, 2, 2, 0, 1)),
    Card(Gem.WHITE, 0, Cost(0, 3, 0, 0, 0)),

    # Blue cards
    Card(Gem.BLUE, 0, Cost(1, 0, 0, 0, 2)),
    Card(Gem.BLUE, 0, Cost(0, 0, 2, 0, 2)),
    Card(Gem.BLUE, 0, Cost(0, 1, 3, 1, 0)),
    Card(Gem.BLUE, 0, Cost(0, 0, 0, 0, 3)),
    Card(Gem.BLUE, 0, Cost(1, 0, 1, 2, 1)),
    Card(Gem.BLUE, 0, Cost(1, 0, 2, 2, 0)),
    Card(Gem.BLUE, 1, Cost(0, 0, 0, 4, 0)),
    Card(Gem.BLUE, 0, Cost(1, 0, 1, 1, 1)),

    # Green cards
    Card(Gem.GREEN, 0, Cost(0, 0, 0, 3, 0)),
    Card(Gem.GREEN, 1, Cost(0, 0, 0, 0, 4)),
    Card(Gem.GREEN, 0, Cost(0, 2, 0, 2, 0)),
    Card(Gem.GREEN, 0, Cost(2, 1, 0, 0, 0)),
    Card(Gem.GREEN, 0, Cost(1, 3, 1, 0, 0)),
    Card(Gem.GREEN, 0, Cost(1, 1, 0, 1, 1)),
    Card(Gem.GREEN, 0, Cost(0, 1, 0, 2, 2)),
    Card(Gem.GREEN, 0, Cost(1, 1, 0, 1, 2)),

    # Red cards
    Card(Gem.RED, 0, Cost(3, 0, 0, 0, 0)),
    Card(Gem.RED, 1, Cost(4, 0, 0, 0, 0)),
    Card(Gem.RED, 0, Cost(1, 1, 1, 0, 1)),
    Card(Gem.RED, 0, Cost(2, 0, 1, 0, 2)),
    Card(Gem.RED, 0, Cost(0, 2, 1, 0, 0)),
    Card(Gem.RED, 0, Cost(2, 1, 1, 0, 1)),
    Card(Gem.RED, 0, Cost(2, 0, 0, 2, 0)),
    Card(Gem.RED, 0, Cost(1, 0, 0, 1, 3)),

    # Black cards
    Card(Gem.BLACK, 1, Cost(0, 4, 0, 0, 0)),
    Card(Gem.BLACK, 0, Cost(0, 0, 3, 0, 0)),
    Card(Gem.BLACK, 0, Cost(2, 0, 2, 0, 0)),
    Card(Gem.BLACK, 0, Cost(2, 2, 0, 1, 0)),
    Card(Gem.BLACK, 0, Cost(0, 0, 2, 1, 0)),
    Card(Gem.BLACK, 0, Cost(0, 0, 1, 3, 1)),
    Card(Gem.BLACK, 0, Cost(1, 2, 1, 1, 0)),
    Card(Gem.BLACK, 0, Cost(1, 1, 1, 1, 0)),
]


def compute_card_stats(cards, gem):
    count = 0
    points = 0
    whites = 0
    blues = 0
    greens = 0
    reds = 0
    blacks = 0

    for card in cards:
        if card.gem == gem:
            count += 1
            points += card.point
            whites += card.cost.white
            blues += card.cost.blue
            greens += card.cost.green
            reds += card.cost.red
            blacks += card.cost.black

    print("Gem " + str(gem) + ":")
    print("    points: " + str(points/count))
    print("    whites: " + str(whites/count))
    print("    blues: " + str(blues/count))
    print("    greens: " + str(greens/count))
    print("    reds: " + str(reds/count))
    print("    blacks: " + str(blacks/count))


def run():
    for gem in Gem:
        compute_card_stats(level_one_cards, gem)


if __name__ == '__main__':
    run()
