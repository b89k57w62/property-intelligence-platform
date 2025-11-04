// Base search response type
export interface SearchResponse<T> {
  items: T[]
  total: number
  page: number
  size: number
  pages: number
}

// Property Transaction
export interface PropertyTransaction {
  id: number
  city: string | null
  district: string | null
  transaction_sign: string | null
  land_location: string | null
  land_area_sqm: number | null
  district_land_use_zoning: string | null
  non_district_land_use: string | null
  transaction_date: string | null
  transaction_pen_number: string | null
  transaction_floor_number: string | null
  total_floor_number: string | null
  building_state: string | null
  main_use: string | null
  main_building_materials: string | null
  construction_complete_date: string | null
  building_area_sqm: number | null
  building_room_count: number | null
  building_hall_count: number | null
  building_compartment_count: number | null
  has_management_organization: string | null
  total_price_ntd: number | null
  unit_price_ntd_per_sqm: number | null
  berth_category: string | null
  berth_area_sqm: number | null
  berth_total_price_ntd: number | null
  note: string | null
  serial_number: string | null
  building_types: string | null
  parking_space_types: string | null
  has_elevator: string | null
}

// Property Presale
export interface PropertyPresale {
  id: number
  city: string | null
  district: string | null
  transaction_sign: string | null
  land_location_building_number: string | null
  land_area_sqm: number | null
  district_land_use_zoning: string | null
  non_district_land_use: string | null
  transaction_date: string | null
  transaction_pen_number: string | null
  transaction_floor_number: string | null
  building_area_sqm: number | null
  building_room_count: number | null
  building_hall_count: number | null
  building_compartment_count: number | null
  has_management_organization: string | null
  total_price_ntd: number | null
  unit_price_ntd_per_sqm: number | null
  berth_category: string | null
  berth_total_price_ntd: number | null
  note: string | null
  serial_number: string | null
  project_name: string | null
  building_types: string | null
  total_floor_number: string | null
  building_material: string | null
  construction_company: string | null
  construction_complete_date: string | null
  construction_license_number: string | null
  termination_status: string | null
}

// Property Rental
export interface PropertyRental {
  id: number
  city: string | null
  district: string | null
  transaction_sign: string | null
  berth_category: string | null
  rental_area_sqm: number | null
  berth_area_sqm: number | null
  rental_date: string | null
  rental_floor_number: string | null
  total_floor_number: string | null
  building_state: string | null
  main_use: string | null
  main_building_materials: string | null
  construction_complete_date: string | null
  building_room_count: number | null
  building_hall_count: number | null
  building_compartment_count: number | null
  has_management_organization: string | null
  rental_type: string | null
  rental_scope: string | null
  monthly_rent_ntd: number | null
  note: string | null
  serial_number: string | null
  transaction_object: string | null
  building_types: string | null
  use_partition: string | null
  berth_types: string | null
  berth_count: number | null
  has_furniture: string | null
  equipment_list: string | null
  total_berth_rent_ntd: number | null
  manager: string | null
  rental_level: string | null
}

// API search params
export interface SearchParams {
  page?: number
  limit?: number
  city?: string
  district?: string
  price_min?: number
  price_max?: number
  order_by?: string
  order_desc?: boolean
}

