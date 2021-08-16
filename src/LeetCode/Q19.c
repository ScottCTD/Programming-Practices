// 19. Remove Nth Node From End of List
// Given the head of a linked list, remove the nth node from the end of the list and return its head.
// Scott 2021/08/17

#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

// Original
// 65.06% 
// Time: O(size of linked list) Space: O(1)
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int size = 0;
    struct ListNode* node = head;
    while (node != NULL) {
        ++size;
        node = node->next;
    }
    if (size == 1) {
        return NULL;
    }
    if (size == n) {
        return head->next;
    }
    node = head;
    struct ListNode* prev = head;
    for (int i = 0; i < size - n; ++i) {
        prev = node;
        node = node->next;
    }
    prev->next = node->next;
    return head;
}

int main() {

    // struct ListNode node04 = {5, NULL};
    // struct ListNode node03 = {4, &node04};
    // struct ListNode node02 = {3, &node03};
    struct ListNode node01 = {2, NULL}; 
    struct ListNode head = {1, &node01};

    struct ListNode* result = removeNthFromEnd(&head, 2);

    struct ListNode* node = result;
    while (node != NULL) {
        printf("%d\n", node->val);
        node = node->next;
    }

    return 0;
}