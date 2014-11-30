#ifndef MATRIX_H_
#define MATRIX_H_

class Matrix {
 public:
  Matrix(int rows, int cols);
  ~Matrix();
  double GetVal(int i, int j) const;
  void SetVal(int i, int j, double val);
  int GetNumRows() const;
  int GetNumCols() const;
  double* GetCol(int j) const;

 private:
  double *matrix_;
  const int nrows_;
  const int ncols_;
};

#endif // MATRIX_H_