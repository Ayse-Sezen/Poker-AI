avgAmtWon = 0
avgAmtLost = 0
totalNumberOfGames = 0

x = 0

fp = open('amountWon.txt', 'r')
lines = fp.readlines()
totalNumberOfGames = len(lines)

for i in range (0, totalNumberOfGames):
    x += int(lines[i])

avgAmtWon = x / totalNumberOfGames
print("Average Amount won: ", round(avgAmtWon))
    
fp.close()
x = 0

fp2 = open('amountLost.txt', 'r')
lines = fp2.readlines()
totalNumberOfGames = len(lines)
for i in range(0, totalNumberOfGames):
    x += int(lines[i])
avgAmtLost = x / totalNumberOfGames
print("Average Amount lost: ", round(avgAmtLost))
    
         
