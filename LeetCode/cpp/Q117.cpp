// 给定一个二叉树

// struct Node {
//   int val;
//   Node *left;
//   Node *right;
//   Node *next;
// }
// 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 nullptr。

// 初始状态下，所有 next 指针都被设置为 nullptr。

#include <iostream>

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:

    // original
    // the idea is to connect the next level on the current level
    Node* connect(Node* root) {
        Node *curr = root;
        Node dummy = Node(0);
        Node *left = &dummy;
        Node *leftmost = nullptr;
        while (curr || leftmost) {
            while (curr) {
                if (curr->left) {
                    if (!leftmost) {
                        leftmost = curr->left;
                    }
                    left->next = curr->left;
                    left = left->next;
                }
                if (curr->right) {
                    if (!leftmost) {
                        leftmost = curr->right;
                    }
                    left->next = curr->right;
                    left = left->next;
                }
                curr = curr->next;
            }
            curr = leftmost;
            leftmost = nullptr;
            left = &dummy;
        }
        return root;
    }
};