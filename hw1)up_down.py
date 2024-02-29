import random

def initialize_env(dict):
    dict['correct_answer'] = random.randint(1, 100)
    dict['try_attempt'] = 1

env_dict={
    'try_attempt' : 1,
    'correct_answer' : random.randint(1, 100),
    'record_list' : []
}

while (1):
    print('숫자를 입력하세요')
    try:
        user_answer = int(input())
        if user_answer > 100 or user_answer < 1:
            print('유효한 범위의 숫자를 입력해주세요.')
        elif user_answer > env_dict['correct_answer']:
            print('DOWN')
            env_dict['try_attempt'] += 1
        elif user_answer < env_dict['correct_answer']:
            print('UP')
            env_dict['try_attempt'] += 1
        else:
            print('정답입니다!')
            print(str(env_dict['try_attempt'])+'회만에 맞추셨습니다!')
            print('다시 하시겠습니까? (y/n) :')
            continue_answer = input()
            if continue_answer == 'n':
                break
            elif continue_answer == 'y' :
                env_dict['record_list'].append(env_dict['try_attempt'])
                env_dict['record_list'].sort()
                initialize_env(env_dict)
                print('최고 기록은 '+str(env_dict['record_list'][0])+'회입니다.')
            else :
                print('잘못된 입력입니다. 프로그램을 종료합니다.')
                break
    except ValueError:
        print('잘못된 입력입니다. 다시 입력해주세요')
