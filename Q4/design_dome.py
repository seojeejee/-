material = ''
diameter = 0
thickness = 1
area = 0
weight = 0

# 재질 밀도
density_data = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

gravity_ratio = 0.378

def sphere_area(diameter, material='유리', thickness=1):
    global material, diameter, thickness, area, weight

    radius = diameter / 2  # 단위: m
    area = 2 * 3.1415926535 * radius ** 2  # 반구 표면적 공식, 단위: m²

    # 부피
    volume_cm3 = area * 10000 * thickness

    # 밀도
    density = density_data.get(material, 2.4)  # g/cm³

    # 무게
    weight_g = volume_cm3 * density

    # kg 단위로 환산
    weight = (weight_g / 1000) * gravity_ratio  # g → kg × 화성중력비

    # 소수점 이하 3자리까지 반올림
    area = round(area, 3)
    weight = round(weight, 3)

    print(f'재질 ⇒ {material}, 지름 ⇒ {diameter}, 두께 ⇒ {thickness}, 면적 ⇒ {area}, 무게 ⇒ {weight} kg')


# 반복 실행
while True:
    print('\n돔 무게 계산기 (종료하려면 "q" 입력)')
    dia_input = input('지름을 입력하세요 (단위: m): ')
    if dia_input.lower() == 'q':
        print('프로그램을 종료합니다.')
        break

    try:
        dia = float(dia_input)
        if dia <= 0:
            print('지름은 0보다 커야 합니다.')
            continue
    except ValueError:
        print('숫자를 입력해주세요.')
        continue

    mat_input = input('재질을 입력하세요 (유리 / 알루미늄 / 탄소강) [기본값: 유리]: ')
    if mat_input == '':
        mat_input = '유리'
    elif mat_input not in density_data:
        print('지원하지 않는 재질입니다. 기본값인 유리로 계산합니다.')
        mat_input = '유리'

    thick_input = input('두께를 입력하세요 (단위: cm) [기본값: 1]: ')
    if thick_input == '':
        thick = 1
    else:
        try:
            thick = float(thick_input)
            if thick <= 0:
                print('두께는 0보다 커야 합니다. 기본값 1로 설정합니다.')
                thick = 1
        except ValueError:
            print('숫자가 아닙니다. 기본값 1로 설정합니다.')
            thick = 1

    sphere_area(dia, mat_input, thick)
