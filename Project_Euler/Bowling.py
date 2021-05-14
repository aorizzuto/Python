





#
In the game of ten-pin bowling, a player rolls a bowling ball down a lane to knock over pins. There are ten pins set at the end of the bowling lane. Each player has 10 frames to roll a bowling ball down a lane and knock over as many pins as possible. The first nine frames are ended after two rolls or when the player knocks down all the pins. The last frame a player will receive an extra roll every time they knock down all ten pins; up to a maximum of three total rolls.

The Challenge
In this challenge you will be given a string representing a player's ten frames. It will look something like this: 'X X 9/ 80 X X 90 8/ 7/ 44' (in Java: "X X 9/ 80 X X 90 8/ 7/ 44"), where each frame is space-delimited, 'X' represents strikes, and '/' represents spares. Your goal is take in this string of frames into a function called bowlingScore and return the players total score.


11 11 11 11 11 11 11 11 11 11
None should equal 20
 Log
X X X X X X X X X XXX
None should equal 300
 Log
00 5/ 4/ 53 33 22 4/ 5/ 45 XXX
None should equal 115
 Log
5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8
None should equal 150
 Log
5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 7/2

X 11 09 43 X 35 06 X 50 12
70 should equal 85
 81 22 81 2/ 70 72 3/ 63 43 53
102 should equal 95
 90 35 8/ 2/ 05 36 4/ 23 51 53
110 should equal 84
 23 31 27 41 53 14 08 X 35 34
69 should equal 77
 62 80 15 50 60 24 21 80 09 XX1
59 should equal 80
 X 03 11 90 X X X X 22 XXX
68 should equal 157
 81 45 X X 50 X 61 X 60 1/X
76 should equal 129
 51 42 71 81 6/ 9/ 8/ 3/ 10 12
113 should equal 94
 06 04 X 1/ 9/ 17 13 60 7/ 34
105 should equal 98
 62 7/ 44 07 81 60 90 04 72 12
83 should equal 77
 8/ 9/ 07 9/ 16 43 31 51 8/ 1/X
91 should equal 102
 81 7/ 8/ 45 09 5/ 30 90 22 53

def bowling_score(frames):

    score_per_frames = []
    score = 0
    save = 0
    print(frames)
    for i in frames.split(' '):
        spare = strike = False
        
        if i == 'X':
            st_sr_none = 1
        elif '/' in i:
            st_sr_none = 2
        elif 'X' in i: # XXX or xxx case
            st_sr_none = 3
        else:
            st_sr_none = 4
        
        if st_sr_none == 2:
            score += int(i[0])+10
        else:
            score += int(i[0])+int(i[1])
            score_per_frames.append(score)
            score = 0
    
    return sum(score_per_frames)
        





















