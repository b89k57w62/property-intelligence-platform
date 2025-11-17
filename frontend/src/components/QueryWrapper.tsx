import { ReactNode } from 'react'
import { Loader2 } from 'lucide-react'

interface QueryWrapperProps {
  isLoading: boolean
  isError: boolean
  error?: Error | null
  children: ReactNode
  loadingMessage?: string
  errorMessage?: string
}

export function QueryWrapper({
  isLoading,
  isError,
  error,
  children,
  loadingMessage = 'Loading...',
  errorMessage = 'An error occurred',
}: QueryWrapperProps) {
  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="text-center">
          <Loader2 className="h-12 w-12 animate-spin text-primary mx-auto mb-4" />
          <p className="text-muted-foreground">{loadingMessage}</p>
        </div>
      </div>
    )
  }

  if (isError) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="text-center max-w-md">
          <div className="text-destructive text-5xl mb-4">⚠️</div>
          <h3 className="text-lg font-semibold text-foreground mb-2">
            {errorMessage}
          </h3>
          {error && (
            <p className="text-sm text-muted-foreground">{error.message}</p>
          )}
        </div>
      </div>
    )
  }

  return <>{children}</>
}

