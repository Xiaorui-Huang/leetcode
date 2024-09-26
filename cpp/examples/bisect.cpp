bool book(int start, int end) {
    const pair<int, int> event{start, end};
    const auto nextEvent = calendar.lower_bound(event);
    if (nextEvent != calendar.end() && nextEvent->first < end) {
        return false;
    }

    if (nextEvent != calendar.begin()) {
        const auto prevEvent = prev(nextEvent);
        if (prevEvent->second > start) {
            return false;
        }
    }

    calendar.insert(event);
    return true;
}

#include <algorithm> // for std::lower_bound
#include <vector>

// Binary search to find the position where an element should be inserted
int binarySearch(const std::vector<int> &sortedArray, int target) {
    auto it = std::lower_bound(sortedArray.begin(), sortedArray.end(), target);
    return (it != sortedArray.end() && *it == target) ? std::distance(sortedArray.begin(), it) : -1;
}

#include <algorithm> // for std::lower_bound
#include <vector>

// Insert element into a sorted vector
void insert(std::vector<int> &sortedArray, int value) {
    auto it = std::lower_bound(sortedArray.begin(), sortedArray.end(), value);
    if (it == sortedArray.end() || *it != value) {
        sortedArray.insert(it, value);
    }
}

#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> sortedArray = {1, 3, 5, 7, 9};

    // Binary Search
    int index = binarySearch(sortedArray, 5);
    if (index != -1) {
        std::cout << "Element found at index " << index << std::endl;
    } else {
        std::cout << "Element not found" << std::endl;
    }

    // Insertion
    insert(sortedArray, 6);
    std::cout << "Array after insertion: ";
    for (int num : sortedArray) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}