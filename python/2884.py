#사용자로부터 알람 시간을 입력받음
h,m = map(int, input('입력 ').split())

#두 정수 H, M의 조건 설정
if (h > 23) or (h <0) or (m > 60) or (m < 0):
    print('다시 입력해주세요.')

if ((m - 45) < 0) and ((h - 1) >= 0):
    h = h-1
    m = (m - 45) + 60
    print('정답 ',h, m)
elif ((m - 45) == 0):
    h = h
    m = m - 45
    print('정답 ',h, m)
elif((m - 45) < 0) and ((h - 1) < 0):
    h = (h - 1) + 24
    m = 60 + (m - 45)
    print('정답 ',h, m)
else:
    h = h
    m = m - 45
    print('정답 ',h, m)
