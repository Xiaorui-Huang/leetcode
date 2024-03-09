#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <iostream>
#include <vector>

using std::ostream;
using std::vector;

/**
 * @brief ListNodeType struct representing a node in a singly linked list
 *
 * @tparam T - Type of the value in the node
 */
template <typename T>
struct ListNodeType {
    T val;
    ListNodeType *next;
    ListNodeType();
    ListNodeType(T x);
    ListNodeType(T x, ListNodeType *next);
    void insertAtEnd(T value);
    ~ListNodeType();
};

// define default ListNodeType as int
using ListNode = ListNodeType<int>;



// instead of .tpp file just implement the template functions here
// Constructor implementations

template <typename T>
ListNodeType<T>::ListNodeType() : val(T()), next(nullptr) {}

template <typename T>
ListNodeType<T>::ListNodeType(T x) : val(x), next(nullptr) {}

template <typename T>
ListNodeType<T>::ListNodeType(T x, ListNodeType *next) : val(x), next(next) {}

template <typename T>
void ListNodeType<T>::insertAtEnd(T value) {
    ListNodeType *newNode = new ListNodeType(value);
    if (this == nullptr) {
        *this = *newNode;
    } else {
        ListNodeType *temp = this;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

template <typename T>
ListNodeType<T>::~ListNodeType() {
    // do nothing as we may have dynamic memory that is not owned by the stack
    // alway clean up manually
}

/**
 * @brief Build a linked list from a vector of values
 *
 * @tparam T Type of the value in the node
 * @param nums vector of values
 * @return ListNodeType<T>* - head node of the linked list
 */
template <typename T>
ListNodeType<T> *buildLinkedList(const vector<T> &nums) {
    if (nums.empty())
        return nullptr;

    ListNodeType<T> *head = new ListNodeType<T>(nums[0]);
    ListNodeType<T> *current = head;
    for (size_t i = 1; i < nums.size(); ++i) {
        current->next = new ListNodeType<T>(nums[i]);
        current = current->next;
    }
    return head;
}

/**
 * @brief Convert a linked list to a vector of values.
 *
 * @tparam T Type of the value in the node.
 * @param head Pointer to the head node of the linked list.
 * @return vector<T> Vector containing the values from the linked list.
 */
template <typename T>
vector<T> linkedListToVector(const ListNodeType<T>* head) {
    vector<T> result;
    const ListNodeType<T>* current = head;
    while (current != nullptr) {
        result.push_back(current->val);
        current = current->next;
    }
    return result;
}


/**
 * @brief Print the linked list
 *
 * @tparam T - Type of the value in the node
 * @param os - output stream
 * @param head - head node of the linked list
 * @return ostream& - output stream
 */
template <typename T>
ostream &operator<<(ostream &os, const ListNodeType<T> *head) {
    const ListNodeType<T> *current = head;
    while (current != nullptr) {
        os << current->val;
        if (current->next != nullptr)
            os << " -> ";
        current = current->next;
    }
    return os;
}

#endif // LINKED_LIST_H
