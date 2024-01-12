#ifndef STATISTICS_HDR
#define STATISTICS_HDR

#include <cmath>
#include <iostream>
#include <limits>
#include <string>

class Statistics {
    private:
        std::string name_;
        size_t n_;
        double sum_;
        double sum2_;
        double min_;
        double max_;
        size_t nr_missing_;
        void check() const;
        double sum2() const { check(); return sum2_; };
        double mean2() const { check(); return sum2()/n(); };
    public:
        Statistics() :
            name_ {""}, n_ {0}, sum_ {0.0}, sum2_ {0.0},
            min_ {std::numeric_limits<double>::max()},
            max_ {-std::numeric_limits<double>::max()},
           nr_missing_ {0} {};
        explicit Statistics(const std::string& name) : Statistics() {
            name_ = name;
        };
        const std::string& name() const { return name_; };
        size_t n() const { return n_; };
        void add(const double value);
        void add(const std::string& str);
        double sum() const { check(); return sum_; };
        double min() const { check(); return min_; };
        double max() const { check(); return max_; };
        double mean() const { check(); return sum()/n(); };
        double stddev() const {
            check();
            return sqrt((sum2() - sum()*sum()/n())/(n() - 1));
        };
        size_t nr_missing() const { return nr_missing_; };
        friend std::ostream& operator<<(std::ostream& out,
                                        const Statistics& stats);
};

#endif
