import random

!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    oppLastPlayed = 'rock'
    myLastPlayed = 'rock'

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.oppLastPlayed = their_move
        self.myLastPlayed = my_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return self.oppLastPlayed


class CyclePlayer(Player):
    index = 0

    def __init__(self):
        self.index = random.randint(0, len(moves))
        super().__init__()

    def move(self):
        self.index += 1
        if self.index >= len(moves):
            self.index = 0
        return moves[self.index]


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        isValid = False
        moveToReturn = ""
        while not isValid:
            val = input("Rock, Paper, Scissors?")
            for move in moves:
                if val.lower() == move.lower():
                    isValid = True
                    moveToReturn = move
                    break
        return moveToReturn


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    player1Score = 0
    player2Score = 0

    def __init__(self):
        self.p2 = HumanPlayer()
        self.players = [CyclePlayer(), ReflectPlayer(),
                        RandomPlayer(), Player()]
        self.p1 = random.choice(self.players)

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1} | You: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.player1Score += 1
            print(f"Player 1 wins this round!")
        elif beats(move2, move1):
            self.player2Score += 1
            print(f"You win the round!")
        else:
            print(f"It's a draw.")
        self.printScore()

    def printScore(self):
        print(f"The score thus far:")
        print(f"Player 1: {self.player1Score} | You: {self.player2Score}")

    def scoreGame(self):
        print(f"The final score is:")
        print(f"Player 1: {self.player1Score} | You: {self.player2Score}")
        if self.player1Score > self.player2Score:
            print(f"Player 1 Wins!")
        elif self.player2Score > self.player1Score:
            print(f"You Win!")
        else:
            print(f"It's a tie!")
        response = input("Do you want to play again? ")
        if response.lower() == "yes":
            self.play_game()

    def new_opponent(self):
        self.p1 = random.choice()

    def play_game(self):
        print("Game start!")

        # Reset variables for replay.
        self.player1Score = 0
        self.player2Score = 0
        self.p1 = random.choice(self.players)
        isValidInt = False
        numRounds = input("How many rounds would you like to play? ")

        while not isValidInt:
            try:
                int(numRounds)
                isValidInt = True
            except ValueError:
                numRounds = input("How many rounds would you like to play? ")

        for round in range(int(numRounds)):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over! Let's see how we did...")
        self.scoreGame()


if __name__ == '__main__':
    game = Game()
    game.play_game()
