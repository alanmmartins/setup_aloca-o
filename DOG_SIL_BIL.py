import matplotlib.pyplot as plt
from datetime import datetime

# Dados estimados e reais (valores fictícios para Billy e Silly, por falta de dados públicos)
cycles = {
    "2024-04-20": {"DOG": 0.0045, "Billy": 0.0003, "Silly": 0.0002},
    "2024-12-11": {"DOG": 0.00995, "Billy": 0.0020, "Silly": 0.0010},
    "2025-04-07": {"DOG": 0.0010, "Billy": 0.0008, "Silly": 0.0003},
    "2026-12-01": {"DOG": 0.0040, "Billy": 0.0050, "Silly": 0.0015},
    "2028-06-01": {"DOG": 0.0015, "Billy": 0.0020, "Silly": 0.0005},
    "2030-01-01": {"DOG": 0.0080, "Billy": 0.0100, "Silly": 0.0030}
}

dates = [datetime.strptime(date, "%Y-%m-%d") for date in cycles]
dog_prices = [v["DOG"] for v in cycles.values()]
billy_prices = [v["Billy"] for v in cycles.values()]
silly_prices = [v["Silly"] for v in cycles.values()]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(dates, dog_prices, marker='o', linestyle='--', label='DOG (Bitcoin)', color='orange')
plt.plot(dates, billy_prices, marker='s', linestyle='--', label='Billy (Runes)', color='blue')
plt.plot(dates, silly_prices, marker='^', linestyle='--', label='Silly (Runes)', color='purple')

plt.title("Comparativo de Projeção: DOG vs Billy vs Silly até 2030")
plt.xlabel("Ano")
plt.ylabel("Preço estimado (USD)")
plt.yscale("log")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
