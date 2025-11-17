import { useQuery, useQueryClient } from '@tanstack/react-query'
import { transactionsApi } from '@/lib/api'
import { queryKeys } from '@/lib/queryKeys'
import type { SearchParams } from '@/types/property'

export const useTransactions = (params?: SearchParams) => {
  const queryClient = useQueryClient()

  const query = useQuery({
    queryKey: queryKeys.transactions.list(params),
    queryFn: () => transactionsApi.getAll(params),
  })

  const prefetchNextPage = (nextPage: number, pageSize: number) => {
    const nextParams = {
      ...params,
      skip: (nextPage - 1) * pageSize,
      limit: pageSize,
    }
    queryClient.prefetchQuery({
      queryKey: queryKeys.transactions.list(nextParams),
      queryFn: () => transactionsApi.getAll(nextParams),
    })
  }

  return { ...query, prefetchNextPage }
}

export const useTransaction = (id: number) => {
  return useQuery({
    queryKey: queryKeys.transactions.detail(id),
    queryFn: () => transactionsApi.getById(id),
    enabled: !!id,
  })
}

