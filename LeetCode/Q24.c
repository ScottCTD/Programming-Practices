/**
 * Given a linked list, swap every two adjacent nodes and return its head. 
 * You must solve the problem without modifying the values in the list's nodes 
 * (i.e., only nodes themselves may be changed.)
 * Scott 2021/08/20
*/
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *create_list(int *array, int size) {
    struct ListNode *node = malloc(sizeof(struct ListNode));
    struct ListNode *head = node;
    for (int i = 0; i < size - 1; ++i) {
        node->val = array[i];
        node->next = malloc(sizeof(struct ListNode));
        node = node->next;
    }
    node->val = array[size - 1];
    node->next = NULL;
    return head;
}

// Original
// 37.54%
// Same idea as the 100% one.
// But I failed to properly implement it.
struct ListNode* swapPairs1(struct ListNode* head) {
    struct ListNode *prev = NULL;
    struct ListNode *node = head;
    if (!node) {
        return NULL;
    }
    struct ListNode *next = node->next;
    if (!next) {
        return node;
    }
    struct ListNode *result = next;

    while (node && next) {
        node->next = next->next;
        next->next = node;
        
        if (prev) {
            prev->next = next;
        }

        prev = node;

        if (node->next && next->next) {
            struct ListNode *temp = node;
            node = next->next->next;
            next = temp->next->next;
        } else {
            break;
        }
    }

    return result;
}

int main(void) {

    int array[] = {1, 2, 3, 4, 5};
    struct ListNode *head = create_list(array, 5);
    struct ListNode *result = swapPairs1(head);
    while (result) {
        printf("%d->", result->val);
        result = result->next;
    }
    printf("NULL\n");

    return 0;
}