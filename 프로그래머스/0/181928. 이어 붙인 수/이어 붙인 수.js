function solution(num_list) {
    var answer = 0;
    let a = ''
    let b = ''
    for (let i=0; i < num_list.length; i++){
        if (num_list[i] % 2 == 1)
            a += String(num_list[i])
        else
            b += String(num_list[i])
    }
    answer = parseInt(a) + parseInt(b)
    return answer;
}