"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Fixed !

score = float(input("Enter score: "))
if 100 > score < 0:
    print("Invalid score")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("passable")
else:
    print("bad")
