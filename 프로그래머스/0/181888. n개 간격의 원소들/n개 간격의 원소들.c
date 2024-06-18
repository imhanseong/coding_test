#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num_list[], size_t num_list_len, int n) {
    size_t answer_len = (num_list_len + n - 1) / n; // 반환할 배열의 길이
    int* answer = (int*)malloc(answer_len * sizeof(int)); // 동적 메모리 할당

    int index = 0;
    for (int i = 0; i < num_list_len; i += n) {
        answer[index++] = num_list[i]; // n개 간격으로 원소 추가
    }

    return answer;
}