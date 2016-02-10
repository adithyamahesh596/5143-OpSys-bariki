#!/bin/bash

p=$1

q="${p##*/}"

fe="${p##*.}"

r=$(date +"%m-%d-%y")

n="${q%.*}_$r.$fe"

touch $n

echo $n "created"
