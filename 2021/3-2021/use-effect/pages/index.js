import Head from 'next/head'
import styles from '../styles/Home.module.css'
import React, { useState, useEffect } from 'react'

export default function Home() {
  const [count, setCount] = useState(0)

  const handleScroll = () => {
    setCount(count + scrollY)
  }

  useEffect(() => {
    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    }
  })

  return (
    <div className={styles.container}>
      <p>You have moved {count} spots</p>
      <button onClick={() => setCount(count + 1)}>
        Move 1 spot
      </button>
    </div>
  )
}