import pandas as pd


def clean_yes_no(value: str) -> bool:
    if pd.isna(value):
        return None
    return value == "有"


def parse_roc_date(date_str) -> str:
    if pd.isna(date_str):
        return None
    return str(int(date_str))


def to_numeric(value):
    return pd.to_numeric(value, errors="coerce")


def clean_string(value: str) -> str:
    if pd.isna(value) or value == "":
        return None
    return str(value).strip()


def has_content(value) -> bool:
    if pd.isna(value):
        return False
    return str(value).strip() != ""
