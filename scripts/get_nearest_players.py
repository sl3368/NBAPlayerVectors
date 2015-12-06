import numpy
import cPickle
import sys

def get_nearest_players(player_string,dictionary,vectors,num_nearest):
	#search for player in index
	for key in dictionary.keys():
		if dictionary[key]==player_string:
			player_index = key
	
	if player_index==None:
		print "Player "+player_string+" not found!"
		sys.exit(0)
		

	#get the vector
	player_vector = vectors[player_index]

	nearest_players = []
	#populate list
	for i in range(len(vectors)):
		if not i==player_index:
			distance = numpy.dot(player_vector,numpy.transpose(vectors[i]))
			nearest_players.append((distance,dictionary[i]))

	#sort the list
	nearest_players.sort(key=lambda tup:tup[0])
    nearest_players.reverse()

	return nearest_players[:num_nearest]
