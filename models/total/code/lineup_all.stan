data {
    int<lower=0> N; // number of data items
    int<lower=0> T; // total number of players
    int<lower=0> K; // number of predictors
    int player2_1[N]; // 2man-first player
    int player2_2[N]; // 2man-second player
    int player3_1[N]; // 3man-first player
    int player3_2[N]; // 3man-second player
    int player3_3[N]; // 3man-third player
    int player4_1[N]; // 4man-first player
    int player4_2[N]; // 4man-second player
    int player4_3[N]; // 4man-third player
    int player4_4[N]; // 4man-fourth player
    int player5_1[N]; // 5man-first player
    int player5_2[N]; // 5man-second player
    int player5_3[N]; // 5man-third player
    int player5_4[N]; // 5man-fourth player
    int player5_5[N]; // 5man-fifth player
    vector[N] y_2; // 2man-outcome vector
    vector[N] mins_2; //2man-minutes vector
    vector[N] y_3; // 3man-outcome vector
    vector[N] mins_3; //3man-minutes vector
    vector[N] y_4; // 4man-outcome vector
    vector[N] mins_4; //4man-minutes vector
    vector[N] y_5; // 5man-outcome vector
    vector[N] mins_5; //5man-minutes vector

}
parameters {
    real alpha; // intercept
    matrix[T,K] players; // latent space describing players
    real<lower=0> sigma; // error scale
}
model {
    real mu_3;
    real mu_4;
    real mu_5;
    for (n in 1:N){
        mu_3 <- 0;
        mu_4 <- 0;
        mu_5 <- 0;
        for (k in 1:K) {
            mu_5 <- mu_5 + players[player1[n],k]*players[player2[n],k]*players[player3[n],k]*players[player4[n],k]*players[player5[n],k];
        }
        y[n] ~ normal(alpha+mu, sigma); // likelihood
    }
}
