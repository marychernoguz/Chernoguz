# импорт библиотек
import numpy as np
import matplotlib.pyplot as plt
# чтение данных из файла
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data.txt", dtype = float)
# перевод напряжения
for i in range (len(data_array)):
    data_array[i] = data_array[i] / 256 * 3.3
x=[]
# создание фигуры и настройка времени
fig, ax = plt.subplots(figsize = (10, 7 ), dpi = 100)
for i in range (len(data_array)):
    x.append(i / 800 * 12)
# подпись осей и аннотация
ax.set_xlabel('time')
ax.set_ylabel('voltage')
ax.annotate('local max', xy=(5.7, max(data_array)), xytext=(max(data_array), 1.5),
            arrowprops=dict(facecolor='black', shrink=0.005))
# постройка графика и маркеры
ax.plot(x, data_array, linewidth = 1,  color = "Green",
        marker = "|", markersize = "5", label = "mesure")
# положение легенды и размер текста
ax.legend(fontsize=16, loc = 'upper left')
# заголовок из двух строк
plt.title('Mesure of voltage \n time of expirement is 12 sec')
# сетка главная и дополнительная
ax.grid(which = "major", color = "limegreen", linestyle = "dashed")
ax.minorticks_on()
ax.grid(which = "minor", color = "yellow", linestyle = "-")
# показ графика
plt.xlim(0)
plt.ylim(0)
plt.show()
# сохранение графика
fig.savefig("Graph.svg")