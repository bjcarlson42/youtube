// getStaticProps()
// 
// What it is:
// Static Generation: Fetch data at build time.
//
// When to use:
// - The data required to render the page is available at build time ahead of a user’s request.
// - The data comes from headless CMS.
// - The data can be publicly cached(not user - specific).
// - The page must be pre - rendered(for SEO) and be very fast — getStaticProps generates HTML and JSON files, both of which can be cached by a CDN for performance.

import Head from 'next/head'

const Todo = ({ todos }) => {
    return (
        <div>
            <Head>
                <title>Todo Page</title>
            </Head>

            <style jsx>{`
                .true {
                    text-decoration: line-through;
                }
            `}
            </style>

            <h1>getStaticProps</h1>

            <ol>
                {todos.map(({ id, title, completed }) => (
                    <li key={id} className={completed}>{title}</li>
                ))}
            </ol>

        </div>
    )
}

export async function getStaticProps() {
    const res = await fetch('https://jsonplaceholder.typicode.com/todos')
    const todos = await res.json()
    return {
        props: {
            todos,
        },
    }
}

export default Todo