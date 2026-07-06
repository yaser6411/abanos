import React, { useEffect, useState } from 'react'

export default function ProductList() {
  const [dbStatus, setDbStatus] = useState(null)
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    async function fetchData() {
      setLoading(true)
      try {
        const res = await fetch('/db-check')
        const data = await res.json()
        setDbStatus(data)
      } catch (err) {
        setDbStatus({ database: 'failed', error: err.message })
      }

      try {
        const r = await fetch('/api/products')
        if (r.ok) {
          const prods = await r.json()
          setProducts(prods)
        } else {
          // keep demo products if API not ready
        }
      } catch (err) {
        // ignore
      }

      setLoading(false)
    }

    fetchData()
  }, [])

  if (loading) return <div className="panel">Loading...</div>

  return (
    <div className="panel">
      <h2>Database status</h2>
      <pre className="status">{JSON.stringify(dbStatus, null, 2)}</pre>

      <h2>Products</h2>
      {products.length === 0 ? (
        <p>No products found. You can add a product with the API.</p>
      ) : (
        <ul className="products">
          {products.map(p => (
            <li key={p.id} className="product">
              <div className="product-name">{p.name}</div>
              <div className="product-meta">{p.vendor ? p.vendor.name : 'Unknown'} • ${p.price.toFixed(2)}</div>
            </li>
          ))}
        </ul>
      )}

      <p className="note">Note: use the backend API to add vendors and products.</p>
    </div>
  )
}
