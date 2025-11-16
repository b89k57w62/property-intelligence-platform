import { useState } from 'react'
import { MdSearch, MdRefresh, MdExpandMore, MdExpandLess, MdLocationCity, MdLocationOn, MdAttachMoney, MdHome } from 'react-icons/md'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

interface SearchFiltersProps {
  onSearch: (filters: {
    city?: string
    district?: string
    priceMin?: number
    priceMax?: number
    ageMin?: number
    ageMax?: number
  }) => void
}

export function SearchFilters({ onSearch }: SearchFiltersProps) {
  const [city, setCity] = useState('')
  const [district, setDistrict] = useState('')
  const [priceMin, setPriceMin] = useState('')
  const [priceMax, setPriceMax] = useState('')
  const [ageMin, setAgeMin] = useState('')
  const [ageMax, setAgeMax] = useState('')
  const [isExpanded, setIsExpanded] = useState(false)

  const handleSearch = () => {
    onSearch({
      city: city || undefined,
      district: district || undefined,
      priceMin: priceMin ? parseInt(priceMin) : undefined,
      priceMax: priceMax ? parseInt(priceMax) : undefined,
      ageMin: ageMin ? parseInt(ageMin) : undefined,
      ageMax: ageMax ? parseInt(ageMax) : undefined,
    })
  }

  const handleReset = () => {
    setCity('')
    setDistrict('')
    setPriceMin('')
    setPriceMax('')
    setAgeMin('')
    setAgeMax('')
    onSearch({})
  }

  return (
    <Card className="mb-4">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>搜尋篩選</CardTitle>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setIsExpanded(!isExpanded)}
            className="flex items-center gap-1"
          >
            {isExpanded ? (
              <>
                收起 <MdExpandLess size={18} />
              </>
            ) : (
              <>
                展開 <MdExpandMore size={18} />
              </>
            )}
          </Button>
        </div>
      </CardHeader>

      {isExpanded && (
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdLocationCity size={16} className="text-primary" />
                城市
              </label>
              <Input
                type="text"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                placeholder="e.g. 台北市"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdLocationOn size={16} className="text-primary" />
                行政區
              </label>
              <Input
                type="text"
                value={district}
                onChange={(e) => setDistrict(e.target.value)}
                placeholder="e.g. 中正區"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdAttachMoney size={16} className="text-primary" />
                最低價格 (元)
              </label>
              <Input
                type="number"
                value={priceMin}
                onChange={(e) => setPriceMin(e.target.value)}
                placeholder="0"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdAttachMoney size={16} className="text-primary" />
                最高價格 (元)
              </label>
              <Input
                type="number"
                value={priceMax}
                onChange={(e) => setPriceMax(e.target.value)}
                placeholder="999999999"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdHome size={16} className="text-primary" />
                最小屋齡 (年)
              </label>
              <Input
                type="number"
                value={ageMin}
                onChange={(e) => setAgeMin(e.target.value)}
                placeholder="0"
                min="0"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium flex items-center gap-1">
                <MdHome size={16} className="text-primary" />
                最大屋齡 (年)
              </label>
              <Input
                type="number"
                value={ageMax}
                onChange={(e) => setAgeMax(e.target.value)}
                placeholder="100"
                min="0"
              />
            </div>
          </div>

          <div className="flex gap-2">
            <Button onClick={handleSearch} className="flex items-center gap-1">
              <MdSearch size={18} />
              搜尋
            </Button>
            <Button onClick={handleReset} variant="outline" className="flex items-center gap-1">
              <MdRefresh size={18} />
              重置
            </Button>
          </div>
        </CardContent>
      )}
    </Card>
  )
}
