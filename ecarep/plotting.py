from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns


def configure_style() -> None:
    plt.style.use('default')
    sns.set_palette("husl")
    print("All libraries imported successfully!")



