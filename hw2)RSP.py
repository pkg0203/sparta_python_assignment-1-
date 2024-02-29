import random
RSP_list = ['가위','바위','보']
Record = {
    'win' : 0,
    'lose' : 0,
    'tie' : 0
}
while(1) :
    computer_index = random.randint(0,2)
    computer_answer = RSP_list[computer_index]
    print('\'가위 / 바위 / 보\'중에서 선택해주세요.')
    user_answer=input()
    if not user_answer in RSP_list :
        print('유효하지 않은 입력입니다.')
        continue
    else :
        print(f'사용자 : {user_answer} / 컴퓨터 : {computer_answer}')
        if user_answer == computer_answer :
            print('비겼습니다.')
            Record['tie']+=1
        elif (user_answer=='가위' and computer_answer=='보') or (user_answer=='바위' and computer_answer=='가위') or (user_answer=='보' and computer_answer=='바위'):
            print('이겼습니다!')
            Record['win']+=1
        else :
            print('패배했습니다...')
            Record['lose']+=1
        print('다시 하시겠습니까? (y/n)')
        continue_answer=input()
        if continue_answer=='n' :
            print('게임을 종료합니다.')
            print('승: '+str(Record['win'])+' 패: '+str(Record['lose'])+' 무승부: '+str(Record['tie']))
            break
        elif continue_answer!='y':
            print('유효하지 않은 입력입니다. 프로그램을 종료합니다.')
            print('승: '+str(Record['win'])+' 패: '+str(Record['lose'])+' 무승부: '+str(Record['tie']))
            break