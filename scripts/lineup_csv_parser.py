import cPickle
import sys
from os import path
import os


## Script for parsing basketball-reference.com CSV file dumps

### Run as:
### python linup_csv_parser.py [directory] [output_file]

filename = sys.argv[1]
savefilename = sys.argv[2]

print len(os.listdir(filename))
for afile in os.listdir(filename):
    f = open(filename+afile)
    entries = []
    for line in f:
        line = line.rstrip('\n')
        atts = line.split(',')
        if atts[0].isdigit():
            entries.append(atts)
    f.close()
    
    if path.isfile(savefilename):
        prev = open(savefilename)
        previous_entries = cPickle.load(prev)
        prev.close()
    else:
        previous_entries = []
    
    if len(previous_entries) == 0:
        previous_entries = entries
    else:
        for entry in entries:
           previous_entries.append(entry)

    wf = open(savefilename,'wb')
    cPickle.dump(previous_entries, wf, protocol=cPickle.HIGHEST_PROTOCOL)
    wf.close()
print 'finished'
