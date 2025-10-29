import pandas as pd
import argparse
import glob
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from app.etl.transformers import clean_yes_no, parse_roc_date, to_numeric, clean_string, has_content


def clean_single_file(input_path: str, output_path: str) -> int:
    df = pd.read_csv(input_path, skiprows=[1])

    cleaned_df = pd.DataFrame({
        'city': df['縣市'] if '縣市' in df.columns else None,
        'district': df['鄉鎮市區'],
        'transaction_target': df['交易標的'].apply(clean_string),
        'address': df['土地位置建物門牌'].apply(clean_string),
        'transaction_date': df['交易年月日'].apply(parse_roc_date),
        'transaction_count': df['交易筆棟數'].apply(clean_string),
        'land_area_sqm': df['土地移轉總面積平方公尺'].apply(to_numeric),
        'urban_land_use': df['都市土地使用分區'].apply(clean_string),
        'non_urban_land_use': df['非都市土地使用分區'].apply(clean_string),
        'non_urban_land_use_code': df['非都市土地使用編定'].apply(clean_string),
        'building_type': df['建物型態'].apply(clean_string),
        'main_usage': df['主要用途'].apply(clean_string),
        'main_material': df['主要建材'].apply(clean_string),
        'construction_date': df['建築完成年月'].apply(clean_string),
        'floor_transfer': df['移轉層次'].apply(clean_string),
        'total_floors': df['總樓層數'].apply(to_numeric),
        'building_area_sqm': df['建物移轉總面積平方公尺'].apply(to_numeric),
        'main_building_area': df['主建物面積'].apply(to_numeric),
        'auxiliary_area': df['附屬建物面積'].apply(to_numeric),
        'balcony_area': df['陽台面積'].apply(to_numeric),
        'room_count': df['建物現況格局-房'].apply(to_numeric),
        'living_count': df['建物現況格局-廳'].apply(to_numeric),
        'bathroom_count': df['建物現況格局-衛'].apply(to_numeric),
        'compartment': df['建物現況格局-隔間'].apply(clean_string),
        'total_price_ntd': df['總價元'].apply(to_numeric),
        'unit_price_sqm': df['單價元平方公尺'].apply(to_numeric),
        'parking_type': df['車位類別'].apply(clean_string),
        'parking_area_sqm': df['車位移轉總面積平方公尺'].apply(to_numeric),
        'parking_price_ntd': df['車位總價元'].apply(to_numeric),
        'has_elevator': df['電梯'].apply(clean_yes_no),
        'has_management': df['有無管理組織'].apply(clean_yes_no),
        'has_note': df['備註'].apply(has_content),
        'note': df['備註'].apply(clean_string),
        'serial_number': df['編號'],
        'transfer_number': df['移轉編號'].apply(clean_string),
    })

    cleaned_df = cleaned_df.dropna(subset=['district', 'transaction_date', 'total_price_ntd'])

    cleaned_df.to_csv(output_path, index=False)

    return len(cleaned_df)


def batch_clean(input_pattern: str, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    files = glob.glob(input_pattern)

    if not files:
        print(f"No files found matching pattern: {input_pattern}")
        return

    total_records = 0

    for file_path in files:
        filename = Path(file_path).stem
        output_path = f"{output_dir}/{filename}_cleaned.csv"

        print(f"Processing: {file_path}")
        count = clean_single_file(file_path, output_path)
        total_records += count
        print(f"  ✓ Cleaned {count} records → {output_path}")

    print(f"\n✅ Total: {total_records} records from {len(files)} files")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input file pattern (e.g., data/raw/*.csv)')
    parser.add_argument('--output', default='data/cleaned', help='Output directory')

    args = parser.parse_args()

    batch_clean(args.input, args.output)
