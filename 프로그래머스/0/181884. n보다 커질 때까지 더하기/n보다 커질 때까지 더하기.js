function solution(numbers, n) {
    var answer = 0;
    for(let i=0; i < numbers.length; i++){
        answer = answer + numbers[i];
        if(answer >  n){
                return answer;
        }
    }
}