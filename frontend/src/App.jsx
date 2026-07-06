import React from 'react'
import ProductList from './components/ProductList'

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>Abanos (Demo)</h1>
        <p>Minimal React frontend for the Abanos FastAPI backend.</p>
      </header>

      <main>
        <ProductList />
      </main>

      <footer className="footer">© Abanos</footer>
    </div>
  )
}
