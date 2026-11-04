def read_matrix_from_csv(file_path: str) -> list[list[float]]:
    """Считывает CSV-файл и возвращает матрицу из float."""
    with open(file_path, 'r') as f:
        # Твой любимый генератор списков!
        return [[float(x) for x in line.strip().split(',')] for line in f if line.strip()]


def main():
    # 1. Читаем данные одной понятной командой
    data1 = read_matrix_from_csv('data1.csv')
    data2 = read_matrix_from_csv('data2.csv')
    
    # Веса — это первая строка из файла weights.csv
    weights = read_matrix_from_csv('weights.csv')[0]
    
       # Вычисляем взвешенную сумму разностей для каждой строки
    results = [
        sum(w * abs(d1 - d2) for d1, d2, w in zip(row1, row2, weights))
        for row1, row2 in zip(data1, data2)
    ]
    
    
    critical = 0
    for i in range(len(results)):   #for all i
        if results[i] > 5:
            critical = critical + 1   #increase by1
    if critical == 1:
        print('criticality: 1 result above 5')
    else:
        print("criticality:", critical, "results above 5")

        
if __name__ == '__main__':
    main()
    
    
    
