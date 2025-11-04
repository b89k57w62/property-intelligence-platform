import { useQuery } from '@tanstack/react-query'
import { presalesApi } from '@/lib/api'
import type { SearchParams } from '@/types/property'

export const usePresales = (params?: SearchParams) => {
  return useQuery({
    queryKey: ['presales', params],
    queryFn: () => presalesApi.getAll(params),
  })
}

export const usePresale = (id: number) => {
  return useQuery({
    queryKey: ['presale', id],
    queryFn: () => presalesApi.getById(id),
    enabled: !!id,
  })
}

