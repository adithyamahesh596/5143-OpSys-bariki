#!/bin/bash

p=$(date +"%m-%d-%y")

r=$p'_'$1

touch $r

echo $r "created"

