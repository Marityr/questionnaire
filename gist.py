from math import pi
import matplotlib.pyplot as plt

# Вносим данные - какие скиллы хотим видеть в веб-разработчике
cat = ['Speed', 'Laziness', 'Responsibility', 'Teamwork', 'Decency']
values = [30, 30, 100, 10, 30]

N = len(cat)

x_as = [n / float(N) * 2 * pi for n in range(N)]

# Связываем последнее значение с первым чтобы построить радиальный график
values += values[:1]
x_as += x_as[:1]

# Устанавливаем цвет и толщину линий
plt.rc('axes', linewidth=0.5, edgecolor="#888888")

# Создаем диаграмму
ax = plt.subplot(111, polar=True)

# Устанавливаем стили для сетки
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)

# Убираем стандартные метки
plt.xticks(x_as[:-1], [])

# Выводим шаг значения на график
plt.yticks([30, 60, 100], ["", "", ""])

# Берем данные для диаграммы
ax.plot(x_as, values, linewidth=0, linestyle='solid', zorder=3)

# Заполняем область под значениями
ax.fill(x_as, values, 'b', alpha=0.3)

# Ограничиваем области
plt.ylim(0, 100)

# Отрисовываем все элементы
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 100 + distance_ax, cat[i], size=10, horizontalalignment=ha, verticalalignment="center")


# Показываем итоговую диаграмму
plt.show()