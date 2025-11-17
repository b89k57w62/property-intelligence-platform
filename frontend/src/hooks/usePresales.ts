import { useQuery, useQueryClient } from '@tanstack/react-query'
import { presalesApi } from '@/lib/api'
import { queryKeys } from '@/lib/queryKeys'
import type { SearchParams } from '@/types/property'

export const usePresales = (params?: SearchParams) => {
  const queryClient = useQueryClient()

  const query = useQuery({
    queryKey: queryKeys.presales.list(params),
    queryFn: () => presalesApi.getAll(params),
  })

  const prefetchNextPage = (nextPage: number, pageSize: number) => {
    const nextParams = {
      ...params,
      skip: (nextPage - 1) * pageSize,
      limit: pageSize,
    }
    queryClient.prefetchQuery({
      queryKey: queryKeys.presales.list(nextParams),
      queryFn: () => presalesApi.getAll(nextParams),
    })
  }

  return { ...query, prefetchNextPage }
}

export const usePresale = (id: number) => {
  return useQuery({
    queryKey: queryKeys.presales.detail(id),
    queryFn: () => presalesApi.getById(id),
    enabled: !!id,
  })
}

