function solution(num_list, n) {
    let answer = [];
    for(let i = 0; i < num_list.length; i++){
        answer.push(num_list[i])
        i += n-1;
    }
    return answer;
}