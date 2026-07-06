import React, { useEffect, useState } from 'react'

export default function ProductList() {
  const [dbStatus, setDbStatus] = useState(null)
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // The backend currently exposes `/db-check` and `/` endpoints.
    // This fetch demonstrates connectivity; later you can point to /api/products.
    async function check() {
      setLoading(true)
      try {
        const res = await fetch('/db-check')
        const data = await res.json()
        setDbStatus(data)
      } catch (err) {
        setDbStatus({ database: 'failed', error: err.message })
      }

      // demo/mock products while backend product endpoints are implemented
      setProducts([
        { id: 1, name: 'Sample Product A', price: 9.99, vendor: 'Vendor X' },
        { id: 2, name: 'Sample Product B', price: 19.99, vendor: 'Vendor Y' }
      ])

      setLoading(false)
    }

    check()
  }, [])

  if (loading) return <div className="panel">Loading...</div>

  return (
    <div className="panel">
      <h2>Database status</h2>
      <pre className="status">{JSON.stringify(dbStatus, null, 2)}</pre>

      <h2>Products (demo)</h2>
      <ul className="products">
        {products.map(p => (
          <li key={p.id} className="product">
            <div className="product-name">{p.name}</div>
            <div className="product-meta">{p.vendor} • ${p.price.toFixed(2)}</div>
          </li>
        ))}
      </ul>

      <p className="note">Note: product endpoints are not implemented yet — this view uses mock data for now.</p>
    </div>
  )
}
