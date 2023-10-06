from collections import defaultdict

def GM():  # get multiple ints
    return map(int, input().split())

n, k, c = GM() #number of teams in comp, teams that will advance, limit on teams from any school
winners = dict()
schools = defaultdict(int)
teams = []

#this list is alr in order by ranking
for i in range(n):
    teams.append(tuple(GM())) #id, school
    winners[teams[i][0]] = False

rank = 0
wins = 0
limit = True
while (wins != k): #while there are still teams to check and not enough winners
    if rank == n:
        rank = 0
        limit = False
    if limit and schools[teams[rank][1]] < c: #if school has not reached limit
            winners[teams[rank][0]] = True #set team to winners
            schools[teams[rank][1]] += 1 #increment school count
            wins += 1 #increment winners
    if not limit:
        if not winners[teams[rank][0]]:
            winners[teams[rank][0]] = True
            wins += 1
    rank += 1 #move to next team


for i in range(n):
    #print(winners[teams[i][0]])
    if winners[teams[i][0]]:
        print(teams[i][0])