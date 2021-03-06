// Code generated by Stan version 2.8

#include <stan/model/model_header.hpp>

namespace lineup_3man_model_namespace {

using std::istream;
using std::string;
using std::stringstream;
using std::vector;
using stan::io::dump;
using stan::math::lgamma;
using stan::model::prob_grad;
using namespace stan::math;

typedef Eigen::Matrix<double,Eigen::Dynamic,1> vector_d;
typedef Eigen::Matrix<double,1,Eigen::Dynamic> row_vector_d;
typedef Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic> matrix_d;

static int current_statement_begin__;
class lineup_3man_model : public prob_grad {
private:
    int N;
    int T;
    int K;
    vector<int> player1;
    vector<int> player2;
    vector<int> player3;
    vector_d y;
    vector_d mins;
public:
    lineup_3man_model(stan::io::var_context& context__,
        std::ostream* pstream__ = 0)
        : prob_grad(0) {
        current_statement_begin__ = -1;

        static const char* function__ = "lineup_3man_model_namespace::lineup_3man_model";
        (void) function__; // dummy call to supress warning
        size_t pos__;
        (void) pos__; // dummy call to supress warning
        std::vector<int> vals_i__;
        std::vector<double> vals_r__;
        context__.validate_dims("data initialization", "N", "int", context__.to_vec());
        N = int(0);
        vals_i__ = context__.vals_i("N");
        pos__ = 0;
        N = vals_i__[pos__++];
        context__.validate_dims("data initialization", "T", "int", context__.to_vec());
        T = int(0);
        vals_i__ = context__.vals_i("T");
        pos__ = 0;
        T = vals_i__[pos__++];
        context__.validate_dims("data initialization", "K", "int", context__.to_vec());
        K = int(0);
        vals_i__ = context__.vals_i("K");
        pos__ = 0;
        K = vals_i__[pos__++];
        context__.validate_dims("data initialization", "player1", "int", context__.to_vec(N));
        validate_non_negative_index("player1", "N", N);
        player1 = std::vector<int>(N,int(0));
        vals_i__ = context__.vals_i("player1");
        pos__ = 0;
        size_t player1_limit_0__ = N;
        for (size_t i_0__ = 0; i_0__ < player1_limit_0__; ++i_0__) {
            player1[i_0__] = vals_i__[pos__++];
        }
        context__.validate_dims("data initialization", "player2", "int", context__.to_vec(N));
        validate_non_negative_index("player2", "N", N);
        player2 = std::vector<int>(N,int(0));
        vals_i__ = context__.vals_i("player2");
        pos__ = 0;
        size_t player2_limit_0__ = N;
        for (size_t i_0__ = 0; i_0__ < player2_limit_0__; ++i_0__) {
            player2[i_0__] = vals_i__[pos__++];
        }
        context__.validate_dims("data initialization", "player3", "int", context__.to_vec(N));
        validate_non_negative_index("player3", "N", N);
        player3 = std::vector<int>(N,int(0));
        vals_i__ = context__.vals_i("player3");
        pos__ = 0;
        size_t player3_limit_0__ = N;
        for (size_t i_0__ = 0; i_0__ < player3_limit_0__; ++i_0__) {
            player3[i_0__] = vals_i__[pos__++];
        }
        validate_non_negative_index("y", "N", N);
        y = vector_d(N);
        context__.validate_dims("data initialization", "y", "vector_d", context__.to_vec(N));
        vals_r__ = context__.vals_r("y");
        pos__ = 0;
        size_t y_i_vec_lim__ = N;
        for (size_t i_vec__ = 0; i_vec__ < y_i_vec_lim__; ++i_vec__) {
            y[i_vec__] = vals_r__[pos__++];
        }
        validate_non_negative_index("mins", "N", N);
        mins = vector_d(N);
        context__.validate_dims("data initialization", "mins", "vector_d", context__.to_vec(N));
        vals_r__ = context__.vals_r("mins");
        pos__ = 0;
        size_t mins_i_vec_lim__ = N;
        for (size_t i_vec__ = 0; i_vec__ < mins_i_vec_lim__; ++i_vec__) {
            mins[i_vec__] = vals_r__[pos__++];
        }

        // validate data
        check_greater_or_equal(function__,"N",N,0);
        check_greater_or_equal(function__,"T",T,0);
        check_greater_or_equal(function__,"K",K,0);

        double DUMMY_VAR__(std::numeric_limits<double>::quiet_NaN());
        (void) DUMMY_VAR__;  // suppress unused var warning


        // initialize transformed variables to avoid seg fault on val access

        try {
        } catch (const std::exception& e) {
            stan::lang::rethrow_located(e,current_statement_begin__);
            // Next line prevents compiler griping about no return
throw std::runtime_error("*** IF YOU SEE THIS, PLEASE REPORT A BUG ***");
        }

        // validate transformed data

        // set parameter ranges
        num_params_r__ = 0U;
        param_ranges_i__.clear();
        ++num_params_r__;
        num_params_r__ += T * K;
        ++num_params_r__;
    }

