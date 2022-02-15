import random
import time
from random import choice

# used variables
firstTotal = []
secondTotal = []
balls = ['YORKER', 'FULL TOSS', 'GOOGLY', 'LENGTH BALL', 'CARROM BALL', 'SLOWER BALL', 'INSWINGER', 'LEG CUTTER', 'OFF CUTTER', 'KNUCKLE BALL']
out = ['RUN OUT !!!', 'CATCH OUT!!!']

# Choosing team
print('Choose both your teams from following IPL teams list \n')
teams = {'CSK': ['Shane Watson', 'Ambati Raydu', 'Suresh Raina', 'MS Dhoni','Kedar Jadhav', 'Ravinder Jadeja','Dwayne Bravo','Imran Tahir', 'Deepak Chahar', 'Harbhajan Singh', 'Shardul Thakur'],
        'MI': ['Rohit Sharma',  'Quinton de Kock', 'Suryakumar Yadav', 'Kieron Pollard','Yuvraj Singh', 'Hardik Pandya', 'Krunal Pandya', 'Ben Cutting', 'Mitchel McClenaghan', ' Rasikh Salam', ' Jasprit Bumrah'],
        'DC': ['Prithvi Shaw', 'Shikhar Dhawan', 'Shreayas Iyer', ' Colin Ingram', 'Rishabh Pant', 'Keemo Paul', 'Axar Patel', 'Rahul Tewatia','Kagiso Rabada', 'Trent Boult', 'Ishant Sharma'],
        'SRH': ['David Warner', 'Johny Bairstow', 'Kane Williamson', 'Manish Pandey', 'Yusuf Pathan','Vijay Shankar', 'Rashid Khan', 'Bhuvneshvar Kumar', 'Shahbaz Nadeem', 'Sandeep Sharma', 'Siddarth Kaul'],
        'KXIP': ['Lokesh Rahul', 'Chris Gayle', 'Mayank Agarwal', 'Sarafraz Khan','Mandeep Singh', 'Nicholas Pooran', 'Sam Curran', 'Ravichandran Ashwin', 'Mohammad Shami', 'Mujeeb Ur Rahman', 'Ankit Rajpoot'],
        'KKR': ['Chris Lynn', 'Nitish Rana', 'Robin Uthappa', 'Dinesh Kartik', 'Shubman Gill','Andre Russell', 'Sunil Narine', 'Piyush Chawla', 'Kuldeep Yadav', 'Lokie Fegurson', 'Prasidh Krishna'],
        'RCB': ['Virat Kohli', 'Parthiv Patel', 'AB De Villiers', 'Shimron Hetmyer','Moeen Ali', 'Shivam Dube', 'Colin De Grandhomme','Navdeep Saini', 'Yujvendra Chahal', 'Umesh Yadav', 'Mohammad Siraj'],
        'RR': ['Ajinkya Rahane', 'Jos Buttler', 'Sanju Samson', 'Steven Smith', 'Rahul Tripathi','Ben Stokes', 'Krinappa Gowtham', 'Jofra Archer', 'Jaydev Unadkat', 'Shreyas Gopal', 'Dhawal Kulkarni']}

keys = teams.keys()  # key = 'teamName'
for keys in teams:
    print(keys)


def select_team(team):
    if team in teams:
        selected_team = team
        return selected_team
    else:
        selected_team = str(input("\nEnter your choice from above mentioned teams only : ")).upper()
        return selected_team


first_team = str(input("\nEnter 1st team choice :")).upper()
firstTeam = select_team(first_team)
second_team = str(input("Enter 2nd team choice :")).upper()
secondTeam = select_team(second_team)
if secondTeam == firstTeam:
    print("This team is already chosen by your opponent!!!! Please choose another team")
    secondTeam = str(input("Enter 2nd team choice :")).upper()
    select_team(secondTeam)
else:
    pass

print(f'\nFirst team is {firstTeam}')
print(f'Second team is {secondTeam}')

players = [firstTeam, secondTeam]
print('\nLETS PLAY CRICKET !!!')

# toss time
print('TOSS TIME!!!!!')
print(f'\n{firstTeam} , What is your call??')
print('HEADS OR TAILS')
tossCall = ['HEADS', 'TAILS']
batBall = ['BAT', 'BOWL']
toss = input('').upper()

while toss:
    if toss in tossCall:
        print(f'\n{toss} is the call')
        random.shuffle(tossCall)
        print(f'\nIt is {tossCall[0]}')
        break
    else:
        print('\nType correctly')
        toss = input('').upper()
        continue


