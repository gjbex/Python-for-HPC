#include "matrices.h"

Matrix::Matrix(const Matrix& other) :
        rows_(other.rows_), cols_(other.cols_),
        data_(new double[rows_ * cols_]) {
    for (int i = 0; i < rows_ * cols_; ++i) {
        data_[i] = other.data_[i];
    }
}

Matrix& Matrix::operator=(const Matrix& other) {
    if (this != &other) {
        rows_ = other.rows_;
        cols_ = other.cols_;
        data_.reset(new double[rows_ * cols_]);
        for (int i = 0; i < rows_ * cols_; ++i) {
            data_[i] = other.data_[i];
        }
    }
    return *this;
}

Matrix::Matrix(Matrix&& other) noexcept :
        rows_{other.rows_}, cols_{other.cols_},
        data_{std::move(other.data_)} {
    other.rows_ = 0;
    other.cols_ = 0;
}

Matrix& Matrix::operator=(Matrix&& other) noexcept {
    if (&other != this) {
        rows_ = other.rows_;
        cols_ = other.cols_;
        data_ = std::move(other.data_);

        other.rows_ = 0;
        other.cols_ = 0;
    }
    return *this;
}

bool Matrix::operator==(const Matrix& other) const {
    if (this == &other) {
        return true;
    }
    if (rows_ != other.rows_ || cols_ != other.cols_) {
        return false;
    }
    for (int i = 0; i < rows_; ++i) {
        for (int j = 0; j < cols_; ++j) {
            if ((*this)(i, j) != other(i, j)) {
                return false;
            }   
        }
    }
    return true;
}

std::ostream& operator<<(std::ostream& os, const Matrix& m) {
    for (int i = 0; i < m.rows_; ++i) {
        for (int j = 0; j < m.cols_; ++j) {
            os << m(i, j) << " ";
        }
        os << std::endl;
    }
    return os;
}
