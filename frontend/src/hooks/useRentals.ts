import { useQuery, useQueryClient } from '@tanstack/react-query'
import { rentalsApi } from '@/lib/api'
import { queryKeys } from '@/lib/queryKeys'
import type { SearchParams } from '@/types/property'

export const useRentals = (params?: SearchParams) => {
  const queryClient = useQueryClient()

  const query = useQuery({
    queryKey: queryKeys.rentals.list(params),
    queryFn: () => rentalsApi.getAll(params),
  })

  const prefetchNextPage = (nextPage: number, pageSize: number) => {
    const nextParams = {
      ...params,
      skip: (nextPage - 1) * pageSize,
      limit: pageSize,
    }
    queryClient.prefetchQuery({
      queryKey: queryKeys.rentals.list(nextParams),
      queryFn: () => rentalsApi.getAll(nextParams),
    })
  }

  return { ...query, prefetchNextPage }
}

export const useRental = (id: number) => {
  return useQuery({
    queryKey: queryKeys.rentals.detail(id),
    queryFn: () => rentalsApi.getById(id),
    enabled: !!id,
  })
}

