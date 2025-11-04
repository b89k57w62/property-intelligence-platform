"""Import property rental data to database"""

import pandas as pd
import argparse
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal
from app.models.property_rental import PropertyRental


def safe_value(val):
    """Convert pandas NaN/numpy NaN to None."""
    if pd.isna(val):
        return None
    return val


def import_rental_file(file_path: str, db, batch_size: int = 1000) -> int:
    """Import single cleaned CSV file to property_rentals table."""
    df = pd.read_csv(file_path)
    df = df.where(pd.notna(df), None)
    total_records = len(df)
    imported_count = 0

    for i in range(0, total_records, batch_size):
        batch_df = df.iloc[i : i + batch_size]
        rentals = []

        for _, row in batch_df.iterrows():
            rental = PropertyRental(
                city=safe_value(row["city"]),
                district=safe_value(row["district"]),
                transaction_target=safe_value(row.get("transaction_target")),
                land_section=safe_value(row.get("land_section")),
                urban_land_use_type=safe_value(row.get("urban_land_use_type")),
                non_urban_land_use_type=safe_value(row.get("non_urban_land_use_type")),
                non_urban_land_use_category=safe_value(
                    row.get("non_urban_land_use_category")
                ),
                building_type=safe_value(row.get("building_type")),
                main_use=safe_value(row.get("main_use")),
                main_building_materials=safe_value(row.get("main_building_materials")),
                construction_complete_date=safe_value(
                    row.get("construction_complete_date")
                ),
                building_rooms=safe_value(row.get("building_rooms")),
                building_halls=safe_value(row.get("building_halls")),
                building_bathrooms=safe_value(row.get("building_bathrooms")),
                building_compartments=safe_value(row.get("building_compartments")),
                has_management=safe_value(row.get("has_management")),
                total_floor_number=safe_value(row.get("total_floor_number")),
                unit_price_ntd=safe_value(row.get("unit_price_ntd")),
                parking_type=safe_value(row.get("parking_type")),
                remarks=safe_value(row.get("remarks")),
                serial_number=safe_value(row.get("serial_number")),
                rental_date=safe_value(row["rental_date"]),
                rental_pen_number=safe_value(row.get("rental_pen_number")),
                land_area_sqm=safe_value(row.get("land_area_sqm")),
                building_area_sqm=safe_value(row.get("building_area_sqm")),
                building_floor_number=safe_value(row.get("building_floor_number")),
                has_furniture=safe_value(row.get("has_furniture")),
                rental_type=safe_value(row.get("rental_type")),
                has_manager=safe_value(row.get("has_manager")),
                rental_period=safe_value(row.get("rental_period")),
                has_elevator=safe_value(row.get("has_elevator")),
                equipment=safe_value(row.get("equipment")),
                rental_service=safe_value(row.get("rental_service")),
                monthly_rent_ntd=safe_value(row["monthly_rent_ntd"]),
                parking_area_sqm=safe_value(row.get("parking_area_sqm")),
                parking_rent_ntd=safe_value(row.get("parking_rent_ntd")),
            )
            rentals.append(rental)

        db.bulk_save_objects(rentals)
        db.commit()
        imported_count += len(rentals)

        progress = (i + len(batch_df)) / total_records * 100
        print(f"  Progress: {progress:.1f}% ({imported_count}/{total_records})")

    return imported_count


def batch_import(input_pattern: str, batch_size: int = 1000):
    """Import multiple CSV files matching pattern."""
    import glob

    db = SessionLocal()

    try:
        files = glob.glob(input_pattern)

        if not files:
            print(f"No files found matching: {input_pattern}")
            return

        total_imported = 0

        for file_path in files:
            print(f"\nImporting: {file_path}")
            count = import_rental_file(file_path, db, batch_size)
            total_imported += count
            print(f"  ✓ Imported {count} records")

        print(f"\n✅ Total: {total_imported} records from {len(files)} files")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input file pattern")
    parser.add_argument("--batch-size", type=int, default=1000, help="Batch size")

    args = parser.parse_args()
    batch_import(args.input, args.batch_size)
