/*
Write program to implement a priority queue in C++ using an inorder list to store the 
items in the queue. Create a class that includes the data items (which should be 
template) and the priority (which should be int). The inorder list should contain these 
objects, with operator <= overloaded so that the items with highest priority appear at the 
beginning of the list (which will make it relatively easy to retrieve the highest item.)*/
#include <iostream>
using namespace std;

template <typename T>
class PriorityQueue {
private:
    struct Node {
        T data;
        int priority;
        Node* next;
        Node(const T& item, int p) : data(item), priority(p), next(nullptr) {}
    };

    Node* head;

public:
    PriorityQueue() : head(nullptr) {}

    void enqueue(const T& item, int priority) {
        Node* newNode = new Node(item, priority);
        if (!head || priority > head->priority) {
            newNode->next = head;
            head = newNode;
        } else {
            Node* current = head;
            while (current->next && priority <= current->next->priority) {
                current = current->next;
            }
            newNode->next = current->next;
            current->next = newNode;
        }
    }

    T dequeue() {
        if (!head) {
            cerr << "Queue is empty!" << endl;
            exit(1);
        }
        Node* temp = head;
        T data = temp->data;
        head = head->next;
        delete temp;
        return data;
    }

    bool isEmpty() const {
        return head == nullptr;
    }
};

int main() {
    PriorityQueue<string> priorityQueue;

    priorityQueue.enqueue("Item 1", 2);
    priorityQueue.enqueue("Item 2", 1);
    priorityQueue.enqueue("Item 3", 3);

    while (!priorityQueue.isEmpty()) {
        cout << "Dequeued: " << priorityQueue.dequeue() << endl;
    }

    return 0;
}
