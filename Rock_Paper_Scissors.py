import random
import time

# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message):
    print(message)
    time.sleep(.25)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def scores(score1, score2):
    if score1 > score2:
        print_pause("Sorry you lost! Better luck next time!")
    elif score2 > score1:
        print_pause("Congrats! You are a winner!!!")
    else:
        print_pause("TIE!")


def play_again():
    response = input("Play again?(Yes or no?)\n").lower()
    if "yes" in response:
        game.play_game()
    elif "no" in response:
        pass
    else:
        play_again()


class Player:

    score = 0

    def __inite__(self):
        pass

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.name = "Computer Friend"
        self.opponent_move = None
        self.player_move = None

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        if beats(my_move, their_move) is True:
            print_pause(f"Yay, {self.name} wins!!")
            self.score += 1
        self.opponent_move = their_move
        self.player_move = my_move


class ReflectPlayer(RandomPlayer):
    def move(self):
        if self.opponent_move is None:
            return super().move()
        else:
            return self.opponent_move


class CyclePlayer(RandomPlayer):

    def move(self):
        if self.player_move is None:
            return super().move()
        else:
            move_index = moves.index(self.player_move)
            move_index += 1
            if move_index == 3:
                move_index = 0
            return moves[move_index]


class Player2(Player):
    def __init__(self):
        self.name = "human"

    def move(self):
        while True:
            move = input("Rock, paper, scissors?\n").lower()
            if move in moves:
                return move

    def learn(self, my_move, their_move):
        if beats(my_move, their_move) is True:
            print_pause(f"Yay, {self.name} wins!!")
            self.score += 1
        self.opponent_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print_pause("Tie!")
        print_pause(f"Player1:{self.p1.score} \t Player2:{self.p2.score}")

    def play_game(self):
        print_pause("Game start!")
        for round in range(1, 4):
            print_pause(f"Round {round}:")
            self.play_round()
        print_pause("Game over!")
        scores(self.p1.score, self.p2.score)
        print_pause(f"Player1:{self.p1.score} \t Player2:{self.p2.score}")
        play_again()


if __name__ == '__main__':
    game = Game(CyclePlayer(), Player2())
    game.play_game()
