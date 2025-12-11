import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_contribution(report, title: str, month: int, year:int):
    entry = report[(report["InvoiceYear"] == year) & (report["InvoiceMonth"] == month)]
    avg_quantity = entry["Quantity"].sum() / len(entry) if len(entry) != 0 else 0
    avg_revenue = entry["Revenue"].sum() / len(entry) if len(entry) != 0 else 0

    _, ax = plt.subplots()
    red_entry = entry[(entry["Quantity"] < avg_quantity) & (entry["Revenue"] < avg_revenue)]
    ax.scatter(entry["Quantity"], entry["Revenue"], color="green", alpha=0.5)
    ax.scatter(red_entry["Quantity"], red_entry["Revenue"], color="red", alpha=0.7)

    if not np.isnan(avg_quantity) and not np.isnan(avg_revenue):
        ax.axhline(avg_revenue, color="green", linestyle="--", label=f"Average Revenue: {avg_revenue:.2f}")
        ax.axvline(avg_quantity, linestyle="--", label=f"Average Quantity: {avg_quantity:.2f}")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Revenue")
    ax.set_title(f"{title} - {month}/{year}")
    ax.legend()
    plt.show();