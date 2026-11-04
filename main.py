def read_matrix_from_csv(file_path: str) -> list[list[float]]:
    """Считывает CSV-файл и возвращает матрицу из float."""
    with open(file_path, 'r') as f:
        return [[float(x) for x in line.strip().split(',')] for line in f if line.strip()]


def main():
    data1 = read_matrix_from_csv('data1.csv')
    data2 = read_matrix_from_csv('data2.csv')
    
    weights = read_matrix_from_csv('weights.csv')[0]
    
    results = [
        sum(w * abs(d1 - d2) for d1, d2, w in zip(row1, row2, weights))
        for row1, row2 in zip(data1, data2)
    ]
    
    
    critical_count = sum(1 for res in results if res > 5)
    
    if critical_count == 1:
        print(f"critical: {critical_count} result above 5")
    else:
        print(f"criticality: {critical_count} results above 5")

        
if __name__ == '__main__':
    main()
    
    
    
