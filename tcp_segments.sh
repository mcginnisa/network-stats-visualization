#!/bin/bash
# save tcp segments received and transmitted every 5 seconds


i="0"
rm tcp_segments.txt
printf 'iteration,received,sent out\n' >> tcp_segments.txt

while [ $i -lt 10 ]
do

i=$[$i+1]

printf $i #debug

printf $i >> tcp_segments.txt
printf ',' >> tcp_segments.txt

# received
#netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d$'\n' -f1 | cut -d' ' -f5 >> tcp_segments.txt 


netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $1}' >> tcp_segments.txt 


printf ',' >> tcp_segments.txt

#sent out
#netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d$'\n' -f2 | cut -d' ' -f5 >> tcp_segments.txt 

netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $2}' >> tcp_segments.txt 


#printf ',' >> tcp_segments.txt
printf '\n' >> tcp_segments.txt
 
sleep 5



done
