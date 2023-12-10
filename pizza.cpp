/*Pizza parlor accepting maximum M orders. Orders are served in first come first served basis. Order 
once placed cannot be cancelled. Write C++ program to simulate the system using circular queue 
using array*/
#include<iostream>
using namespace std;

class CircularQueue {
private:
    int front, rear, capacity;
    int* queue;

public:
    CircularQueue(int size) {
        front = rear = -1;
        capacity = size;
        queue = new int[size];
    }

    void enqueue(int order) {
        if ((rear + 1) % capacity == front) {
            cout << "Queue is full. Cannot accept more orders." << endl;
        } else {
            if (front == -1)
                front = 0;
            rear = (rear + 1) % capacity;
            queue[rear] = order;
            cout << "Order " << order << " placed successfully." << endl;
        }
    }

    void serveOrders(int numOrders) {
        if (front == -1)
            cout << "No orders to serve." << endl;
        else {
            cout << "Serving orders: ";
            for (int i = 0; i < numOrders; ++i) {
                cout << queue[front] << " ";
                if (front == rear)
                    front = rear = -1;
                else
                    front = (front + 1) % capacity;
            }
            cout << endl;
        }
    }
};

int main() {
    int maxOrders = 10; // Maximum orders the pizza parlor can accept
    CircularQueue pizzaQueue(maxOrders);

    pizzaQueue.enqueue(1);
    pizzaQueue.enqueue(2);
    pizzaQueue.enqueue(3);

    pizzaQueue.serveOrders(2);

    pizzaQueue.enqueue(4);
    pizzaQueue.enqueue(5);
    pizzaQueue.enqueue(6);

    pizzaQueue.serveOrders(3);

    return 0;
}
