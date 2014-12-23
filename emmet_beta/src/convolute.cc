#include "convolute.h"
#include "math.h"
#include "assert.h"
#include <stdio.h>


int convVal(double *Z, double *data, Matrix3D *pdfValues, Matrix *postConvVal, Integrator *intgr) {

  int ZvarPoints  = pdfValues->GetNumDim1();
  int ZmeanPoints = pdfValues->GetNumDim2();
  int ZPoints     = pdfValues->GetNumDim3();

  // Calculates integrand with pdf and omega
  double *integrand = new double[ZPoints];
  double temp;

  // variance
  for (int n = 0; n < ZvarPoints; n++) {
    // mean
    for (int m = 0; m < ZmeanPoints; m++) {

      for (int k = 0; k < ZPoints; k++) {
	integrand[k] = pdfValues->GetVal(n, m, k) * data[k];
      }
      temp = intgr->integrate(integrand, Z, ZPoints);
      postConvVal->SetVal(n, m, temp);
    }
  }

  // Frees memory allocated within function
  delete integrand;

  return 0;
}