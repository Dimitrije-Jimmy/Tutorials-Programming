#include "cuda_runtime.h"
#include "device_launch_parameters.h"
#include <stdio.h>

cudaError_t addWithCuda (int *c, const int *a, const int *b, unsigned int size);

__global__ void addKernel(int *c, const int *a, const int *b) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}
    
int main()
{
    const int arraySize = 5;
    const int a[arraySize] = {1, 2, 3, 4, 5 };
    const int b[arraySize] = { 10, 20, 30, 40, 50 };
    int c[arraySize] = { 0 };
    
    // Add vectors in parallel.
    cudaError_t cudaStatus = addWithCuda (c, a, b, arraySize);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "addWithCuda failed!");
        return 1;
    }

    printf("{1,2,3,4,5} + {10, 20, 30, 40, 50} = {%d,%d,%d,%d,%d}\n",
        c[0], [1], [2], c[3], c[4]);

    // cudaDeviceReset must be called before exiting in order for profiling and
    // tracing tools such as Nsight and Visual Profiler to show complete traces.
    cudaStatus = cudaDevice Reset();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDevice Reset failed!");
        return 1;
    }

    return 0;
}

// Helper function for using CUDA to add vectors in parallel.