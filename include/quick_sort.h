#ifndef QUICK_SORT_H
#define QUICK_SORT_H

#define SWAP(x, y, T)                                                                              \
    do {                                                                                           \
        T temp = *(x);                                                                             \
        *(x) = *(y);                                                                               \
        *(y) = temp;                                                                               \
    } while (0)

// Quicksort implementation with custom comparator
#define QUICKSORT_CMP_IMPL(T, cmp)                                                               \
    static int partition_##T##_cmp(T arr[], int low, int high) {                                   \
        T pivot = arr[high];                                                                       \
        int i = (low - 1);                                                                         \
        for (int j = low; j <= high - 1; j++) {                                                    \
            if (cmp(&arr[j], &pivot) < 0) {                                                        \
                i++;                                                                               \
                SWAP(&arr[i], &arr[j], T);                                                         \
            }                                                                                      \
        }                                                                                          \
        SWAP(&arr[i + 1], &arr[high], T);                                                          \
        return (i + 1);                                                                            \
    }                                                                                              \
    void quick_sort_##T##_cmp(T arr[], int low, int high) {                                        \
        if (low < high) {                                                                          \
            int pi = partition_##T##_cmp(arr, low, high);                                          \
            quick_sort_##T##_cmp(arr, low, pi - 1);                                                \
            quick_sort_##T##_cmp(arr, pi + 1, high);                                               \
        }                                                                                          \
    }

// Quicksort implementation without custom comparator (uses < operator)
#define QUICKSORT_IMPL(T)                                                                        \
    static int partition_##T(T arr[], int low, int high) {                                         \
        T pivot = arr[high];                                                                       \
        int i = (low - 1);                                                                         \
        for (int j = low; j <= high - 1; j++) {                                                    \
            if (arr[j] < pivot) {                                                                  \
                i++;                                                                               \
                SWAP(&arr[i], &arr[j], T);                                                         \
            }                                                                                      \
        }                                                                                          \
        SWAP(&arr[i + 1], &arr[high], T);                                                          \
        return (i + 1);                                                                            \
    }                                                                                              \
    void quick_sort_##T(T arr[], int low, int high) {                                              \
        if (low < high) {                                                                          \
            int pi = partition_##T(arr, low, high);                                                \
            quick_sort_##T(arr, low, pi - 1);                                                      \
            quick_sort_##T(arr, pi + 1, high);                                                     \
        }                                                                                          \
    }

#endif // QUICK_SORT_H