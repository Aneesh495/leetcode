#include <random>
#include <vector>

class Skiplist {
private:
    static constexpr int MAX_LEVEL = 16;
    struct Node {
        int value;
        std::vector<Node*> next;
        Node (int value, int level)
            : value(value), next(level, nullptr) {}
    };
    Node* head;
    std::mt19937 generator;
    std::bernoulli_distribution coinFlip;

    int randomLevel() {
        int level = 1;
        while (level < MAX_LEVEL && coinFlip(generator)) {
            ++level;
        }
        return level;
    }
public:
    Skiplist()
        : head(new Node(0, MAX_LEVEL)),
          generator(std::random_device{}()),
          coinFlip(0.5) {}
    ~Skiplist() {
        Node* current = head;
        while (current != nullptr) {
            Node*next = current->next[0];
            delete current;
            current = next;
        }
    }
    
    bool search(int target) {
        Node* current = head;
        for (int level = MAX_LEVEL - 1; level >= 0; --level) {
            while (current->next[level] != nullptr && current->next[level]->value < target) {
                    current = current->next[level];
            }
        }
        current = current->next[0];
        return current != nullptr && current->value == target;
    }
    
    void add(int num) {
        std::vector<Node*> predecessors(MAX_LEVEL, nullptr);
        Node* current = head;
        for (int level = MAX_LEVEL - 1; level >= 0; --level) {
            while (current->next[level] != nullptr && current->next[level]->value < num) {
                current = current->next[level];
            }
            predecessors[level] = current;
        }
        int nodeLevel = randomLevel();
        Node* newNode = new Node(num, nodeLevel);
        for (int level = 0; level < nodeLevel; ++level) {
            newNode->next[level] = predecessors[level]->next[level];
            predecessors[level]->next[level] = newNode;
        }
    }
    
    bool erase(int num) {
        std::vector<Node*> predecessors(MAX_LEVEL, nullptr);
        Node* current = head;
        for (int level = MAX_LEVEL - 1; level >= 0; --level) {
            while (current->next[level] != nullptr && current->next[level]->value < num) {
                current = current->next[level];
            }
            predecessors[level] = current;
        }
        Node* target = predecessors[0]->next[0];
        if (target == nullptr || target->value != num) {
            return false;
        }
        for (int level = 0; level < MAX_LEVEL; ++level) {
            if (predecessors[level]->next[level] == target) {
                predecessors[level]->next[level] = target->next[level];
            }
        }
        delete target;
        return true;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */