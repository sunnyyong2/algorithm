1) 정류장 번호를 인덱스로 하는 배열을 만들고, 입력된 충전기 위치를 표시한다.
2) 마지막 충전위치 last = 0(출발지에는 충전기가 있음)
충전횟수 cnt = 0(출발지 충전은 포함하지 않는다.)
3) last + k >= N(마지막 충전 위치 + 운행거리 >=종점을 지나면 종료)
last + k < N 인 동안 충전과 운행을 반복
4) last + k인 자리(next_stop)에 충전기가 있으면
last = last + k 방금 충전한 위치를 마지막 충전 위치로 기록하고
cnt += 1 충전횟수 1 증가
5) last+k인 자리 next_stop에 충전기가 없으면
충전기를 찾을 때까지 next_stop 1 감소
- next_stop과 last가 같아지면 운행 불가
- last에 다다르기 전 next_stop에 충전기가 있으면
충전기가 있는 위치를 마지막 충전 위치로 기록 last = next_stop
cnt += 1, 3)부터 반복