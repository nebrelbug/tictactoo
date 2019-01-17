import React, { Component } from 'react';
import {openPositions} from './Winner'
import * as tf from '@tensorflow/tfjs';

export function Play (board, player) {
    let openPos = openPositions(board)
    var returnSpace = openPos[Math.floor(Math.random()*openPos.length)];
    return returnSpace
}