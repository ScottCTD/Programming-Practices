#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*
A Failed Attemp
*/
bool isValid01(char * s){
    char* pointer = s;
    int length = 0;
    while (*(pointer++) != '\0') {
        ++length;
    } 
    if (length == 0 || length == 1 || length % 2 != 0) return false;
    for (int i = 0; i < length; ++i) {
        int index01 = length - 1 - i;
        int index02;
        if (i < length / 2) {
            index02 = length - 1 - (length - i);
        } else {
            index02 = length - 1 - i;
        }
        switch (s[i]) {
            case '(':
                if (s[index01] != ')' && s[i + 1] != ')') {
                    return false;
                }
                break;
            case '[':
                if (s[index01] != ']' && s[i + 1] != ']') {
                    return false;
                }
                break;
            case '{':
                if (s[index01] != '}' && s[i + 1] != '}') {
                    return false;
                }
                break;
            case ')':
                if (i == 0) return false;
                if (s[index02] != '(' && s[i - 1] != '(') {
                    return false;
                }
                break;
            case ']':
                if (i == 0) return false;
                if (s[index02] != '[' && s[i - 1] != '[') {
                    return false;
                }
                break;
            case '}':
                if (i == 0) return false;
                if (s[index02] != '{' && s[i - 1] != '{') {
                    return false;
                }
                break;
        }
    }
    return true;
}

bool isValid02(char* s) {
    char* pointer = s;
    int length = 0;
    while (*(pointer++) != '\0') ++length;
    if (length <= 1) return false;
    bool* is_used = malloc(length);
    for (int i = 0; i < length; ++i) {
        int index = i;
        switch (s[i]) {
        case '(':
            while (index < length) {
                if (s[index] == ')' && !is_used[index]) {
                    is_used[index] = true;
                    break;
                }
                index++;
            }
            if (!is_used[index]) return false;
            break;
        case '[':
            while (index < length) {
                if (s[index] == ']' && !is_used[index]) {
                    is_used[index] = true;
                    break;
                }
                index++;
            }
            if (!is_used[index]) return false;
            break;
        case '{':
            while (index < length) {
                if (s[index] == '}' && !is_used[index]) {
                    is_used[index] = true;
                    break;
                }
                index++;
            }
            if (!is_used[index]) return false;
            break;
        case ')':
            if (is_used[i]) continue;
            return false;
            break;
        case ']':
            if (is_used[i]) continue;
            return false;
            break;
        case '}':
            if (is_used[i]) continue;
            return false;
            break;
        }
    }
    return true;
}

int main() {

    char s[] = "()";
    /*
    A Failed Attemp
    */
    printf("%d\n", isValid02(s));

    return 0;
}