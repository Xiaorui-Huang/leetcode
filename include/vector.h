#ifndef VECTOR_H
#define VECTOR_H

#include <assert.h>
#include <stdlib.h>

#define VEC_IMPL(T)                                                                                 \
    typedef struct {                                                                                \
        int size;                                                                                   \
        int cap;                                                                                    \
        T *data;                                                                                    \
    } Vec_##T;                                                                                      \
                                                                                                    \
    static Vec_##T *vec_new_##T(int init_cap) {                                                     \
        assert(init_cap > 0);                                                                       \
        Vec_##T *vec = (Vec_##T *)malloc(sizeof(Vec_##T));                                          \
        vec->size = 0;                                                                              \
        vec->cap = init_cap;                                                                        \
        vec->data = (T *)malloc(sizeof(T) * init_cap);                                              \
        return vec;                                                                                 \
    }                                                                                               \
                                                                                                    \
    static void vec_free_##T(Vec_##T *vec) {                                                        \
        free(vec->data);                                                                            \
        free(vec);                                                                                  \
    }                                                                                               \
                                                                                                    \
    static void vec_push_##T(Vec_##T *vec, T item) {                                                \
        if (vec->size == vec->cap) {                                                                \
            vec->cap *= 2;                                                                          \
            vec->data = (T *)realloc(vec->data, sizeof(T) * vec->cap);                              \
        }                                                                                           \
        vec->data[vec->size++] = item;                                                              \
    }                                                                                               \
                                                                                                    \
    static T vec_pop_##T(Vec_##T *vec) {                                                            \
        assert(vec->size > 0);                                                                      \
        return vec->data[--vec->size];                                                              \
    }

#endif // VECTOR_H
