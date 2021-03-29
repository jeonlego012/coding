#include <stdio.h>
#include <math.h>

int findNum, sum = 0;
int isGetAnswer = 0, isEndCheck = 0;
int numList[10][10] = { 0 };
long long answer = 0;  

void makeList() {
    for (int j = 0; j < 10; j++) numList[0][j] = 1;
 
    for (int i = 1; i < 10; i++) {
        for (int j = i; j < 10; j++) {
            if (j == i) numList[i][j] = 1;
            else
                for (int k = i - 1; k < j; k++) numList[i][j] += numList[i-1][k];
        }
    }
}
 
int dfs(long long start_num, long long digit, long long now_num) {
    if (isGetAnswer) return 0;
    if (digit == 1) { 
        if (!isEndCheck) isEndCheck = 1;
        else    sum++;
    }
    else {
        for (long long i = digit-2 ; i < start_num; i++)
            dfs( i, digit-1, now_num+ (long long)(i * pow(10, digit - 2)) );
    }
    if ((sum == findNum) && !isGetAnswer) {
        answer = now_num;
        isGetAnswer = 1;
    }
}

int main(){
    makeList();
 
    scanf("%d", &findNum);
    if (findNum == 0) {
        printf("0\n");
        return 0;
    }
 
    long long start_num;
    long long digit;
    int isFindRange = 0; 
 
    for (int i = 0; i < 10 && (!isFindRange) ; i++) {
        for (int j = i; j < 10 && (!isFindRange); j++) {
            if ( (sum + numList[i][j]) > findNum){
                isFindRange = 1;
            }
            else {
                digit = i + 1;
                start_num = j+1;
                sum += numList[i][j];
            }
        }
    }
 
    long long now_num = (long long)(start_num * pow(10, digit - 1));
    if (findNum == 1022) {
        now_num = 9876543210;
    }
 
    if (sum == findNum) {
        if (sum == 1023)  answer = -1;
        else answer = now_num;
    }
    else if (findNum > 1022  ) {
        answer = -1;
    }
    else dfs(start_num, digit, now_num);
 
    printf("%lld\n", answer); 
 
    return 0; 
}
