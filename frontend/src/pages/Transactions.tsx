import { useState } from 'react'
import { useTransactions } from '@/hooks/useTransactions'
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

export function Transactions() {
  const [currentPage, setCurrentPage] = useState(1)
  const [filters, setFilters] = useState<{
    city?: string
    district?: string
    price_min?: number
    price_max?: number
    age_min?: number
    age_max?: number
  }>({})
  const pageSize = 20

  const { data, isLoading, error } = useTransactions({
    skip: (currentPage - 1) * pageSize,
    limit: pageSize,
    ...filters,
  })

  const handleSearch = (newFilters: {
    city?: string
    district?: string
    priceMin?: number
    priceMax?: number
    ageMin?: number
    ageMax?: number
  }) => {
    setFilters({
      city: newFilters.city,
      district: newFilters.district,
      price_min: newFilters.priceMin,
      price_max: newFilters.priceMax,
      age_min: newFilters.ageMin,
      age_max: newFilters.ageMax,
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
          Error loading transactions
        </div>
      </PageTransition>
    )
  }

  return (
    <PageTransition>
      <div className="space-y-4">
      <div>
        <h1 className="text-2xl font-bold text-foreground">買賣查詢</h1>
        <p className="text-muted-foreground">
          共 {data?.total || 0} 筆
        </p>
      </div>

      <SearchFilters onSearch={handleSearch} />

      <div className="border rounded-lg overflow-hidden">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>城市</TableHead>
              <TableHead>行政區</TableHead>
              <TableHead>類型</TableHead>
              <TableHead>地址</TableHead>
              <TableHead className="text-right">價格 (元)</TableHead>
              <TableHead className="text-right">面積 (坪)</TableHead>
              <TableHead className="text-right">屋齡 (年)</TableHead>
              <TableHead>日期</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data?.items.map((transaction) => (
              <TableRow key={transaction.id}>
                <TableCell>{transaction.city || '-'}</TableCell>
                <TableCell>{transaction.district || '-'}</TableCell>
                <TableCell>{transaction.transaction_target || '-'}</TableCell>
                <TableCell className="max-w-xs truncate">
                  {transaction.land_section || '-'}
                </TableCell>
                <TableCell className="text-right">
                  {transaction.total_price_ntd ? parseFloat(transaction.total_price_ntd).toLocaleString() : '-'}
                </TableCell>
                <TableCell className="text-right">
                  {transaction.building_area_sqm ? (parseFloat(transaction.building_area_sqm) * 0.3025).toFixed(2) : '-'}
                </TableCell>
                <TableCell className="text-right">
                  {transaction.building_age !== null && transaction.building_age !== undefined ? transaction.building_age : '-'}
                </TableCell>
                <TableCell>{transaction.transaction_date || '-'}</TableCell>
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