    ~lineup_3man_model() { }


    void transform_inits(const stan::io::var_context& context__,
                         std::vector<int>& params_i__,
                         std::vector<double>& params_r__,
                         std::ostream* pstream__) const {
        stan::io::writer<double> writer__(params_r__,params_i__);
        size_t pos__;
        (void) pos__; // dummy call to supress warning
        std::vector<double> vals_r__;
        std::vector<int> vals_i__;

        if (!(context__.contains_r("alpha")))
            throw std::runtime_error("variable alpha missing");
        vals_r__ = context__.vals_r("alpha");
        pos__ = 0U;
        context__.validate_dims("initialization", "alpha", "double", context__.to_vec());
        double alpha(0);
        alpha = vals_r__[pos__++];
        try {
            writer__.scalar_unconstrain(alpha);
        } catch (const std::exception& e) { 
            throw std::runtime_error(std::string("Error transforming variable alpha: ") + e.what());
        }

        if (!(context__.contains_r("players")))
            throw std::runtime_error("variable players missing");
        vals_r__ = context__.vals_r("players");
        pos__ = 0U;
        context__.validate_dims("initialization", "players", "matrix_d", context__.to_vec(T,K));
        matrix_d players(T,K);
        for (int j2__ = 0U; j2__ < K; ++j2__)
            for (int j1__ = 0U; j1__ < T; ++j1__)
                players(j1__,j2__) = vals_r__[pos__++];
        try {
            writer__.matrix_unconstrain(players);
        } catch (const std::exception& e) { 
            throw std::runtime_error(std::string("Error transforming variable players: ") + e.what());
        }

        if (!(context__.contains_r("sigma")))
            throw std::runtime_error("variable sigma missing");
        vals_r__ = context__.vals_r("sigma");
        pos__ = 0U;
        context__.validate_dims("initialization", "sigma", "double", context__.to_vec());
        double sigma(0);
        sigma = vals_r__[pos__++];
        try {
            writer__.scalar_lb_unconstrain(0,sigma);
        } catch (const std::exception& e) { 
            throw std::runtime_error(std::string("Error transforming variable sigma: ") + e.what());
        }

        params_r__ = writer__.data_r();
        params_i__ = writer__.data_i();
    }

    void transform_inits(const stan::io::var_context& context,
                         Eigen::Matrix<double,Eigen::Dynamic,1>& params_r,
                         std::ostream* pstream__) const {
      std::vector<double> params_r_vec;
      std::vector<int> params_i_vec;
      transform_inits(context, params_i_vec, params_r_vec, pstream__);
      params_r.resize(params_r_vec.size());
      for (int i = 0; i < params_r.size(); ++i)
        params_r(i) = params_r_vec[i];
    }


