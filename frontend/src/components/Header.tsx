import { Link } from 'react-router-dom'
import { MdDarkMode, MdLightMode } from 'react-icons/md'
import { useTheme } from '@/contexts/ThemeContext'
import { Button } from '@/components/ui/button'

export function Header() {
  const { theme, toggleTheme } = useTheme()

  return (
    <header className="border-b bg-background">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <Link to="/" className="text-xl font-semibold text-foreground hover:text-primary transition-colors">
          Property Intelligence
        </Link>

        <div className="flex items-center gap-6">
          <nav className="flex gap-6">
            <Link
              to="/transactions"
              className="text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Transactions
            </Link>
            <Link
              to="/presales"
              className="text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Presales
            </Link>
            <Link
              to="/rentals"
              className="text-sm font-medium text-foreground hover:text-primary transition-colors"
            >
              Rentals
            </Link>
          </nav>

          <Button
            onClick={toggleTheme}
            variant="ghost"
            size="icon"
            aria-label="Toggle theme"
          >
            {theme === 'light' ? <MdDarkMode size={20} /> : <MdLightMode size={20} />}
          </Button>
        </div>
      </div>
    </header>
  )
}

