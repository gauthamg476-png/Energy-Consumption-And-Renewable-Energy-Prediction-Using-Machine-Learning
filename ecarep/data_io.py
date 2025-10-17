from __future__ import annotations

import io
import pandas as pd


def upload_and_read_excel(sheet_name: str) -> tuple[pd.DataFrame, str]:
    """
    Upload an Excel file using Colab's file upload dialog and read the given sheet.

    Returns (df, file_name). This mirrors the original notebook's behavior.
    """
    # Lazy imports to avoid errors when not in Colab
    from google.colab import files  # type: ignore

    uploaded = files.upload()
    file_name = list(uploaded.keys())[0]
    print(f"Uploaded file: {file_name}")

    df = pd.read_excel(io.BytesIO(uploaded[file_name]), sheet_name=sheet_name)
    return df, file_name



