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
