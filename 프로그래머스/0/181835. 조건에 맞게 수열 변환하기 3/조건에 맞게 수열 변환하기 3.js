function solution(arr, k) {
    var answer = [];
    for(let i=0; i < arr.length; i++){
        if(k % 2 != 0){
            answer.push(k * arr[i]);
        }
        else{
            answer.push(k + arr[i])
        }
    }
    return answer;
}