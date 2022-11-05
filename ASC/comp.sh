#!/bin/bash
echo "Executing file: $1"
as --32 $1.s -o $1
./$1
