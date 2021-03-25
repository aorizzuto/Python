

# Project Euler: 54
"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

from collections import Counter
import time

def euler_54():

  f = open("p054_poker.txt")

  p1 = []
  p2 = []
  
  print("--------------")
  for i in f.readlines():
    p1.append(i[:14])
    p2.append(i[15:-1])

  w1,w2 = check_wins(p1,p2)
  
  return w1,w2




def check_wins(p1,p2):
  
  w1 = w2 = 0
  for i in range(len(p1)):
    j1 = check_cards(p1[i])
    j2 = check_cards(p2[i])

    if j1 == j2:
      if j1 > 14:
        j1,j2 = check_super_tie(p1[i],p2[i],j1)
      else:
        j1,j2 = check_tie(p1[i],p2[i])
  
    if j1 > j2:
      print(p1[i],j1,"     ",p2[i],j2)
      w1 += 1
    else:
      w2 += 1

  return w1,w2

"""
23: Escalera real
22:  Escalera color
21:  Poker
20:  Full
19:  Color
18:  Escalera
17:  Pierna
16:  Doble par
15:  Par
14:  Cartas
"""

def check_cards(cards):
  c = ['2','3','4','5','6','7','8','9','J','Q','K','A']
  values = [cards[0],cards[3],cards[6],cards[9],cards[12]]
  cont = dict(Counter(values))

  if cards[1]==cards[4]==cards[7]==cards[10]==cards[13]:
    # Escalera real
    if 'T' in cards and 'J' in cards and 'Q' in cards and 'K' in cards and 'A' in cards:
      return 23

    # Escalera color
    x = sorted(values)
    if (x) == c[c.index(x[0]):int(c.index(x[0]))+4]:
      return 22

  # Poker
  if 4 in cont.values():
    return 21
  
  # Full
  if 3 in cont.values() and 2 in cont.values():
    return 20
  
  # Color
  if cards[1]==cards[4]==cards[7]==cards[10]==cards[13]:
    return 19

  # Escalera
  x = sorted(values)
  if (x) == c[c.index(x[0]):int(c.index(x[0]))+5]:
    return 18
  
  # Pierna
  if 3 in cont.values():
    return 17

  # Doble par
  if Counter(sorted(cont.values()))[2] == 2:
    return 16
  
  # Par
  if 2 in cont.values():
    return 15
  
  return 0






def check_tie(cards1,cards2):
 
  values1 = [cards1[0],cards1[3],cards1[6],cards1[9],cards1[12]]
  values2 = [cards2[0],cards2[3],cards2[6],cards2[9],cards2[12]]

  values1 = sorted([int(i) for i in replace_TJQKA(values1)])
  values2 = sorted([int(i) for i in replace_TJQKA(values2)])


  
  for i in range(len(values1)-1,0,-1):
    if values1[i] != values2[i]:
      max_1 = values1[i]
      max_2 = values2[i]
      break
    
  return max_1, max_2






def check_super_tie(cards1,cards2,tie_value):
  values1 = [cards1[0],cards1[3],cards1[6],cards1[9],cards1[12]]
  values2 = [cards2[0],cards2[3],cards2[6],cards2[9],cards2[12]]

  values1 = sorted([int(i) for i in replace_TJQKA(values1)])
  values2 = sorted([int(i) for i in replace_TJQKA(values2)])

  cont1 = dict(Counter(values1))
  cont2 = dict(Counter(values2))

  if tie_value == 15:
    return list(cont1.keys())[list(cont1.values()).index(2)],list(cont2.keys())[list(cont2.values()).index(2)]

  if tie_value == 16:
    return 0,0

  if tie_value == 17:
    return 0,0

  if tie_value == 18:
    return 0,0

  if tie_value == 19:
    return 0,0

  if tie_value == 20:
    return 0,0

  if tie_value == 21:
    return 0,0





def replace_TJQKA(values):
    # Cards
  values = [v.replace('A','14') for v in values]
  values = [v.replace('K','13') for v in values]
  values = [v.replace('Q','12') for v in values]
  values = [v.replace('J','11') for v in values]
  values = [v.replace('T','10') for v in values]

  return values


##############################################

if __name__ == "__main__":

  start=time.time()

  a,b = euler_54()

  print("El jugador 1 ganó {} y el jugador 2 ganó {}".format(a,b))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
l jugador 1 ganó 376 y el jugador 2 ganó 624

Tiempo de operación: 0.10389041900634766 seg.
"""

