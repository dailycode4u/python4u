import random, sys, time

ranking = [0, 0, 0]
wincounter = 0
losscounter = 0
wongames = ranking[0]
lostgames = ranking[1]
while True:
    ans = input("Rock Paper Scissors? or type q to quit => ")
    if ans == 'q':
        sys.exit()

    ans2 = random.choice(['rock', 'paper', 'scissors'])

    if ans != ans2:
        losscounter += 1
        ranking[1]=losscounter
        lostgames = ranking[1]
        outcome = "Sorry, Try again. \n Won=> " + str(wongames) + " Lost=> " + str(lostgames)

        with open('rps_result', 'w') as f:
            f.write('\n')
            f.write(outcome)
            time.sleep(random.randint(0, 0))
            print(outcome)
            print('Lost Games', lostgames)
            print('Won games ', wongames)


    else:
        wincounter += 1
        ranking[0]=wincounter
        wongames = ranking[0]
        outcome2 = "Winner Winner Chicken Dinner! \n Won " + str(wongames) + " Lost=> " + str(lostgames)
        with open('rps_result', 'w') as f:
            f.write('\n')
            f.write(outcome2)
            time.sleep(random.randint(0, 0))
            print(outcome2)
            print('Lost Games', lostgames)
            print('Won games', wongames)
