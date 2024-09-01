/*
 * @lc app=leetcode id=1116 lang=c
 *
 * [1116] Print Zero Even Odd
 *
 * https://leetcode.com/problems/print-zero-even-odd/description/
 *
 * concurrency
 * Medium (60.97%)
 * Likes:    490
 * Dislikes: 333
 * Total Accepted:    52.9K
 * Total Submissions: 86K
 * Testcase Example:  '2'
 *
 * You have a function printNumber that can be called with an integer parameter
 * and prints it to the console.
 * 
 * 
 * For example, calling printNumber(7) prints 7 to the console.
 * 
 * 
 * You are given an instance of the class ZeroEvenOdd that has three functions:
 * zero, even, and odd. The same instance of ZeroEvenOdd will be passed to
 * three different threads:
 * 
 * 
 * Thread A: calls zero() that should only output 0's.
 * Thread B: calls even() that should only output even numbers.
 * Thread C: calls odd() that should only output odd numbers.
 * 
 * 
 * Modify the given class to output the series "010203040506..." where the
 * length of the series must be 2n.
 * 
 * Implement the ZeroEvenOdd class:
 * 
 * 
 * ZeroEvenOdd(int n) Initializes the object with the number n that represents
 * the numbers that should be printed.
 * void zero(printNumber) Calls printNumber to output one zero.
 * void even(printNumber) Calls printNumber to output one even number.
 * void odd(printNumber) Calls printNumber to output one odd number.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 2
 * Output: "0102"
 * Explanation: There are three threads being fired asynchronously.
 * One of them calls zero(), the other calls even(), and the last one calls
 * odd().
 * "0102" is the correct output.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 5
 * Output: "0102030405"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 1000
 * 
 * 
 */
// Global function to print a number
#include <stdio.h> // Include the necessary header file
void printNumber(int x) { printf("%d", x); }
// @lc code=start

// Include necessary headers based on the operating system
#ifdef _WIN32
#include <windows.h>
typedef HANDLE Mutex;
#define LOCK(mutex) WaitForSingleObject(mutex, INFINITE)
#define UNLOCK(mutex) ReleaseMutex(mutex)
#define INIT_MUTEX(mutex) mutex = CreateMutex(NULL, FALSE, NULL)
#define DESTROY_MUTEX(mutex) CloseHandle(mutex)
typedef DWORD(WINAPI *ThreadFunction)(LPVOID);
#define CREATE_THREAD(thread, func, arg) thread = CreateThread(NULL, 0, func, arg, 0, NULL)
#define JOIN_THREAD(thread) WaitForSingleObject(thread, INFINITE)
#define THREAD_RETURN DWORD WINAPI
#else
#include <pthread.h>
typedef pthread_mutex_t Mutex;
#define LOCK(mutex) pthread_mutex_lock(&mutex)
#define UNLOCK(mutex) pthread_mutex_unlock(&mutex)
#define INIT_MUTEX(mutex) pthread_mutex_init(&mutex, NULL)
#define DESTROY_MUTEX(mutex) pthread_mutex_destroy(&mutex)
typedef void *(*ThreadFunction)(void *);
#define CREATE_THREAD(thread, func, arg) pthread_create(&thread, NULL, func, arg)
#define JOIN_THREAD(thread) pthread_join(thread, NULL)
#define THREAD_RETURN void *
#endif

typedef struct {
    int n;
    Mutex zero_lock;
    Mutex even_lock;
    Mutex odd_lock;
} ZeroEvenOdd;

// Function to create and initialize the ZeroEvenOdd object
ZeroEvenOdd *zeroEvenOddCreate(int n) {
    ZeroEvenOdd *obj = (ZeroEvenOdd *)malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    INIT_MUTEX(obj->zero_lock);
    INIT_MUTEX(obj->even_lock);
    INIT_MUTEX(obj->odd_lock);

    LOCK(obj->even_lock); // lock even and odd initially
    LOCK(obj->odd_lock);
    return obj;
}

THREAD_RETURN zero(void *arg) {
    ZeroEvenOdd *obj = (ZeroEvenOdd *)arg;
    for (int i = 1; i <= obj->n; i++) {
        LOCK(obj->zero_lock);
        printNumber(0);
        if (i % 2 == 0)
            UNLOCK(obj->even_lock);
        else
            UNLOCK(obj->odd_lock);
    }
    return 0;
}

THREAD_RETURN even(void *arg) {
    ZeroEvenOdd *obj = (ZeroEvenOdd *)arg;
    for (int i = 2; i <= obj->n; i += 2) {
        LOCK(obj->even_lock);
        printNumber(i);
        UNLOCK(obj->zero_lock);
    }
    return 0;
}

THREAD_RETURN odd(void *arg) {
    ZeroEvenOdd *obj = (ZeroEvenOdd *)arg;
    for (int i = 1; i <= obj->n; i += 2) {
        LOCK(obj->odd_lock);
        printNumber(i);
        UNLOCK(obj->zero_lock);
    }
    return 0;
}

void zeroEvenOddFree(ZeroEvenOdd *obj) {
    DESTROY_MUTEX(obj->zero_lock);
    DESTROY_MUTEX(obj->even_lock);
    DESTROY_MUTEX(obj->odd_lock);
    free(obj);
}

// @lc code=end
