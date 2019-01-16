import React, { Component } from 'react';
import Board from './Board'
import './App.css';
import calculateWinner, {isEven} from './Winner'

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {
      board: [0,0,1,0,0,0,0,0,0],
      playing: false, // -1 if player is x, 1 if player is o
      turn: 0,
      winner: false
    };
  }

  renderButtons() {
    if (this.state.playing === false) {
      return (
        <div className="buttons">
          <button className="button">Play as X</button>
          <button className="button">Play as O</button>
        </div>
      )
    }
  }

  handleBoardClick(i) {
    if (!this.state.playing || this.state.winner || this.state.board[i] !== 0) { // If game over, game won, or square empty, do nothing
      return
    } else {
      var board = this.state.board
      board[i] = this.state.userPiece
      this.setState({
        board: board,
        turn: this.state.turn + 1,
        winner: calculateWinner(this.state.board)
      });
    }
  }

  returnStatus() {
    let stat
    let winner = this.state.winner
    if (winner) {
      stat = "Winner: " + winner
      this.setState({winner: winner})
    } else {
      if (this.state.playing === -1) {
        if (isEven(this.state.turn)) {
          stat = "Your turn, X!"
        } else {
          stat = "AI thinking..."
        }
      } else if (this.state.playing === -1) {
        if (!isEven(this.state.turn)) {
          stat = "Your turn, O!"
        } else {
          stat = "AI thinking..."
        }
      } 
    }
    return stat
  }

  render() {

    return (
      <div className="game">
        <Board
            squares={this.state.board}
            onClick={i => this.handleBoardClick(i)}
        />
        <div className="game-info">
          <div className="status">{this.returnStatus()}</div>
          {this.renderButtons()}
        </div>
      </div>
    );
  }
}

export default Game