import React, { Component } from 'react';
import Board from './Board'
import './App.css';
import calculateWinner, {isEven} from './Winner'
import {Status, Buttons} from './Messages'
import * as AI from './AI'

class Game extends Component {
  constructor(props) {
    super(props);
    this.state = {
      board: [0,0,0,0,0,0,0,0,0],
      playing: false, // -1 if player is x, 1 if player is o
      turn: 0,
      winner: 'none'
    };
  }

  startGame(player) {
    this.setState({
      board: [0,0,0,0,0,0,0,0,0],
      turn: 0,
      winner: 'none',
      playing: player
    }, () => {
      console.log("You are player " + player)
      if (player === 1) {
        this.aiMove(AI.Play(this.state.board, -1))
      }
    })
  }

  move(pos, player) {
    console.log("Player %s moves at %s", player, pos)
    var board = this.state.board
    board[pos] = player
    console.log("board: " + board)
    let currentWinner = calculateWinner(board)
    this.setState({
      board: board,
      turn: this.state.turn + 1,
      winner: currentWinner,
      playing: (currentWinner === 'none' ? this.state.playing : false)
    }, () => {
      if (player === this.state.playing) {
        this.aiMove(AI.Play(this.state.board, this.state.playing * -1))
      }
    })
  }

  aiMove(pos) {
    this.move(pos, this.state.playing * -1)
  }


  handleBoardClick(i) {
    if (!this.state.playing || this.state.winner !== 'none' || this.state.board[i] !== 0) { // If game over, game won, or square empty, do nothing
      return
    } else {
      if (this.state.playing === -1) { // If user is X
        if (isEven(this.state.turn)) {
          this.move(i, this.state.playing)
        } else {
          return
        }
      } else if (this.state.playing === 1) { // If user is O
        if (isEven(this.state.turn)) {
          console.log("state is even")
          return
        } else {
          this.move(i, this.state.playing)
        }
      }

    }
  }

  render() {

    return (
      <div className="game">
        <Board
            squares={this.state.board}
            onClick={i => this.handleBoardClick(i)}
        />
        <div className="game-info">
          <Status winner={this.state.winner} playing={this.state.playing} turn={this.state.turn}/>
          <Buttons playing={this.state.playing} onClick={player => this.startGame(player)}/>
        </div>
      </div>
    );
  }
}

export default Game