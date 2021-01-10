// getInitialProps()

function Github({ name, projects }) {
    return (
        <div>
            <h1>getInitialProps</h1>

            <p>{name}</p>
            <p>{projects[0].id} </p>
        </div>
    )
}

Github.getInitialProps = async () => {
    const res = await fetch('https://api.github.com/users/bjcarlson42/repos')
    const json = await res.json()
    const projects = json
    return {
        name: 'Ben',    
        projects: projects
    }
}

export default Github