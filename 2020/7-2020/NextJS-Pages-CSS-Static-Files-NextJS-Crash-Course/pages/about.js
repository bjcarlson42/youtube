import Button from '../components/Button'

export default function About() {
    return (
        <div>
            <h1 className="about-title">About Page</h1>
            <Button />
            <p style={{fontSize: '40px', color: 'red'}}>I am a paragraph.</p>
            <p className="jsx-class">hello</p>
            <img className="img" src="/1.jpg"></img>

            <style jsx>{`
        .jsx-class {
            color: blue;
        }

        .img {
            width: 300px;
            height: auto;
        }
      `}</style>
        </div>
    )
}