import { useQuery } from '@tanstack/react-query'
import { transactionsApi } from '@/lib/api'
import type { SearchParams } from '@/types/property'

export const useTransactions = (params?: SearchParams) => {
  return useQuery({
    queryKey: ['transactions', params],
    queryFn: () => transactionsApi.getAll(params),
  })
}

export const useTransaction = (id: number) => {
  return useQuery({
    queryKey: ['transaction', id],
    queryFn: () => transactionsApi.getById(id),
    enabled: !!id,
  })
}