    template <bool propto__, bool jacobian__, typename T__>
    T__ log_prob(vector<T__>& params_r__,
                 vector<int>& params_i__,
                 std::ostream* pstream__ = 0) const {

        T__ DUMMY_VAR__(std::numeric_limits<double>::quiet_NaN());
        (void) DUMMY_VAR__;  // suppress unused var warning

        T__ lp__(0.0);
        stan::math::accumulator<T__> lp_accum__;

        // model parameters
        stan::io::reader<T__> in__(params_r__,params_i__);

        T__ alpha;
        (void) alpha;   // dummy to suppress unused var warning
        if (jacobian__)
            alpha = in__.scalar_constrain(lp__);
        else
            alpha = in__.scalar_constrain();

        Eigen::Matrix<T__,Eigen::Dynamic,Eigen::Dynamic>  players;
        (void) players;   // dummy to suppress unused var warning
        if (jacobian__)
            players = in__.matrix_constrain(T,K,lp__);
        else
            players = in__.matrix_constrain(T,K);

        T__ sigma;
        (void) sigma;   // dummy to suppress unused var warning
        if (jacobian__)
            sigma = in__.scalar_lb_constrain(0,lp__);
        else
            sigma = in__.scalar_lb_constrain(0);


        // transformed parameters

        // initialize transformed variables to avoid seg fault on val access

        try {
        } catch (const std::exception& e) {
            stan::lang::rethrow_located(e,current_statement_begin__);
            // Next line prevents compiler griping about no return
throw std::runtime_error("*** IF YOU SEE THIS, PLEASE REPORT A BUG ***");
        }

        // validate transformed parameters

        const char* function__ = "validate transformed params";
        (void) function__; // dummy to suppress unused var warning

        // model body
        try {
            {
                T__ mu;
                (void) mu;  // dummy to suppress unused var warning
                stan::math::initialize(mu, DUMMY_VAR__);
                current_statement_begin__ = 18;
                for (int n = 1; n <= N; ++n) {
                    current_statement_begin__ = 19;
                    stan::math::assign(mu, 0);
                    current_statement_begin__ = 20;
                    for (int k = 1; k <= K; ++k) {
                        current_statement_begin__ = 21;
                        stan::math::assign(mu, (mu + ((get_base1(players,get_base1(player1,n,"player1",1),k,"players",1) * get_base1(players,get_base1(player2,n,"player2",1),k,"players",1)) * get_base1(players,get_base1(player3,n,"player3",1),k,"players",1))));
                    }
                    current_statement_begin__ = 23;
                    lp_accum__.add(normal_log<propto__>(get_base1(y,n,"y",1), (alpha + mu), (sigma / get_base1(mins,n,"mins",1))));
                }
            }
        } catch (const std::exception& e) {
            stan::lang::rethrow_located(e,current_statement_begin__);
            // Next line prevents compiler griping about no return
throw std::runtime_error("*** IF YOU SEE THIS, PLEASE REPORT A BUG ***");
        }

        lp_accum__.add(lp__);
        return lp_accum__.sum();

    } // log_prob()

    template <bool propto, bool jacobian, typename T_>
    T_ log_prob(Eigen::Matrix<T_,Eigen::Dynamic,1>& params_r,
               std::ostream* pstream = 0) const {
      std::vector<T_> vec_params_r;
      vec_params_r.reserve(params_r.size());
      for (int i = 0; i < params_r.size(); ++i)
        vec_params_r.push_back(params_r(i));
      std::vector<int> vec_params_i;
      return log_prob<propto,jacobian,T_>(vec_params_r, vec_params_i, pstream);
    }


    void get_param_names(std::vector<std::string>& names__) const {
        names__.resize(0);
        names__.push_back("alpha");
        names__.push_back("players");
        names__.push_back("sigma");
    }


    void get_dims(std::vector<std::vector<size_t> >& dimss__) const {
        dimss__.resize(0);
        std::vector<size_t> dims__;
        dims__.resize(0);
        dimss__.push_back(dims__);
        dims__.resize(0);
        dims__.push_back(T);
        dims__.push_back(K);
        dimss__.push_back(dims__);
        dims__.resize(0);
        dimss__.push_back(dims__);
    }

