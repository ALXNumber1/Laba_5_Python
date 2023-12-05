import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Создадим данные для построения графиков
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Функции
    z1 = abs(x) ** 0.25 + abs(y) ** 0.25
    z2 = x ** 2 - y ** 2
    z3 = 2 * x + 3 * y
    z4 = x ** 2 + y ** 2
    z5 = 2 + 2 * x + 2 * y - x ** 2 - y ** 2

    # Построение графиков
    fig = plt.figure(figsize=(15, 5))

    # График 1
    ax1 = fig.add_subplot(151, projection='3d')
    ax1.plot_surface(x, y, z1, cmap='coolwarm')
    ax1.set_title('$z = x^{0.25} + y^{0.25}$')

    # График 2
    ax2 = fig.add_subplot(152, projection='3d')
    ax2.plot_surface(x, y, z2, cmap='cividis')
    ax2.set_title('$z = x^2 - y^2$')

    # График 3
    ax3 = fig.add_subplot(153, projection='3d')
    ax3.plot_surface(x, y, z3, cmap='viridis')
    ax3.set_title('$z = 2x + 3y$')

    # График 4
    ax4 = fig.add_subplot(154, projection='3d')
    ax4.plot_surface(x, y, z4, cmap='inferno')
    ax4.set_title('$z = x^2 + y^2$')

    # График 5
    ax5 = fig.add_subplot(155, projection='3d')
    ax5.plot_surface(x, y, z5, cmap='magma')
    ax5.set_title('$z = 2 + 2x + 2y - x^2 - y^2$')

    plt.show()