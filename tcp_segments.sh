#!/bin/bash
# save tcp segments received and transmitted every 5 seconds

#if the file does not exist, start file
FILE=/home/ssuee/5hw_11_11/tcp_segments.txt
if test ! -f "$FILE"; then
    
    printf '1,' >> tcp_segments.txt #append a comma

    # append received
    netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $1}' >> tcp_segments.txt 

    printf ',' >> tcp_segments.txt #append a comma

    # append sent out
    netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $2}' >> tcp_segments.txt 


    printf '\n' >> tcp_segments.txt #append a newline
fi

#get last iteration #
expr $(tail tcp_segments.txt -n1 | awk 'BEGIN{ FS = "," }{printf $1}') + 1 >> tcp_segments.txt

#remove last newline (last byte)
truncate -s -1 tcp_segments.txt 


printf ',' >> tcp_segments.txt #append a comma

# append received
netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $1}' >> tcp_segments.txt 

printf ',' >> tcp_segments.txt #append a comma

# append sent out
netstat --statistics -t | grep Tcp -A 10 | grep segment | cut -d" " -f5 | awk 'BEGIN{ RS = "" ; FS = "\n" }{printf $2}' >> tcp_segments.txt 


printf '\n' >> tcp_segments.txt #append a newline