    template <typename RNG>
    void write_array(RNG& base_rng__,
                     std::vector<double>& params_r__,
                     std::vector<int>& params_i__,
                     std::vector<double>& vars__,
                     bool include_tparams__ = true,
                     bool include_gqs__ = true,
                     std::ostream* pstream__ = 0) const {
        vars__.resize(0);
        stan::io::reader<double> in__(params_r__,params_i__);
        static const char* function__ = "lineup_3man_model_namespace::write_array";
        (void) function__; // dummy call to supress warning
        // read-transform, write parameters
        double alpha = in__.scalar_constrain();
        matrix_d players = in__.matrix_constrain(T,K);
        double sigma = in__.scalar_lb_constrain(0);
        vars__.push_back(alpha);
        for (int k_1__ = 0; k_1__ < K; ++k_1__) {
            for (int k_0__ = 0; k_0__ < T; ++k_0__) {
                vars__.push_back(players(k_0__, k_1__));
            }
        }
        vars__.push_back(sigma);

        if (!include_tparams__) return;
        // declare and define transformed parameters
        double lp__ = 0.0;
        (void) lp__; // dummy call to supress warning
        stan::math::accumulator<double> lp_accum__;


        try {
        } catch (const std::exception& e) {
            stan::lang::rethrow_located(e,current_statement_begin__);
            // Next line prevents compiler griping about no return
throw std::runtime_error("*** IF YOU SEE THIS, PLEASE REPORT A BUG ***");
        }

        // validate transformed parameters

        // write transformed parameters

        if (!include_gqs__) return;
        // declare and define generated quantities

        double DUMMY_VAR__(std::numeric_limits<double>::quiet_NaN());
        (void) DUMMY_VAR__;  // suppress unused var warning


        // initialize transformed variables to avoid seg fault on val access

        try {
        } catch (const std::exception& e) {
            stan::lang::rethrow_located(e,current_statement_begin__);
            // Next line prevents compiler griping about no return
throw std::runtime_error("*** IF YOU SEE THIS, PLEASE REPORT A BUG ***");
        }

        // validate generated quantities

        // write generated quantities
    }

    template <typename RNG>
    void write_array(RNG& base_rng,
                     Eigen::Matrix<double,Eigen::Dynamic,1>& params_r,
                     Eigen::Matrix<double,Eigen::Dynamic,1>& vars,
                     bool include_tparams = true,
                     bool include_gqs = true,
                     std::ostream* pstream = 0) const {
      std::vector<double> params_r_vec(params_r.size());
      for (int i = 0; i < params_r.size(); ++i)
        params_r_vec[i] = params_r(i);
      std::vector<double> vars_vec;
      std::vector<int> params_i_vec;
      write_array(base_rng,params_r_vec,params_i_vec,vars_vec,include_tparams,include_gqs,pstream);
      vars.resize(vars_vec.size());
      for (int i = 0; i < vars.size(); ++i)
        vars(i) = vars_vec[i];
    }

    static std::string model_name() {
        return "lineup_3man_model";
    }


    void constrained_param_names(std::vector<std::string>& param_names__,
                                 bool include_tparams__ = true,
                                 bool include_gqs__ = true) const {
        std::stringstream param_name_stream__;
        param_name_stream__.str(std::string());
        param_name_stream__ << "alpha";
        param_names__.push_back(param_name_stream__.str());
        for (int k_1__ = 1; k_1__ <= K; ++k_1__) {
            for (int k_0__ = 1; k_0__ <= T; ++k_0__) {
                param_name_stream__.str(std::string());
                param_name_stream__ << "players" << '.' << k_0__ << '.' << k_1__;
                param_names__.push_back(param_name_stream__.str());
            }
        }
        param_name_stream__.str(std::string());
        param_name_stream__ << "sigma";
        param_names__.push_back(param_name_stream__.str());

        if (!include_gqs__ && !include_tparams__) return;

        if (!include_gqs__) return;
    }


    void unconstrained_param_names(std::vector<std::string>& param_names__,
                                   bool include_tparams__ = true,
                                   bool include_gqs__ = true) const {
        std::stringstream param_name_stream__;
        param_name_stream__.str(std::string());
        param_name_stream__ << "alpha";
        param_names__.push_back(param_name_stream__.str());
        for (int k_1__ = 1; k_1__ <= K; ++k_1__) {
            for (int k_0__ = 1; k_0__ <= T; ++k_0__) {
                param_name_stream__.str(std::string());
                param_name_stream__ << "players" << '.' << k_0__ << '.' << k_1__;
                param_names__.push_back(param_name_stream__.str());
            }
        }
        param_name_stream__.str(std::string());
        param_name_stream__ << "sigma";
        param_names__.push_back(param_name_stream__.str());

        if (!include_gqs__ && !include_tparams__) return;

        if (!include_gqs__) return;
    }

}; // model

} // namespace

typedef lineup_3man_model_namespace::lineup_3man_model stan_model;

