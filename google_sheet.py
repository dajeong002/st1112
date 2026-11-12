import pandas as pd


def load_google_sheet(sheet_id, gid=0):
    """Load one publicly accessible Google Sheets tab as a DataFrame."""
    csv_url = (
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/export"
        f"?format=csv&gid={gid}"
    )
    return pd.read_csv(csv_url)


# 사용 예시
# df = load_google_sheet("구글시트_ID", gid=0)
# print(df.head())
