import React, { Component } from 'react';

export function Play (board, player) {
    let openPos = openPositions(board)
    var returnSpace = openPos[Math.floor(Math.random()*openPos.length)];
    return returnSpace
}

function openPositions(board) {
    let openPos = []
    for (var i = 0; i < 9; i++) {
        if (board[i] === 0) {
            openPos.push(i)
        }
    }
    return openPos 
}