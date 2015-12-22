import sklearn
import numpy
import cPickle
from sklearn.manifold import TSNE
import sys
import os

filename = sys.argv[1]
savefilename = sys.argv[2]
no_players = int(sys.argv[3])
vector_size = int(sys.argv[4])

k = []
i=0
with open(filename) as f:
    for line in f:
        if i<6:
            k.append(line.rstrip('\n').split(','))
        i=i+1
print 'Done parsing csv'
mean_alpha = numpy.array(k[5][1]).astype('f')
mean_sigma = numpy.array(k[5][-1]).astype('f')
mean_data = numpy.array(k[5][2:-1]).astype('f')
mean_data = mean_data.reshape((vector_size,no_players))
mean_data = mean_data.transpose()

tsne_model = TSNE()
transformed_space = tsne_model.fit_transform(mean_data)

output = [mean_data,transformed_space,mean_alpha,mean_sigma]
sf = open(savefilename,'wb')
cPickle.dump(output, sf, protocol=cPickle.HIGHEST_PROTOCOL)
sf.close()

os.remove(filename)
