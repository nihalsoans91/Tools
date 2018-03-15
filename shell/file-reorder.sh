#!/bin/bash
curdir=${PWD##*/}
i=1; temp=$(mktemp -p .); for file in image*
do
mv "$file" $temp;
mv $temp $(printf "img_%s_%0.3d.jpg" $curdir $i)
i=$((i + 1))
done
rm file-reorder.sh
