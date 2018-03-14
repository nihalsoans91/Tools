#!/bin/bash
comma=','
csv=""
cat practice_filereading.txt | while read line
do
  l=0
   if [ "$line" = "min_BatchIRL_InputLen:" ]
   then
     read line
     csv=$line$comma
   fi
   if [ "$line" = "LBA" ]
   then
     read line
     csv=$csv$line$comma
   fi
   if [ "$line" = "ILE" ]
   then
      read line
      arr=( $line )
      a1=${arr[0]}
      a2=${arr[1]}
      csv=$csv$a1$comma$a2
      l=1
   fi
   if [ $l -eq 1 ]
   then
     echo $csv >> output.csv
     l=0
     csv=""
   fi

done
