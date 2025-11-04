// Base search response type
export interface SearchResponse<T> {
  items: T[]
  total: number
  page: number
  page_size: number
  total_pages: number
}

// Property Transaction
export interface PropertyTransaction {
  id: number
  city: string
  district: string
  transaction_target: string | null
  land_section: string | null
  urban_land_use_type: string | null
  non_urban_land_use_type: string | null
  non_urban_land_use_category: string | null
  building_type: string | null
  main_use: string | null
  main_building_materials: string | null
  construction_complete_date: string | null
  building_rooms: number | null
  building_halls: number | null
  building_bathrooms: number | null
  building_compartments: boolean | null
  has_management: boolean | null
  total_floor_number: number | null
  unit_price_ntd: string | null
  parking_type: string | null
  remarks: string | null
  serial_number: string | null
  transaction_date: string
  transaction_pen_number: string | null
  land_area_sqm: string | null
  building_area_sqm: string | null
  building_floor_number: string | null
  total_price_ntd: string
  parking_area_sqm: string | null
  parking_price_ntd: string | null
  main_building_area: string | null
  auxiliary_building_area: string | null
  balcony_area: string | null
  has_elevator: boolean | null
}

// Property Presale
export interface PropertyPresale {
  id: number
  district: string
  transaction_target: string | null
  land_section: string | null
  urban_land_use_type: string | null
  non_urban_land_use_type: string | null
  non_urban_land_use_category: string | null
  building_type: string | null
  main_use: string | null
  main_building_materials: string | null
  construction_complete_date: string | null
  building_rooms: number | null
  building_halls: number | null
  building_bathrooms: number | null
  building_compartments: boolean | null
  has_management: boolean | null
  total_floor_number: number | null
  unit_price_ntd: string | null
  parking_type: string | null
  remarks: string | null
  serial_number: string | null
  transaction_date: string
  transaction_pen_number: string | null
  land_area_sqm: string | null
  building_area_sqm: string | null
  building_floor_number: string | null
  total_price_ntd: string
  parking_area_sqm: string | null
  parking_price_ntd: string | null
  city: string
  project_name: string | null
  building_number: string | null
  termination_status: string | null
}

// Property Rental
export interface PropertyRental {
  id: number
  district: string
  transaction_target: string | null
  land_section: string | null
  urban_land_use_type: string | null
  non_urban_land_use_type: string | null
  non_urban_land_use_category: string | null
  building_type: string | null
  main_use: string | null
  main_building_materials: string | null
  construction_complete_date: string | null
  building_rooms: number | null
  building_halls: number | null
  building_bathrooms: number | null
  building_compartments: boolean | null
  has_management: boolean | null
  total_floor_number: number | null
  unit_price_ntd: string | null
  parking_type: string | null
  remarks: string | null
  serial_number: string | null
  city: string
  rental_date: string
  rental_pen_number: string | null
  land_area_sqm: string | null
  building_area_sqm: string | null
  building_floor_number: string | null
  has_furniture: boolean | null
  rental_type: string | null
  has_manager: boolean | null
  rental_period: string | null
  has_elevator: boolean | null
  equipment: string | null
  rental_service: string | null
  monthly_rent_ntd: string
  parking_area_sqm: string | null
  parking_rent_ntd: string | null
}

// API search params (for request)
export interface SearchParams {
  skip?: number
  limit?: number
  city?: string
  district?: string
  price_min?: number
  price_max?: number
  order_by?: string
  order_desc?: boolean
}

