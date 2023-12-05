import numpy as np

if __name__ == "__main__":
    N = 21

    X = np.ones((12, 3))
    X[:, 1] = np.random.randint(N, N + 13, size=12)
    X[:, 2] = np.random.randint(60, 83, size=12)

    Y = np.random.uniform(13.5, 18.6, size=12)

    A = np.linalg.inv(X.T @ X) @ X.T @ Y
    print(f"Оценки уравнения регрессии:\n{A}")

    Y_predicted = A[0] + A[1]*X[:, 1] + A[2]*X[:, 2]

    print(f"\nПредсказанные значения Y:\n{Y_predicted}")

    print(f"\nИсходный вектор-столбец Y:\n{Y}")
