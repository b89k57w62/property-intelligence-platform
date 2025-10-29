import pandas as pd
import argparse
import glob
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal
from app.models.property import Property


def import_single_file(file_path: str, db, batch_size: int = 1000) -> int:
    df = pd.read_csv(file_path)

    total_records = len(df)
    imported_count = 0

    for i in range(0, total_records, batch_size):
        batch_df = df.iloc[i:i+batch_size]
        properties = []

        for _, row in batch_df.iterrows():
            prop = Property(
                city=row['city'] if pd.notna(row['city']) else None,
                district=row['district'],
                transaction_target=row['transaction_target'] if pd.notna(row['transaction_target']) else None,
                address=row['address'] if pd.notna(row['address']) else None,
                transaction_date=row['transaction_date'],
                transaction_count=row['transaction_count'] if pd.notna(row['transaction_count']) else None,
                land_area_sqm=row['land_area_sqm'] if pd.notna(row['land_area_sqm']) else None,
                urban_land_use=row['urban_land_use'] if pd.notna(row['urban_land_use']) else None,
                non_urban_land_use=row['non_urban_land_use'] if pd.notna(row['non_urban_land_use']) else None,
                non_urban_land_use_code=row['non_urban_land_use_code'] if pd.notna(row['non_urban_land_use_code']) else None,
                building_type=row['building_type'] if pd.notna(row['building_type']) else None,
                main_usage=row['main_usage'] if pd.notna(row['main_usage']) else None,
                main_material=row['main_material'] if pd.notna(row['main_material']) else None,
                construction_date=row['construction_date'] if pd.notna(row['construction_date']) else None,
                floor_transfer=row['floor_transfer'] if pd.notna(row['floor_transfer']) else None,
                total_floors=int(row['total_floors']) if pd.notna(row['total_floors']) else None,
                building_area_sqm=row['building_area_sqm'] if pd.notna(row['building_area_sqm']) else None,
                main_building_area=row['main_building_area'] if pd.notna(row['main_building_area']) else None,
                auxiliary_area=row['auxiliary_area'] if pd.notna(row['auxiliary_area']) else None,
                balcony_area=row['balcony_area'] if pd.notna(row['balcony_area']) else None,
                room_count=int(row['room_count']) if pd.notna(row['room_count']) else None,
                living_count=int(row['living_count']) if pd.notna(row['living_count']) else None,
                bathroom_count=int(row['bathroom_count']) if pd.notna(row['bathroom_count']) else None,
                compartment=row['compartment'] if pd.notna(row['compartment']) else None,
                total_price_ntd=int(row['total_price_ntd']),
                unit_price_sqm=row['unit_price_sqm'] if pd.notna(row['unit_price_sqm']) else None,
                parking_type=row['parking_type'] if pd.notna(row['parking_type']) else None,
                parking_area_sqm=row['parking_area_sqm'] if pd.notna(row['parking_area_sqm']) else None,
                parking_price_ntd=int(row['parking_price_ntd']) if pd.notna(row['parking_price_ntd']) else None,
                has_elevator=row['has_elevator'] if pd.notna(row['has_elevator']) else None,
                has_management=row['has_management'] if pd.notna(row['has_management']) else None,
                has_note=row['has_note'] if pd.notna(row['has_note']) else None,
                note=row['note'] if pd.notna(row['note']) else None,
                serial_number=row['serial_number'] if pd.notna(row['serial_number']) else None,
                transfer_number=row['transfer_number'] if pd.notna(row['transfer_number']) else None,
            )
            properties.append(prop)

        db.bulk_save_objects(properties)
        db.commit()
        imported_count += len(properties)

        progress = (i + len(batch_df)) / total_records * 100
        print(f"  Progress: {progress:.1f}% ({imported_count}/{total_records})")

    return imported_count


def batch_import(input_pattern: str, batch_size: int = 1000):
    db = SessionLocal()

    try:
        files = glob.glob(input_pattern)

        if not files:
            print(f"No files found matching pattern: {input_pattern}")
            return

        total_imported = 0

        for file_path in files:
            print(f"\nImporting: {file_path}")
            count = import_single_file(file_path, db, batch_size)
            total_imported += count
            print(f"  ✓ Imported {count} records")

        print(f"\n✅ Total imported: {total_imported} records from {len(files)} files")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input file pattern (e.g., data/cleaned/*.csv)')
    parser.add_argument('--batch-size', type=int, default=1000, help='Batch size')

    args = parser.parse_args()

    batch_import(args.input, args.batch_size)
