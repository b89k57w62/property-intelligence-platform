import { QueryClient } from '@tanstack/react-query'
import { AxiosError } from 'axios'

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000,
      retry: (failureCount, error) => {
        if (error instanceof AxiosError) {
          const status = error.response?.status
          if (status === 404 || status === 401 || status === 403) return false
          if (status && status >= 500) return failureCount < 2
          if (!status) return failureCount < 3
        }
        return false
      },
      refetchOnWindowFocus: false,
      throwOnError: false,
    },
  },
})

