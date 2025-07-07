import matplotlib.pyplot as plt
from datetime import datetime

# Dados dos ciclos do ETH
eth_cycles = {
    "2015-08-07": {"event": "Lançamento", "price": 0.75},
    "2016-12-01": {"event": "Pré-Bull Market", "price": 8},
    "2018-01-13": {"event": "Topo ciclo #1", "price": 1400},
    "2018-12-15": {"event": "Fundo Bear", "price": 85},
    "2021-11-10": {"event": "Topo ciclo #2", "price": 4878},
    "2022-06-18": {"event": "Fundo Bear", "price": 880},
    "2025-10-01": {"event": "Topo ciclo #3 (estimado)", "price": 12000},
    "2029-10-01": {"event": "Topo ciclo #4 (estimado)", "price": 22000}
}

# Preparar listas para o gráfico
dates = [datetime.strptime(date, "%Y-%m-%d") for date in eth_cycles.keys()]
prices = [data["price"] for data in eth_cycles.values()]
labels = [data["event"] for data in eth_cycles.values()]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, marker='o', linestyle='--', color='purple', label='ETH price')

# Adicionar rótulos nos pontos
for i, label in enumerate(labels):
    plt.text(dates[i], prices[i], f"{label}\n${prices[i]}", fontsize=8, ha='left', va='bottom')

plt.title("Ciclos Históricos e Projeções do Ethereum até 2030")
plt.xlabel("Ano")
plt.ylabel("Preço em USD")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