def toss_time(team1, team2):
    print(f'{team1} won the toss. What would you like to do? Bat or Bowl??')
    call = input('').upper()
    try:
        if call not in batBall:
            print('Type correctly!!')
            call = input('').upper()
    finally:
        print(f'{team1} chose to {call} first')
        if call == 'BAT':
            batting_team, bowling_team = teams[team1], teams[team2]
            return batting_team, bowling_team
        elif call == 'BOWL':
            batting_team, bowling_team = teams[team2], teams[team1]
            return batting_team, bowling_team


def innings(batting_team, bowling_team, first_scores):
    batting_team_list = teams[batting_team]
    batting_options = iter(batting_team_list)
    on_strike = next(batting_options)
    on_strike_scores = []
    player_scores = []
    wickets = 10
    total = []
    team_total = 0
    bowling_options = teams[bowling_team][5:]

    for over in range(0, 3):
        bowler = choice(bowling_options)
        print(f'{on_strike} is on strike, {bowler} is bowling.')
        print('Press any key to respond. \n')
        for ball in range(1, 7):
            ball_delivered = choice(balls)
            played_for = choice(balls)
            if wickets == 0 or team_total > first_scores:
                break
            elif ball_delivered == played_for:
                print(f'\n {over}.{ball}')
                print(f'\n LBW !!!  {bowler} has taken the wicket of {on_strike}')
                player_scores = sum(on_strike_scores)
                team_total = sum(total)
                out_player_scores = {on_strike: player_scores}
                print(f'{batting_team} is at {team_total}')
                print(out_player_scores)
                on_strike = next(batting_options)
                print(f'{on_strike} is on strike\n')
                wickets -= 1
                on_strike_scores = [0]
                time.sleep(2)
            else:
                print(f'{over}.{ball}', end='')
                start = time.time()
                input('')
                end = time.time()
                time_taken = end - start
                if time_taken < 1:
                    print('A sixxxxerrrr!!  ')
                    total.append(6)
                    on_strike_scores.append(6)
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    if team_total > first_scores:
                        break
                elif (time_taken > 1) and (time_taken < 1.5):
                    print('Boundaryyy!!!')
                    total.append(4)
                    on_strike_scores.append(4)
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    if team_total > first_scores:
                        break
                elif (time_taken > 2) and (time_taken < 2.5):
                    print('only 2 runs')
                    total.append(2)
                    on_strike_scores.append(2)
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    if team_total > first_scores:
                        break
                elif (time_taken > 2.5) and (time_taken < 3):
                    print(f'{on_strike} duck the ball')
                    total.append(0)
                    on_strike_scores.append(0)
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    if team_total > first_scores:
                        break
                elif ((time_taken > 1.5) and (time_taken < 2)) or time_taken > 3:
                    print(f'{choice(out)} {bowler} has taken the wicket of {on_strike}')
                    player_scores = sum(on_strike_scores)
                    team_total = sum(total)
                    out_player_scores = {on_strike: player_scores}
                    print(f'{batting_team} is at {team_total}')
                    print(out_player_scores)
                    on_strike = next(batting_options)
                    wickets -= 1
                    on_strike_scores = [0]
                    player_scores = [0]

            print(f'{batting_team} is at {team_total}')
            print(f'{on_strike} is at {player_scores}\n')
    return team_total


# game logic
if toss == tossCall[0]:
    toss_time(firstTeam, secondTeam)
    first_innings_total = innings(firstTeam, secondTeam, 1000)  # 1000 is just a big score to compare 1st innings scores
    print(f'{secondTeam} needs {first_innings_total} scores to win the match')
    second_innings_total = innings(secondTeam, firstTeam, first_innings_total)
    if first_innings_total > second_innings_total:
        print(f'{firstTeam} has won the match')
    elif second_innings_total > first_innings_total:
        print(f'{secondTeam} has won the match')
    elif first_innings_total == second_innings_total:
        print('Drawwwww!!!! \n Both teams scored same runs')

if toss == tossCall[1]:
    toss_time(secondTeam, firstTeam)
    first_innings_total = innings(secondTeam, firstTeam, 1000)
    print(f'{firstTeam} needs {first_innings_total} scores to win the match')
    second_innings_total = innings(firstTeam, secondTeam, first_innings_total)
    if first_innings_total > second_innings_total:
        print(f'{firstTeam} has won the match')
    elif second_innings_total > first_innings_total:
        print(f'{secondTeam} has won the match')
    elif first_innings_total == second_innings_total:
        print('Drawwwww!!!! \n Both teams scored same runs')


