import matplotlib.pyplot as plt
from datetime import datetime

dog_cycles = {
  "2024-04-20": {"event": "Lançamento", "price": 0.0045},
  "2024-12-11": {"event": "Topo #1 (real)", "price": 0.00995},
  "2025-04-07": {"event": "Fundo #1 (real)", "price": 0.0010},
  "2026-12-01": {"event": "Topo #2 (proj.)", "price": 0.0040},
  "2028-06-01": {"event": "Fundo #2 (proj.)", "price": 0.0015},
  "2030-01-01": {"event": "Topo #3 (proj.)", "price": 0.0080},
}

dates = [datetime.fromisoformat(d) for d in dog_cycles]
prices = [v["price"] for v in dog_cycles.values()]
labels = [v["event"] for v in dog_cycles.values()]

plt.figure(figsize=(8,5))
plt.plot(dates, prices, marker='o', linestyle='--')
for d,p,l in zip(dates, prices, labels):
    plt.text(d, p, f"{l}\n${p:.4f}", fontsize=8)
plt.yscale("log")
plt.grid(True)
plt.title("Projeção DOG (Ordinals) até 2030")
plt.xlabel("Ano"); plt.ylabel("USD")
plt.show()
