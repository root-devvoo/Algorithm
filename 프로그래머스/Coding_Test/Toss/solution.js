// 한 문제라도 맞추겠다는 생각으로 했지만, 테스트 시간이 끝나버려서 완전히 solve 하지 못한 1개의 문제
// (나중에라도 제대로 해결해보려고 남긴다)
// 나는 이번 코테를 통해서, 프론트 쪽은 아니라는 확신이 들었다. (물론, 프론트에 대한 역량 준비도 덜 됐고...)
function solution(paths) {
    var answer = '';

    for(i=0; i<paths.length; i++) {
      answer += paths[i];
    }
    
    const path = require("path");

    answer = path.join(answer);

    return answer;
}
