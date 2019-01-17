import React, { Component } from 'react';
import calculateWinner, {isEven} from './Winner'

export function Buttons(props) {
    if (props.playing === false) {
      return (
        <div className="buttons">
          <button className="button" style={{marginRight:'2.5%'}} onClick={() => props.onClick(-1)}>Play as X</button>
          <button className="button" style={{marginLeft:'2.5%'}} onClick={() => props.onClick(1)}>Play as O</button>
        </div>
        )
    } else {
        return null
    }
}

export function Status(props) {
    console.log("props: " + JSON.stringify(props))
    let stat
    let winner = props.winner
    if (winner === -1) {
        stat = "X won!"
    } else if (winner === 1) {
        stat = "O won!"
    } else if (winner === 0) {
        stat = "It's a draw!"
    } else if (winner === 'none') {
        if (props.playing === -1) { // If user is X
            if (isEven(props.turn)) {
                stat = "Your turn, X!" 
            } else {
                stat = "AI thinking..."
            }
        } else if (props.playing === 1) { // If user is O
            if (!isEven(props.turn)) {
                stat = "Your turn, O!"
            } else {
                stat = "AI thinking..."
            }
        } 
    }
    return <div className="status">{stat}</div>
}