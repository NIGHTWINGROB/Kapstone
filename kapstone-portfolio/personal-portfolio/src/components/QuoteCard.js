import { Col } from "react-bootstrap";

export const QuoteCard = ({ author, quote, imgUrl }) => {
  return (
    <Col size={12} sm={6} md={4}>
      <div className="quote-imgbx">
        <img src={imgUrl} alt='quote'/>
        <div className="quote-txtx">
          <h4>{author}</h4>
          <span>{quote}</span>
        </div>
      </div>
    </Col>
  )
}
