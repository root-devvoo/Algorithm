// sudo-G41 의 답안
// 자바나 파이썬으로 Converting하면서 스스로 공부할 목적으로 올림
// 나는 해결 못했던 문제니까... ㅠ
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> p) {
  vector<int> answer(p.size(),0);
  for(int i=0,j=0,minIdx=0; i<p.size();){
    if(j<p.size()){
      if(p[j]<p[minIdx]){
        minIdx=j;
      }
      j++;
    }
    else{
      if(minIdx==i){
        i++;
      }
      else{
        answer[i]++;
        answer[minIdx]++;
        int tmp=p[i];
        p[i]=p[minIdx];
        p[minIdx]=tmp;
      }
      minIdx=j=i;
    }
  }
  return answer;
}
