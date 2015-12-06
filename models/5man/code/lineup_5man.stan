data {
    int<lower=0> N; // number of data items
    int<lower=0> T; // total number of players
    int<lower=0> K; // number of predictors
    int player1[N]; // first player
    int player2[N]; // second player
    int player3[N]; // third player
    int player4[N]; // fourth player
    int player5[N]; // fifth player
    vector[N] y; // outcome vector
    vector[N] mins; //minutes vector
}
parameters {
    real alpha; // intercept
    matrix[T,K] players; // latent space describing players
    real<lower=0> sigma; // error scale
}
model {
    real mu;
    for (n in 1:N){
        mu <- 0;
        for (k in 1:K) {
            mu <- mu + players[player1[n],k]*players[player2[n],k]*players[player3[n],k]*players[player4[n],k]*players[player5[n],k];
        }
        y[n] ~ normal(alpha+mu, sigma/mins[n]); // likelihood
    }
}
