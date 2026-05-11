import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Dados arbitrários para distribuição do tempo
activities = ['Trabalho', 'Descanso', 'Esporte', 'Sono']
time_spent = [8, 2, 2, 12]  # Horas para cada atividade

def plot_pie_chart(start_angle):
    plt.clf()  # Limpeza da figura atual
    plt.pie(time_spent, labels=activities, startangle=start_angle, autopct='%1.1f%%')
    plt.title('Distribuição do tempo durante o dia')
    plt.draw()

def update(val):
    angle = slider.val
    plot_pie_chart(angle)

# Criação da figura e dos eixos
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

# Desenho inicial do gráfico de pizza
plot_pie_chart(0)

# Configuração do slider para alterar o ângulo inicial
ax_angle = plt.axes([0.1, 0.1, 0.8, 0.05])
slider = Slider(ax_angle, 'Ângulo Inicial', 0, 360, valinit=0)

slider.on_changed(update)

plt.show(block=True)