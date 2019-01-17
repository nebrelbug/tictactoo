import React, { Component } from 'react';
import {openPositions} from './Winner'

export function Play (board, player) {
    let openPos = openPositions(board)
    var returnSpace = openPos[Math.floor(Math.random()*openPos.length)];
    return returnSpace
}