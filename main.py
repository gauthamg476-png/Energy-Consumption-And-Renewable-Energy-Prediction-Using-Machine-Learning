import warnings
warnings.filterwarnings('ignore')

import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error,
)
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

from ecarep.plotting import configure_style
from ecarep.data_io import upload_and_read_excel
from ecarep.preprocess import prepare_dataframe, get_energy_types


def main() -> None:
    # Set style for plots and print import success message (matches original behavior)
    configure_style()

    # Upload and read Excel (Colab flow)
    df, _file_name = upload_and_read_excel(sheet_name='TN_RE_2019_2024')

    # Display basic info (matches original)
    print("Dataset Overview:")
    print(df.head())
    print(f"\nDataset shape: {df.shape}")

    # Prepare dataframe (date index, sorting, totals)
    df = prepare_dataframe(df)

    # Energy types list (unchanged)
    energy_types = get_energy_types()
    _ = energy_types  # referenced to preserve original variable presence

    print("\nData preparation complete!")
    print(f"Date range: {df.index.min()} to {df.index.max()}")
    print(f"Final dataset shape: {df.shape}")


if __name__ == '__main__':
    main()


