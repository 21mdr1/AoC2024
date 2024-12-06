# /bin/bash

cd ~/OneDrive/Documents/Projects/AoC2024

DAY=$1

mkdir day${DAY}

touch input/input${DAY}.txt input/test/test-input${DAY}.txt

cp helpers/templates/script.txt day${DAY}/part1.py
cp helpers/templates/script.txt day${DAY}/part2.py
cp helpers/templates/utils.txt day${DAY}/utils.py

git add .
git commit -m "Create files for day ${DAY}"