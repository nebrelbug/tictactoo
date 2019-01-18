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
    console.log("AI is playing: " + player)
    let model = await tf.loadModel(process.env.PUBLIC_URL + '/models/supermodel/model.json')
    console.log("model loaded!")

    let openPos = openPositions(board)
    let nextBoardsArray = []

    for (var i = 0; i < openPos.length; i++) {
        var currentBoard = returnMove(board, player, openPos[i])
        // console.log("currentBoard is: " + currentBoard)
        nextBoardsArray.push(currentBoard)
    }
    let nextBoards = tf.tensor(nextBoardsArray, [nextBoardsArray.length, 9, 1])
    // nextBoards.print()
    const firstPredictions = model.predict(nextBoards)
    console.log("predictions: " + firstPredictions)

    let returnSpace = openPos[0]
    let moveProb = -1000

    let predictiondata = await firstPredictions.data()
    let predictions = Array.from(predictiondata);
    console.log("predictions: " + predictions)

    if (player === -1) { // If AI is X
        for (var j = 0; j < openPos.length; j++) {
            let prediction = [predictions[j*3], predictions[j*3+1], predictions[j*3+2]]
            // console.log
            console.log("prediction: " + prediction)
            if (prediction[0] - 1.1 * prediction[2] > moveProb) { // If probability of O winning is greater
                returnSpace = openPos[j]
                moveProb = prediction[0] - 1.1* prediction[2]
            }
        }
    } else if (player === 1) { // If AI is O
        for (var j = 0; j < openPos.length; j++) {
            let prediction = [predictions[j*3], predictions[j*3+1], predictions[j*3+2]]
            console.log("prediction: " + prediction)
            if (prediction[2] - 1.1 * prediction[0] > moveProb) { // If probability of O winning is greater
                returnSpace = openPos[j]
                moveProb = prediction[2] - 1.1 * prediction[0]
            }
        }
    }

    return returnSpace
}

/*
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
    let newBoard = board.slice()
    if (newBoard[pos] === 0) {
        newBoard[pos] = player
    } else {
        return "Error! Space not open!"
    }
    return newBoard
}