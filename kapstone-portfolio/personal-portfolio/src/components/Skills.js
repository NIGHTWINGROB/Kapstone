import Carousel from 'react-multi-carousel';
import 'react-multi-carousel/lib/styles.css';

export const Skills = () => {
  const responsive = {
    superLargeDesktop: {
      breakpoint: { max: 4000, min: 3000 },
      items: 5
    },
    desktop: {
      breakpoint: { max: 3000, min: 1024 },
      items: 3
    },
    tablet: {
      breakpoint: { max: 1024, min: 464 },
      items: 2
    },
    mobile: {
      breakpoint: { max: 464, min: 0 },
      items: 1
    }
  };

  return (
    <section className="skill" id="skills">
        <div className="container">
            <div className="row">
                <div className="col-12">
                    <div className="skill-bx wow zoomIn">
                        <h2>Skills</h2>
                        <p>Languages and frameworks I'm Comfortable with</p>
                        <Carousel responsive={responsive} infinite={true} className="owl-carousel owl-theme skill-slider">
                            <div className="item">
                                <img src='./assets/img/python.jpg' alt='python' />
                                <h5>Python</h5>
                            </div>
                            <div className="item">
                            <img src='./assets.img/javaascript.png' alt='javascript' />
                                <h5>Javascript</h5>
                            </div>
                            <div className="item">
                            <img src='./assets/img/html5.png' alt='HTML5' />
                                <h5>Html5</h5>
                            </div>
                            <div className="item">
                            <img src='./assets/img/react.png' alt='react' />
                                <h5>React</h5>
                            </div>
                        </Carousel>
                    </div>
                </div>
            </div>
        </div>
    </section>
  )
}
