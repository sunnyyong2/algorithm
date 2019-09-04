score = [88, 30, 61, 55, 95]
# for i in score:
# idx     0    1   2   3   4
# print('score_length:', len(score))
for i in range(len(score)):
    if i > 60:
        print('{}번 학생은 {}점으로 합격입니다.'.format(i+1, score[i]))
    else:
        print('{}번 학생은 {}점으로 불합격입니다.'.format(i+1, score[i]))
# for i in range(len(score)):
#     print('i:', i, 'score:', score[i])