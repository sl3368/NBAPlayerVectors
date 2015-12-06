import cPickle
import numpy
import sys
from sets import ImmutableSet
import pystan

## Script for taking parsed objects and extracting relavent data for 
## probabilisitic models

### FOR 3 MAN LINEUPS
### Command line arguments [object_path] [output_path] [rdump_path] [K vector length]

filename = sys.argv[1]
savefilename = sys.argv[2]
rdump_fn = sys.argv[3]
k_size = int(sys.argv[4])

f = open(filename)
data = cPickle.load(f)
f.close()

players = []
player1 = []
player2 = []
player3 = []
points_val = []
minutes_val = []

for lineup in data:
    names = lineup[1].split(' | ')
    if lineup[3]=='2014-15':
        if len(names)==3:
            if len(lineup[19])>0:
                if len(lineup[5])>0:
                    for name in names:
                        if name not in players:
                            players.append(name)
        
                    #make the set
                    two_men = [players.index(name) for name in names]
                    player1.append(two_men[0]+1)
                    player2.append(two_men[1]+1)
                    player3.append(two_men[2]+1)
                    points_val.append(float(lineup[19]))
                    minutes_val.append(float(lineup[5]))

#normalize minutes
max_mins = max(minutes_val)
max_mins = max_mins+1
max_mins_norm = [(m+1)/max_mins for m in minutes_val]

index_to_player_dict = {}
for i,val in enumerate(players):
    index_to_player_dict[i]=val

print 'Number of data points: '+str(len(player1))
print 'Total number of plyaers: '+str(len(players))
    
save_data = [player1,player2,player3,points_val,minutes_val,players,index_to_player_dict]
sf = open(savefilename,'wb')
cPickle.dump(save_data,sf, protocol=cPickle.HIGHEST_PROTOCOL)
sf.close()

data_dict = { "N":len(player1), "T":len(players), "K":k_size, "player1":player1, "player2":player2, "player3":player3, "y":points_val, "mins":max_mins_norm }

pystan.misc.stan_rdump(data_dict,rdump_fn)
