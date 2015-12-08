import sys
import cPickle
import pystan
import numpy

## USAGE python 2man_cross_validation.py [filename] [directory_name] [K_value]

filename = sys.argv[1]
directory = sys.argv[2]
k_val = int(sys.argv[3])

FOLDS = 10
split = .9

## LOAD THE WHOLE DATA

f = open(filename)
data = cPickle.load(f)
f.close()

player1 = data[0]
player2 = data[1]
player3 = data[2]
player4 = data[3]
player5 = data[4]
pts = data[5]
norm_mins = data[6]
all_players = data[7]
N = len(player1)
split_idx = int(split*N)

## FOR EACH FOLD
for k in range(FOLDS):
    
    ## INITIALIZE TRAINING AND TESTING VARIABLES
    tr_player1 = []
    tr_player2 = []
    tr_player3 = []
    tr_player4 = []
    tr_player5 = []
    tr_mins = []
    tr_pts = []

    ts_player1 = []
    ts_player2 = []
    ts_player3 = []
    ts_player4 = []
    ts_player5 = []
    ts_mins = []
    ts_pts = []
    
    
    all_idx = range(N)
    numpy.random.shuffle(all_idx)
    tr_idx,ts_idx = all_idx[:split_idx],all_idx[split_idx:]

    # BUILD TRAINING AND TEST SETS
    for i in tr_idx:
        tr_player1.append(player1[i])
        tr_player2.append(player2[i])
        tr_player3.append(player3[i])
        tr_player4.append(player4[i])
        tr_player5.append(player5[i])
        tr_mins.append(norm_mins[i])
        tr_pts.append(pts[i])
    
    for i in ts_idx:
        ts_player1.append(player1[i]-1)
        ts_player2.append(player2[i]-1)
        ts_player3.append(player3[i]-1)
        ts_player4.append(player4[i]-1)
        ts_player5.append(player5[i]-1)
        ts_mins.append(norm_mins[i])
        ts_pts.append(pts[i])

    
    # SAVE TRAINING DATA IN THE CORRECT FORMAT
    data_dict = { "N":len(tr_player1), "T":len(all_players), "K":k_val, "player1":tr_player1, "player2":tr_player2, "player3":tr_player3, "player4":tr_player4, "player5":tr_player5, "y":tr_pts, "mins":tr_mins }
    pystan.misc.stan_rdump(data_dict,directory+"CV/training/"+str(k)+"_fold_"+str(k_val)+".data.R")

    # SAVE THE TESTING DATA
    testing_data = [ts_player1,ts_player2,ts_player3,ts_player4,ts_player5,ts_mins,ts_pts]
    sf = open(directory+"CV/testing/"+str(k)+"_fold_test_"+str(k_val)+".data",'wb')
    cPickle.dump(testing_data,sf, protocol=cPickle.HIGHEST_PROTOCOL)
    sf.close()
