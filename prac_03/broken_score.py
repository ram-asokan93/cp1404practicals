"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = random.randint(0, 100)
    print(evaluate_score(score))


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()