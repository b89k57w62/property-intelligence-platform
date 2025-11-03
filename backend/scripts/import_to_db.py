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
        batch_df = df.iloc[i : i + batch_size]
        properties = []

        for _, row in batch_df.iterrows():
            prop = Property(
                # Location
                city=row["city"],
                district=row["district"],
                land_location=(
                    row["land_location"] if pd.notna(row["land_location"]) else None
                ),
                land_section=(
                    row["land_section"] if pd.notna(row["land_section"]) else None
                ),
                # Transaction Info
                transaction_date=row["transaction_date"],
                transaction_pen_number=(
                    row["transaction_pen_number"]
                    if pd.notna(row["transaction_pen_number"])
                    else None
                ),
                transaction_target=(
                    row["transaction_target"]
                    if pd.notna(row["transaction_target"])
                    else None
                ),
                # Area Info
                land_area_sqm=(
                    row["land_area_sqm"] if pd.notna(row["land_area_sqm"]) else None
                ),
                urban_land_use_type=(
                    row["urban_land_use_type"]
                    if pd.notna(row["urban_land_use_type"])
                    else None
                ),
                non_urban_land_use_type=(
                    row["non_urban_land_use_type"]
                    if pd.notna(row["non_urban_land_use_type"])
                    else None
                ),
                non_urban_land_use_category=(
                    row["non_urban_land_use_category"]
                    if pd.notna(row["non_urban_land_use_category"])
                    else None
                ),
                transaction_purpose=(
                    row["transaction_purpose"]
                    if pd.notna(row["transaction_purpose"])
                    else None
                ),
                # Building Info
                building_type=(
                    row["building_type"] if pd.notna(row["building_type"]) else None
                ),
                main_use=row["main_use"] if pd.notna(row["main_use"]) else None,
                main_building_materials=(
                    row["main_building_materials"]
                    if pd.notna(row["main_building_materials"])
                    else None
                ),
                construction_complete_date=(
                    row["construction_complete_date"]
                    if pd.notna(row["construction_complete_date"])
                    else None
                ),
                building_area_sqm=(
                    row["building_area_sqm"]
                    if pd.notna(row["building_area_sqm"])
                    else None
                ),
                main_building_area=(
                    row["main_building_area"]
                    if pd.notna(row["main_building_area"])
                    else None
                ),
                auxiliary_building_area=(
                    row["auxiliary_building_area"]
                    if pd.notna(row["auxiliary_building_area"])
                    else None
                ),
                balcony_area=(
                    row["balcony_area"] if pd.notna(row["balcony_area"]) else None
                ),
                building_rooms=(
                    int(row["building_rooms"])
                    if pd.notna(row["building_rooms"])
                    else None
                ),
                building_halls=(
                    int(row["building_halls"])
                    if pd.notna(row["building_halls"])
                    else None
                ),
                building_bathrooms=(
                    int(row["building_bathrooms"])
                    if pd.notna(row["building_bathrooms"])
                    else None
                ),
                building_compartments=(
                    bool(row["building_compartments"])
                    if pd.notna(row["building_compartments"])
                    else None
                ),
                has_management=(
                    bool(row["has_management"])
                    if pd.notna(row["has_management"])
                    else None
                ),
                has_elevator=(
                    bool(row["has_elevator"]) if pd.notna(row["has_elevator"]) else None
                ),
                # Price Info
                total_floor_number=(
                    int(row["total_floor_number"])
                    if pd.notna(row["total_floor_number"])
                    else None
                ),
                building_floor_number=(
                    row["building_floor_number"]
                    if pd.notna(row["building_floor_number"])
                    else None
                ),
                total_price_ntd=row["total_price_ntd"],
                unit_price_ntd=(
                    row["unit_price_ntd"] if pd.notna(row["unit_price_ntd"]) else None
                ),
                parking_type=(
                    row["parking_type"] if pd.notna(row["parking_type"]) else None
                ),
                parking_area_sqm=(
                    row["parking_area_sqm"]
                    if pd.notna(row["parking_area_sqm"])
                    else None
                ),
                parking_price_ntd=(
                    row["parking_price_ntd"]
                    if pd.notna(row["parking_price_ntd"])
                    else None
                ),
                # Additional Info
                remarks=row["remarks"] if pd.notna(row["remarks"]) else None,
                serial_number=(
                    row["serial_number"] if pd.notna(row["serial_number"]) else None
                ),
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
    parser.add_argument(
        "--input", required=True, help="Input file pattern (e.g., data/cleaned/*.csv)"
    )
    parser.add_argument("--batch-size", type=int, default=1000, help="Batch size")

    args = parser.parse_args()

    batch_import(args.input, args.batch_size)
