function solution(str_list, ex) {
    var answer = [];
    for(let i of str_list){
        if(!i.includes(ex)){
            answer.push(i)
        }
    }
    return answer.join("");
}