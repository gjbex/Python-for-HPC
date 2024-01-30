#include "statistics.h"

void Statistics::check() const {
    if (n() == 0) {
        std::cerr << "### error: no values for statistics" << std::endl;
        std::exit(10);
    }
}

void Statistics::add(const double value) {
    n_++;
    sum_ += value;
    sum2_ += value*value;
    if (value < min())
        min_ = value;
    if (value > max())
        max_ = value;
}

void Statistics::add(const std::string& str) {
    try {
        double value {std::stod(str)};
        add(value);
    } catch (std::invalid_argument&) {
        nr_missing_++;
    }
}

std::ostream& operator<<(std::ostream& out, const Statistics& stats) {
    return out << "name = " << stats.name() << std::endl
               << "n = " << stats.n() << std::endl
               << "mean = " << stats.mean() << std::endl
               << "stddev = " << stats.stddev() << std::endl
               << "min = " << stats.min() << std::endl
               << "max = " << stats.max() << std::endl
               << "nr. missing = " << stats.nr_missing();
}
