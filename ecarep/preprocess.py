from __future__ import annotations

import pandas as pd


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reproduce the original preprocessing without changing logic:
    - Create Date index from Year and Month with day=01
    - Sort by Date
    - Compute Total Generation (MU)
    - Return modified DataFrame
    """
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'] + '-01')
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)

    df['Total Generation (MU)'] = (
        df['Wind Generation (MU)']
        + df['Solar Generation (MU)']
        + df['Hydro Generation (MU)']
    )
    return df


def get_energy_types() -> list[str]:
    return [
        'Wind Generation (MU)',
        'Solar Generation (MU)',
        'Hydro Generation (MU)',
        'Total Generation (MU)'
    ]



