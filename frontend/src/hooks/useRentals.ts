import { useQuery } from '@tanstack/react-query'
import { rentalsApi } from '@/lib/api'
import type { SearchParams } from '@/types/property'

export const useRentals = (params?: SearchParams) => {
  return useQuery({
    queryKey: ['rentals', params],
    queryFn: () => rentalsApi.getAll(params),
  })
}

export const useRental = (id: number) => {
  return useQuery({
    queryKey: ['rental', id],
    queryFn: () => rentalsApi.getById(id),
    enabled: !!id,
  })
}

