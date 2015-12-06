import pystan
import numpy
import cPickle

f = open('2_man_14_15.data')
nba_data = cPickle.load(f)
f.close()

player1 = nba_data[0] 
player2 = nba_data[1]
points = nba_data[2]
minutes = nba_data[3]
players = nba_data[4]
index_to_players = nba_data[5]

print 'Number of players: '+str(len(players))
print 'Size of data set: '+str(len(player1))

#Normalizing minutes
floor = 1
maximum = max(minutes) + floor
normalized_minutes = [i+floor/maximum for i in minutes]

#Describing the Model
nba_code = """
        data {
            int<lower=0> N; // number of data items
            int<lower=0> T; // total number of players
            int<lower=0> K; // number of predictors
            int player1[N]; // first player
            int player2[N]; // second player
            vector[N] y; // outcome vector
            vector[N] mins; //minutes vector
        }
        parameters {
            real alpha; // intercept
            matrix[T,K] players; // latent space describing players
            real<lower=0> sigma; // error scale
        }
        model {
        for (n in 1:N)
            y[n] ~ normal(alpha+players[player1[n]]*players[player2[n]]', sigma/mins[n]); // likelihood
        }
    """
nba_dat = {'N': len(player1),'T': len(players),'K': 100,
           'y': points,'player1':player1,'player2':player2,'mins':minutes}

fit = pystan.stan(model_code=nba_code, data=nba_dat,iter=100, chains=1)
params = fit.extract(permuted=True)
save_items = [fit,params]
sf = open('14_15_nomin_pystan.fit','wb')
cPickle.dump(fit, save_items, protocol=cPickle.HIGHEST_PROTOCOL)
sf.close()

