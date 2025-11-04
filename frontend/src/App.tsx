import { Routes, Route } from 'react-router-dom'
import { Layout } from '@/components/Layout'
import { Home } from '@/pages/Home'
import { Transactions } from '@/pages/Transactions'
import { Presales } from '@/pages/Presales'
import { Rentals } from '@/pages/Rentals'

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/transactions" element={<Transactions />} />
        <Route path="/presales" element={<Presales />} />
        <Route path="/rentals" element={<Rentals />} />
      </Routes>
    </Layout>
  )
}

export default App

