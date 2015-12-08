import numpy
from numpy import random
import cPickle
import pystan
import sys

def create_2man_sim_data(N,T,K,filename,players_filename):
	
    #create random player matrix
    player_mat = numpy.ones((T,K)).astype('f')
    
    #populate players_matrix
    for i in range(T):
    	for k in range(K):
    		player_mat[i,k] = random.random_integers(-100,100) * random.rand(1)
    
    #generative process
    #draw two players, make sure not the same, then dot product
    #draw an alpha,sigma value, and a minutes value 
    
    alpha = random.random_integers(-100,100) * random.rand(1)
    sigma = random.random_integers(-100,100) * random.rand(1)	
    
    player1= []
    player2= []
    points= numpy.zeros((N,))
    mins= numpy.zeros((N,))
    
    for i in range(N):
        p1 = random.random_integers(0,T-1)
        p2 = random.random_integers(0,T-1)
        while(p1==p2):
        	p2 = random.random_integers(0,T-1)
        min_played = random.rand(1)
        pts = (alpha+numpy.dot(player_mat[p1],numpy.transpose(player_mat[p2]))) + (sigma/min_played)*random.randn()
         
        #append generations
        player1.append(p1)
        player2.append(p2)
        points[i]=pts
        mins[i]=min_played

    #create the dictionary
    sim_data = { "N" : N, "K":K, "T":T,"player1":player1,"player2":player2,"y":points,"mins":mins}
    
    #create R dump
    pystan.misc.stan_rdump(sim_data,filename)
    
    #save original vals
    sim_params = [player_mat,alpha,sigma]
    f = open(players_filename,'wb')
    cPickle.dump(sim_params,f)
    f.close()
    
    print "Simulation Complete"

if __name__=="__main__":
	N = int(sys.argv[1])
	T = int(sys.argv[2])
	K = int(sys.argv[3])
	filename = sys.argv[4]
	players_filename = sys.argv[5]
	
	create_2man_sim_data(N,T,K,filename,players_filename)
	

