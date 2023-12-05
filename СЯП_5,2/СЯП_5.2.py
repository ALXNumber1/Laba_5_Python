import numpy as np
import matplotlib.pyplot as plt


def f(x, a):
    return np.exp(a * x) - 3.45 * a


if __name__ == "__main__":
    x_value = 3.67
    a_values = np.arange(0, 2.1, 0.2)

    # Создание массива значений функции
    function_values = [f(x_value, a) for a in a_values]

    # Вывод значений аргумента и функции
    for a, value in zip(a_values, function_values):
        print(f'{a = :.2f}, f(x) = {value:.2f}')

    # Нахождение наибольшего и наименьшего значений
    max_value = np.max(function_values)
    min_value = np.min(function_values)

    # Нахождение среднего значения
    mean_value = float(np.mean(function_values))

    # Вывод результатов
    print(f'\nМаксимальное значение: {max_value:.2f}')
    print(f'Минимальное значение: {min_value:.2f}')
    print(f'Среднее значение: {mean_value:.2f}')
    print(f'Количество элементов массива: {len(function_values)}')

    # Сортировка массива
    sorted_values = np.sort(function_values)

    # Построение графика
    plt.plot(a_values, function_values, marker='o', label='f(x)')
    plt.axhline(y=mean_value, color='r', linestyle='--', label='Среднее значение')

    # Оформление графика
    plt.xlabel('Значения параметра a')
    plt.ylabel('Значения функции f(x)')
    plt.title('График функции f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()