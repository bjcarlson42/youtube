// getStaticPaths()

const TodoItem = ({ todo }) => {

    return (
        <div>
            <h1>getStaticPaths()</h1>
            <p>userId: {todo.userId}</p>
            <p>id: {todo.id}</p>
            <p>title: {todo.title}</p>
            <p>completed: {todo.completed.toString()}</p>
        </div>
    )
}

export async function getStaticProps(context) {
    const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${context.params.id}`)
    const todo = await res.json()
    return {
        props: {
            todo,
        },
    }
}

export async function getStaticPaths() {
    return {
        paths: new Array(200).fill(null).map((_, index) => (
            { params: { id: `${index + 1}` } }
        )),
        fallback: true,
    }
}

// export async function getStaticPaths() {
//     return {
//         paths: [
//             { params: { id: '1' } },
//             { params: { id: '2' } },
//             { params: { id: '3' } },
//         ],
//         fallback: false,
//     }
// }

export default TodoItem