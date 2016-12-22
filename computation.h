#ifndef __COMPUTATION_H__
#define __COMPUTATION_H__
#include "thread_pool.h"

typedef void (*OnComputationComplete)(void*);

struct Computation {
    void (*f)(void*);
    void* arg;
    pthread_mutex_t m;
    pthread_cond_t finished_cond;
    int complete;
    struct Task task;
    OnComputationComplete on_complete;
    void* on_complete_arg;
};

void thpool_submit_computation(
    struct ThreadPool *pool,
    struct Computation *computation,
    OnComputationComplete on_complete,
    void* on_complete_arg
);

void thpool_complete_computation(
    struct Computation *computation
);

void thpool_wait_computation(struct Computation *computation);
#endif
