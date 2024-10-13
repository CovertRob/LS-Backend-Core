#!/bin/bash

function server() {
    while true
    do
      message_ar=()
      check=true
      while $check
      do
        read line
        message_ar+=($line)
        if [[ "${#line}" -eq 1 ]]
        then
          check=false
        fi
      done
      method=${message_ar[0]}
      path=${message_ar[1]}
      if [[ $method = 'GET' ]]
      then 
        if [[ -f "./www/$path" ]]
        then  
          echo -ne "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nContent-Length: $(wc -c <'./www/'$path)\r\n\r\n"; cat "./www/$path"
        else
          echo -ne 'HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n'
        fi
      else
        echo -ne 'HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n'
      fi
    done
}

coproc SERVER_PROCESSS { server; }

netcat -lv 2345 <&${SERVER_PROCESSS[0]} >&${SERVER_PROCESSS[1]}