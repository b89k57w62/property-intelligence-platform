import { useState } from 'react'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

interface SearchFiltersProps {
  onSearch: (filters: {
    city?: string
    district?: string
    priceMin?: number
    priceMax?: number
  }) => void
}

export function SearchFilters({ onSearch }: SearchFiltersProps) {
  const [city, setCity] = useState('')
  const [district, setDistrict] = useState('')
  const [priceMin, setPriceMin] = useState('')
  const [priceMax, setPriceMax] = useState('')
  const [isExpanded, setIsExpanded] = useState(false)

  const handleSearch = () => {
    onSearch({
      city: city || undefined,
      district: district || undefined,
      priceMin: priceMin ? parseInt(priceMin) : undefined,
      priceMax: priceMax ? parseInt(priceMax) : undefined,
    })
  }

  const handleReset = () => {
    setCity('')
    setDistrict('')
    setPriceMin('')
    setPriceMax('')
    onSearch({})
  }

  return (
    <Card className="mb-4">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>Search Filters</CardTitle>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setIsExpanded(!isExpanded)}
          >
            {isExpanded ? 'Collapse' : 'Expand'}
          </Button>
        </div>
      </CardHeader>

      {isExpanded && (
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="space-y-2">
              <label className="text-sm font-medium">City</label>
              <Input
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="e.g. 台北市"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">District</label>
              <Input
                type="text"
                value={district}
                onChange={(e) => setDistrict(e.target.value)}
                placeholder="e.g. 中正區"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">Min Price (NTD)</label>
              <Input
                type="number"
                value={priceMin}
                onChange={(e) => setPriceMin(e.target.value)}
                placeholder="0"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium">Max Price (NTD)</label>
              <Input
                type="number"
                value={priceMax}
                onChange={(e) => setPriceMax(e.target.value)}
                placeholder="999999999"
              />
            </div>
          </div>

          <div className="flex gap-2">
            <Button onClick={handleSearch}>
              Search
            </Button>
            <Button onClick={handleReset} variant="outline">
              Reset
            </Button>
          </div>
        </CardContent>
      )}
    </Card>
  )
}

