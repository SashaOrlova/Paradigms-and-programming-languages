#include "computation.h"

void thpool_submit_computation(struct ThreadPool *pool, struct Computation *computation,
    OnComputationComplete on_complete, void* on_complete_arg)
{
    pthread_mutex_init(&computation->m, NULL);
    pthread_cond_init(&computation->finished_cond, NULL);
    computation->complete = 0;
    computation->task.f = computation->f;
    computation->task.arg = computation->arg;
    computation->on_complete = on_complete;
    computation->on_complete_arg = on_complete_arg;
    thpool_submit(pool, &(computation->task));
}


void thpool_complete_computation(struct Computation *computation){
    pthread_mutex_lock(&computation->m);
    computation->complete = 1;
    if (computation->on_complete)
        computation->on_complete(computation->on_complete_arg);
    pthread_cond_signal(&computation->finished_cond); 
    pthread_mutex_unlock(&computation->m);
}


void thpool_wait_computation(struct Computation *computation){
        pthread_mutex_lock(&computation->m);
        while (!computation->complete) {
            pthread_cond_wait(&computation->finished_cond, &computation->m);
        }
        pthread_mutex_unlock(&computation->m);
        pthread_cond_destroy(&computation->finished_cond);
        pthread_mutex_destroy(&computation->m);
}
