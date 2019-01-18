import React, {
    Component
} from 'react';
import {
    openPositions
} from './Winner'
import * as tf from '@tensorflow/tfjs';

// async function getModel() {
//     const model = await tf.loadModel(process.env.PUBLIC_URL + '/models/supermodel/model.json');
//     return model
// }


export async function Play(board, player) {
    let model = await tf.loadModel(process.env.PUBLIC_URL + '/models/supermodel/model.json')
    console.log("model loaded!")
    //const prediction = model.predict(board);
    //console.log("predictions: " + prediction)
    let openPos = openPositions(board)
    let nextBoardsArray = []

    for (var i = 0; i < nextBoardsArray.length; i++) {
        var currentBoard = returnMove(board, player, openPos[i])
        console.log("currentBoard is: " + currentBoard)

        const x = tf.tensor1d(currentBoard);
        x.reshape([9, 1]).print();
    }
    let nextBoards = tf.variable(tf.zeros([openPos.length, 9, 1]))


    var returnSpace = openPos[Math.floor(Math.random() * openPos.length)];
    return returnSpace

}

/*
const a = tf.tensor([1.0, 2.0, 3.0, 10.0, 20.0, 30.0], shape);

open = game.open_positions()
next_positions = np.zeros((9, 9), dtype=np.int) // Initialize the array

for i in range(0,len(open)):
    next_positions[i] = game.return_move(piece, open[i]) // Add a possible next position
    
next_positions = next_positions[~np.all(next_positions == 0, axis=1)] // Remove all empty next positions
next_positions = np.expand_dims(next_positions, axis=2) // Give it a spacial dimension
predictions = model.predict(next_positions) // Generate predictions for each possible position
move_to_return = open[0] // default move
move_prob = -1000 // Initialize the prob of winning to 0
if piece == 'o':
    for index, prediction in enumerate(predictions):
        if prediction[2] - 1.1 * prediction[0] > move_prob:
            move_to_return = open[index] // Index is the prediction index, which corresponds to move in next_positions
            move_prob = prediction[2] - prediction[0]
elif piece == 'x':
    for index, prediction in enumerate(predictions):
        if prediction[0] - 1.1 * prediction[2] > move_prob:
            move_to_return = open[index] // Index is the prediction index, which corresponds to move in next_positions
            move_prob = prediction[0] - prediction[2]
return move_to_return
*/

function returnMove(board, player, pos) { // player is 'X' or 'O'. Pos is an integer from 0 to 8
    if (board[pos] === 0) {
        board[pos] = player
    } else {
        return "Error! Space not open!"
    }
}