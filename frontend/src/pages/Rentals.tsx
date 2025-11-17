import { useState } from 'react'
import { useRentals } from '@/hooks/useRentals'
import { Pagination } from '@/components/Pagination'
import { SearchFilters } from '@/components/SearchFilters'
import { PageTransition } from '@/components/PageTransition'
import { QueryWrapper } from '@/components/QueryWrapper'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

export function Rentals() {
  const [currentPage, setCurrentPage] = useState(1)
  const [filters, setFilters] = useState<{
    city?: string
    district?: string
    price_min?: number
    price_max?: number
  }>({})
  const pageSize = 20

  const { data, isLoading, error, prefetchNextPage } = useRentals({
    skip: (currentPage - 1) * pageSize,
    limit: pageSize,
    ...filters,
  })

  const handleSearch = (newFilters: {
    city?: string
    district?: string
    priceMin?: number
    priceMax?: number
  }) => {
    setFilters({
      city: newFilters.city,
      district: newFilters.district,
      price_min: newFilters.priceMin,
      price_max: newFilters.priceMax,
    })
    setCurrentPage(1)
  }

  return (
    <PageTransition>
      <QueryWrapper
        isLoading={isLoading}
        isError={!!error}
        error={error}
        loadingMessage="載入租賃資料中..."
        errorMessage="無法載入租賃資料"
      >
        <div className="space-y-4">
          <div>
            <h1 className="text-2xl font-bold text-foreground">租賃查詢</h1>
            <p className="text-muted-foreground">
              共 {data?.total || 0} 筆
            </p>
          </div>

          <SearchFilters onSearch={handleSearch} />

          <div className="border rounded-lg overflow-hidden">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>City</TableHead>
                  <TableHead>District</TableHead>
                  <TableHead>Type</TableHead>
                  <TableHead className="text-right">Area (m²)</TableHead>
                  <TableHead className="text-right">Monthly Rent (NTD)</TableHead>
                  <TableHead>Furniture</TableHead>
                  <TableHead>Date</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {data?.items.map((rental) => (
                  <TableRow key={rental.id}>
                    <TableCell>{rental.city || '-'}</TableCell>
                    <TableCell>{rental.district || '-'}</TableCell>
                    <TableCell className="max-w-xs truncate">
                      {rental.transaction_target || '-'}
                    </TableCell>
                    <TableCell className="text-right">
                      {rental.building_area_sqm ? parseFloat(rental.building_area_sqm).toFixed(2) : '-'}
                    </TableCell>
                    <TableCell className="text-right">
                      {rental.monthly_rent_ntd ? parseFloat(rental.monthly_rent_ntd).toLocaleString() : '-'}
                    </TableCell>
                    <TableCell>
                      {rental.has_furniture ? 'Yes' : 'No'}
                    </TableCell>
                    <TableCell>{rental.rental_date || '-'}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>

            <Pagination
              currentPage={currentPage}
              totalPages={data?.total_pages || 1}
              onPageChange={setCurrentPage}
              onPageHover={(page) => prefetchNextPage(page, pageSize)}
            />
          </div>
        </div>
      </QueryWrapper>
    </PageTransition>
  )
}

