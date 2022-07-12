import matplotlib.pyplot as plt
import numpy as np


# Нормальное отображение китайского и минусового знаков
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# Использовать стиль рисования ggplot
plt.style.use('ggplot')

# Создать данные
values = [1, 2, 4, 1, 3]
feature = ['Сила атаки', 'Защита', 'Устойчивость',
           'Сила заклинания', 'жизненная ценность', 'Сила атаки']

color = ['r', 'r', 'r', 'r', 'r']
N = len(values)
# Установите угол радиолокационной карты, используемый для разделения круглой поверхности пополам
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# Чтобы закрыть радарную диаграмму, необходимо выполнить следующие шаги
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

# Рисование
fig = plt.figure()
# Здесь должен быть установлен полярный формат координат
ax = fig.add_subplot(111, polar=True)
# Нарисуйте линейную диаграмму
ax.plot(angles, values, 'o-', linewidth=1)
# Цвет заливки
ax.fill(angles, values, color='r', alpha=0.25)
# Добавить теги для каждой функции
ax.set_thetagrids(angles * 180 / np.pi, feature)
# Установить диапазон радиолокационной карты
plt.yticks([1, 2, 3, 4, 5], ["", "", "", "", ""])
ax.set_ylim(0, 5)
# Добавить заголовок
plt.title('Атрибуты игрового персонажа')
# Добавить линии сетки
ax.grid(True)
# Отображение графики
plt.show()
