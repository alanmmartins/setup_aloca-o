import matplotlib.pyplot as plt # type: ignore
import pandas as pd # type: ignore
from datetime import datetime, timedelta

# Dados dos halvings e ciclos anteriores
halvings = {
    "2012-11-28": {"halving_price": 12, "top_price": 1150, "top_date": "2013-12-01"},
    "2016-07-09": {"halving_price": 650, "top_price": 20000, "top_date": "2017-12-17"},
    "2020-05-11": {"halving_price": 8600, "top_price": 69000, "top_date": "2021-11-10"},
    "2024-04-19": {"halving_price": 63000, "top_price": 200000, "top_date": "2025-11-01"},  # projeção conservadora
    "2028-05-10": {"halving_price": 120000, "top_price": 300000, "top_date": "2029-11-01"}  # projeção conservadora
}

# Construir DataFrame
data = []
for halving_date, info in halvings.items():
    halving_dt = datetime.strptime(halving_date, "%Y-%m-%d")
    if info["top_date"]:
        top_dt = datetime.strptime(info["top_date"], "%Y-%m-%d")
        delta = (top_dt - halving_dt).days
    else:
        # previsão: 1,5 anos após o halving de 2024
        top_dt = halving_dt + timedelta(days=int(1.5 * 365))
        delta = None
    data.append({
        "Halving": halving_dt,
        "Topo": top_dt,
        "Preço Halving": info["halving_price"],
        "Preço Topo": info["top_price"],
        "Dias até o Topo": delta
    })

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df["Halving"], df["Preço Halving"], 'bo-', label="Preço no Halving")
plt.plot(df["Topo"], df["Preço Topo"], 'ro--', label="Preço no Topo (real ou estimado)")

for i, row in df.iterrows():
    plt.text(row["Halving"], row["Preço Halving"], f'{row["Preço Halving"]}', va='bottom', ha='right', fontsize=9)
    if row["Preço Topo"]:
        plt.text(row["Topo"], row["Preço Topo"], f'{row["Preço Topo"]}', va='bottom', ha='left', fontsize=9)

plt.title("Ciclos do Bitcoin: Preço no Halving vs Preço no Topo")
plt.xlabel("Ano")
plt.ylabel("Preço em USD")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.yscale("log")  # escala logarítmica para visualizar melhor
plt.xticks(rotation=45)
plt.show()
