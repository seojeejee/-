print('Hello Mars')

try:
    # 로그 파일 읽기
    with open('./mission_computer_main.log', 'r', encoding='UTF-8') as file:
        logList = file.readlines()

    # 로그 출력
    for log in logList:
        print(log, end='')

    print('\n--------------------------------------------------------\n')

# 예외 처리 
except Exception as e:
    error_message = str(e)
    with open('./error_file.txt', 'w', encoding='UTF-8') as error_file:
        error_file.write(error_message)
