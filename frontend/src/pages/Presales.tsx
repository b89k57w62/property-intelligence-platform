import { useState } from 'react'
import { usePresales } from '@/hooks/usePresales'
import { Pagination } from '@/components/Pagination'
import { SearchFilters } from '@/components/SearchFilters'
import { PageTransition } from '@/components/PageTransition'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

export function Presales() {
  const [currentPage, setCurrentPage] = useState(1)
  const [filters, setFilters] = useState<{
    city?: string
    district?: string
    price_min?: number
    price_max?: number
  }>({})
  const pageSize = 20

  const { data, isLoading, error } = usePresales({
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

  if (isLoading) {
    return (
      <PageTransition>
        <div className="text-center py-8 text-foreground">Loading...</div>
      </PageTransition>
    )
  }

  if (error) {
    return (
      <PageTransition>
        <div className="text-center py-8 text-destructive">
          Error loading presales
        </div>
      </PageTransition>
    )
  }

  return (
    <PageTransition>
      <div className="space-y-4">
      <div>
        <h1 className="text-2xl font-bold text-foreground">預售屋查詢</h1>
        <p className="text-muted-foreground">
          共 {data?.total || 0} 筆
        </p>
      </div>

      <SearchFilters onSearch={handleSearch} />

      <div className="border rounded-lg overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Project</TableHead>
              <TableHead>City</TableHead>
              <TableHead>District</TableHead>
              <TableHead>Location</TableHead>
              <TableHead className="text-right">Price (NTD)</TableHead>
              <TableHead className="text-right">Area (m²)</TableHead>
              <TableHead>Date</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data?.items.map((presale) => (
              <TableRow key={presale.id}>
                <TableCell className="font-medium">
                  {presale.project_name || '-'}
                </TableCell>
                <TableCell>{presale.city || '-'}</TableCell>
                <TableCell>{presale.district || '-'}</TableCell>
                <TableCell className="max-w-xs truncate">
                  {presale.land_section || '-'}
                </TableCell>
                <TableCell className="text-right">
                  {presale.total_price_ntd ? parseFloat(presale.total_price_ntd).toLocaleString() : '-'}
                </TableCell>
                <TableCell className="text-right">
                  {presale.building_area_sqm ? parseFloat(presale.building_area_sqm).toFixed(2) : '-'}
                </TableCell>
                <TableCell>{presale.transaction_date || '-'}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>

        <Pagination
          currentPage={currentPage}
          totalPages={data?.total_pages || 1}
          onPageChange={setCurrentPage}
        />
      </div>
    </div>
    </PageTransition>
  )
}

