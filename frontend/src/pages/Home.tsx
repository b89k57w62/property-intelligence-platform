import { Link } from 'react-router-dom'
import { PageTransition } from '@/components/PageTransition'
import { Card, CardHeader, CardTitle, CardDescription } from '@/components/ui/card'

export function Home() {
  return (
    <PageTransition>
      <div className="space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Property Intelligence Platform</h1>
          <p className="text-muted-foreground mt-2">
            Real estate data query and analysis system
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
          <Link to="/transactions">
            <Card className="hover:border-primary hover:shadow-md transition-all cursor-pointer">
              <CardHeader>
                <CardTitle>Transactions</CardTitle>
                <CardDescription>
                  Browse property transaction records
                </CardDescription>
              </CardHeader>
            </Card>
          </Link>

          <Link to="/presales">
            <Card className="hover:border-primary hover:shadow-md transition-all cursor-pointer">
              <CardHeader>
                <CardTitle>Presales</CardTitle>
                <CardDescription>
                  View presale property information
                </CardDescription>
              </CardHeader>
            </Card>
          </Link>

          <Link to="/rentals">
            <Card className="hover:border-primary hover:shadow-md transition-all cursor-pointer">
              <CardHeader>
                <CardTitle>Rentals</CardTitle>
                <CardDescription>
                  Explore rental property data
                </CardDescription>
              </CardHeader>
            </Card>
          </Link>
        </div>
      </div>
    </PageTransition>
  )
}

