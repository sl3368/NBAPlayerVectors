import subprocess
import sys
import cPickle
import numpy
import os

## USAGE python run_cv.py [cv_directory] [savefilename] [num folds] [number of players] [vector length]

directory = sys.argv[1]
savefilename = sys.argv[2]
folds = int(sys.argv[3])
num_players = int(sys.argv[4])
vector_length = int(sys.argv[5])

mean_err = []
mean_scld_err = []
mean_pct_err = []
mean_scld_pct_err = []

fold_err = []
fold_scld_err = []
fold_pct_err = []
fold_scld_pct_err = []
fold_pts = []
fold_mins = []

## For each fold
for k in range(folds):
    print "PERFORMING INFERENCE ON "+str(k)+" FOLD...."    
    training_fn_string = directory+"CV/training/"+str(k)+"_fold_"+str(vector_length)+".data.R"   
 
    ## Perform SVI
    subprocess.call(["./code/lineup_4man","variational","data","file="+training_fn_string])
    
    ## Process Inference
    subprocess.call(["python","process_inference.py","output.csv","results/tmp/cv_tmp_file.save",str(num_players),str(vector_length)])
    
    ## Load the testing data
    f = open(directory+"CV/testing/"+str(k)+"_fold_test_"+str(vector_length)+".data")
    test_data = cPickle.load(f)
    f.close()

    player1_test = test_data[0]
    player2_test = test_data[1]
    player3_test = test_data[2]
    player4_test = test_data[3]
    mins_test = test_data[4]
    pts_test = test_data[5]
    
    
    ## Load latent vectors
    f = open("results/tmp/cv_tmp_file.save")
    inferred = cPickle.load(f)
    f.close()
    
    mean_vecs = inferred[0]
    mean_alpha = inferred[2]
    mean_sigma = inferred[3]

    specific_mean_err = []
    specific_mean_scld_err = []
    specific_mean_pct_err = []
    specific_mean_scld_pct_err = []

    for i in range(20):
         
        for t in range(len(player1_test)):

            ## compute product of vectors
            vector_sum = 0
            for i in range(vector_length):
                vector_sum = vector_sum + mean_vecs[player1_test[t]][i] + mean_vecs[player2_test[t]][i] + mean_vecs[player3_test[t]][i] + mean_vecs[player4_test[t]][i]

            ## compute the value of the lineup
            predicted_pts = numpy.random.normal(mean_alpha+vector_sum,mean_sigma/mins_test[t])
            clipped_predicted_pts = numpy.clip(predicted_pts,-1000000,1000000)

            ## compute the error
            diff = abs(clipped_predicted_pts-pts_test[t])
            fold_err.append(diff)     
            specific_mean_err.append(diff)
            
            ## scaled error
            scld_err = diff * mins_test[t]* mins_test[t]
            fold_scld_err.append(scld_err)
            specific_mean_scld_err.append(scld_err)

            ## percent error
            pct_err = diff/(abs(pts_test[t])+.1)
            fold_pct_err.append(pct_err)
            specific_mean_pct_err.append(pct_err)
            
            ## scaled percent error
            pct_err_scld = pct_err * mins_test[t]* mins_test[t]
            fold_scld_pct_err.append(pct_err_scld)
            specific_mean_scld_pct_err.append(pct_err_scld)
 
            ## real vals
            fold_pts.append(pts_test[t])
            fold_mins.append(mins_test[t])
            
            ## Compute held out log probability
            

    ## remove temporary file
    os.remove("results/tmp/cv_tmp_file.save")

    ## add mean to fold result
    mean_err.append(numpy.mean(specific_mean_err))
    mean_scld_err.append(numpy.mean(specific_mean_scld_err))
    mean_pct_err.append(numpy.mean(specific_mean_pct_err))
    mean_scld_pct_err.append(numpy.mean(specific_mean_scld_pct_err))


## Print out results
print "Across all folds results..."
print "Mean Error: "+str(numpy.mean(mean_err))
print "Mean Scaled Error: "+str(numpy.mean(mean_scld_err))
print "Mean Percent Error: "+str(numpy.mean(mean_pct_err))
print "Mean Scaled Percent Error: "+str(numpy.mean(mean_scld_pct_err))

## Save data
print "\n\nSavng data..."
saving_data = [fold_err,fold_scld_err,fold_pct_err,fold_scld_pct_err,fold_mins,fold_pts,mean_err,mean_scld_err,mean_pct_err,mean_scld_pct_err]
sf = open(savefilename,'wb')
cPickle.dump(saving_data, sf, protocol=cPickle.HIGHEST_PROTOCOL)
sf.close()
print "Finished..."
