"""Clean rental data (c_lvr_land_c.csv files)"""

import pandas as pd
import argparse
import glob
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from app.etl.transformers import clean_yes_no, parse_roc_date, to_numeric, clean_string
from app.etl.district_mapping import get_city_from_district


def clean_rental_file(input_path: str, output_path: str) -> int:
    """Clean single rental CSV file."""
    df = pd.read_csv(input_path, skiprows=[1])

    df["city"] = df["鄉鎮市區"].apply(get_city_from_district)

    cleaned_df = pd.DataFrame(
        {
            "city": df["city"],
            "district": df["鄉鎮市區"],
            "transaction_target": df["交易標的"].apply(clean_string),
            "land_section": df["土地位置建物門牌"].apply(clean_string),
            "urban_land_use_type": df["都市土地使用分區"].apply(clean_string),
            "non_urban_land_use_type": df["非都市土地使用分區"].apply(clean_string),
            "non_urban_land_use_category": df["非都市土地使用編定"].apply(clean_string),
            "building_type": df["建物型態"].apply(clean_string),
            "main_use": df["主要用途"].apply(clean_string),
            "main_building_materials": df["主要建材"].apply(clean_string),
            "construction_complete_date": df["建築完成年月"].apply(clean_string),
            "building_rooms": df["建物現況格局-房"].apply(to_numeric),
            "building_halls": df["建物現況格局-廳"].apply(to_numeric),
            "building_bathrooms": df["建物現況格局-衛"].apply(to_numeric),
            "building_compartments": df["建物現況格局-隔間"].apply(clean_yes_no),
            "has_management": df["有無管理組織"].apply(clean_yes_no),
            "total_floor_number": df["總樓層數"].apply(to_numeric),
            "unit_price_ntd": df["單價元平方公尺"].apply(to_numeric),
            "parking_type": df["車位類別"].apply(clean_string),
            "remarks": df["備註"].apply(clean_string),
            "serial_number": df["編號"],
            "rental_date": df["租賃年月日"].apply(parse_roc_date),
            "rental_pen_number": df["租賃筆棟數"].apply(clean_string),
            "land_area_sqm": df["土地面積平方公尺"].apply(to_numeric),
            "building_area_sqm": df["建物總面積平方公尺"].apply(to_numeric),
            "building_floor_number": df["租賃層次"].apply(clean_string),
            "has_furniture": df["有無附傢俱"].apply(clean_yes_no),
            "rental_type": df["出租型態"].apply(clean_string),
            "has_manager": df["有無管理員"].apply(clean_yes_no),
            "rental_period": df["租賃期間"].apply(clean_string),
            "has_elevator": df["有無電梯"].apply(clean_yes_no),
            "equipment": df["附屬設備"].apply(clean_string),
            "rental_service": df["租賃住宅服務"].apply(clean_string),
            "monthly_rent_ntd": df["總額元"].apply(to_numeric),
            "parking_area_sqm": df["車位面積平方公尺"].apply(to_numeric),
            "parking_rent_ntd": df["車位總額元"].apply(to_numeric),
        }
    )

    cleaned_df = cleaned_df.dropna(
        subset=["city", "district", "rental_date", "monthly_rent_ntd"]
    )

    cleaned_df.to_csv(output_path, index=False)
    return len(cleaned_df)


def batch_clean(input_pattern: str, output_dir: str):
    """Clean multiple rental CSV files."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    files = glob.glob(input_pattern)

    if not files:
        print(f"No files found matching: {input_pattern}")
        return

    total_records = 0

    for file_path in files:
        filename = Path(file_path).stem
        output_path = f"{output_dir}/{filename}_cleaned.csv"

        print(f"Processing: {file_path}")
        count = clean_rental_file(file_path, output_path)
        total_records += count
        print(f"  ✓ Cleaned {count} records → {output_path}")

    print(f"\n✅ Total: {total_records} records from {len(files)} files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", required=True, help="Input file pattern (e.g., data/raw/*_c.csv)"
    )
    parser.add_argument(
        "--output", default="data/cleaned/rentals", help="Output directory"
    )

    args = parser.parse_args()
    batch_clean(args.input, args.output)
