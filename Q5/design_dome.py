import numpy as np

def main():
    # CSV 파일 로딩
    arr1 = np.genfromtxt("mars_base_main_parts-001.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)
    arr2 = np.genfromtxt("mars_base_main_parts-002.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)
    arr3 = np.genfromtxt("mars_base_main_parts-003.csv", delimiter=",", dtype=None, encoding='utf-8-sig', names=True)

    # 배열 병합
    parts = np.concatenate((arr1, arr2, arr3))

    # 평균값 계산
    names = parts['parts'].astype(str)
    strengths = parts['strength']
    unique_parts = np.unique(names)

    averages = np.array([
        (part, strengths[names == part].mean())
        for part in unique_parts
    ], dtype = [('parts', 'U30'), ('avg_strength', 'f4')])

    # 평균값이 50보다 작은 항목 필터링
    parts_to_work_on = parts[means < 50]

    # 파일 저장 (예외처리 포함)
    
    np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%s, %. 3f', header='parts,avg_strength')
  
