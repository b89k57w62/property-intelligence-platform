import type { SearchParams } from '@/types/property'

export const queryKeys = {
  transactions: {
    all: ['transactions'] as const,
    lists: () => [...queryKeys.transactions.all, 'list'] as const,
    list: (params?: SearchParams) => [...queryKeys.transactions.lists(), params] as const,
    details: () => [...queryKeys.transactions.all, 'detail'] as const,
    detail: (id: number) => [...queryKeys.transactions.details(), id] as const,
  },
  presales: {
    all: ['presales'] as const,
    lists: () => [...queryKeys.presales.all, 'list'] as const,
    list: (params?: SearchParams) => [...queryKeys.presales.lists(), params] as const,
    details: () => [...queryKeys.presales.all, 'detail'] as const,
    detail: (id: number) => [...queryKeys.presales.details(), id] as const,
  },
  rentals: {
    all: ['rentals'] as const,
    lists: () => [...queryKeys.rentals.all, 'list'] as const,
    list: (params?: SearchParams) => [...queryKeys.rentals.lists(), params] as const,
    details: () => [...queryKeys.rentals.all, 'detail'] as const,
    detail: (id: number) => [...queryKeys.rentals.details(), id] as const,
  },
}

