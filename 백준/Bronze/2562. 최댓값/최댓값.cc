#include <stdio.h>

int main(){
    int arr[9];
    int max = 0, index;
    for(int i=0; i < 9; i++){
        scanf("%d", &arr[i]);
        if(max < arr[i]){
            max = arr[i];
            index = i + 1;
        }
    }
    printf("%d %d", max, index);
}