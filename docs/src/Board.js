import React, { Component } from 'react';
import './Board.css';

function Square(props) {
    return (
      <button className={props.squareClass} onClick={props.onClick}>
        {props.value}
      </button>
    );
}
  
class Board extends Component {
    renderSquare(i) {
        var squareVal = ""
        var squareClass = 'square square-open'
        if (this.props.squares[i]===-1) {
            squareVal = "X"
            squareClass = 'square'
        } else if (this.props.squares[i]===1) {
            squareVal = "O"
            squareClass = 'square'
        }
      return (
        <Square
          value={squareVal}
          onClick={() => this.props.onClick(i)}
          squareClass={squareClass}
        />
      );
    }
  
    render() {
      return (
        <div className="board">
          <div className="board-row">
            {this.renderSquare(0)}
            {this.renderSquare(1)}
            {this.renderSquare(2)}
          </div>
          <div className="board-row">
            {this.renderSquare(3)}
            {this.renderSquare(4)}
            {this.renderSquare(5)}
          </div>
          <div className="board-row">
            {this.renderSquare(6)}
            {this.renderSquare(7)}
            {this.renderSquare(8)}
          </div>
        </div>
      );
    }
}

export default Board