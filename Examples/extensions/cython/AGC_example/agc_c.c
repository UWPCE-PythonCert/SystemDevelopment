/* C version of AGC code */

#include <stdio.h>
#include <math.h>

void AGC(int nAGC, int npts, float *amp, float *ampAGC);

void AGC(int nAGC, int npts, float *amp, float *ampAGC) {

	float fmax;
	float absamp[npts];
    int i, j, nAGC2;


    for (i = 0; i < npts; i++){
         ampAGC[i] = 0.0;
         absamp[i] = fabs(amp[i]);
	}
	nAGC2 = nAGC / 2;

    for (i = nAGC2; i < npts-nAGC2; i++){
         fmax = 0.0;
         for ( j=(i-nAGC2); j < i+nAGC2+1; j++ ){
            if ( absamp[j] > fmax ) {
            	fmax = absamp[j];
            }
         }
         ampAGC[i] = amp[i] / fmax;
    }
    return;
  }

