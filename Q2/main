import json

try:
    # 로그 파일 읽기
    with open('./mission_computer_main.log', 'r', encoding='UTF-8') as file:
        logList = [line.strip().split(',', 1) for line in file if ',' in line]

    # 로그 리스트 출력
    for log in logList:
        print(log)

    print('\n--------------------------------------------------------\n')

    # 시간의 역순으로 정렬 (날짜 및 시간 기준)
    logList.sort(reverse=True, key=lambda x: x[0])

    # 리스트를 사전(Dict)으로 변환
    logDict = {i: {'datetime': log[0], 'message': log[1]} for i, log in enumerate(logList)}

    # JSON 파일로 저장
    with open('./mission_computer_main.json', 'w', encoding='UTF-8') as json_file:
        json.dump(logDict, json_file, ensure_ascii=False, indent=4)

# 예외 처리 
except Exception as e:
    error_message = str(e)
    with open('./error_file.txt', 'w', encoding='UTF-8') as error_file:
        error_file.write(error_message)
