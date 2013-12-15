"%~1" -nosound -fps 30 -ovc copy -o %~2
::"%~1" -f concat -r 30 -i "%~2" -y -r 30 -c copy "%~3"
::"%~1" -i "concat:C:\MOV\EDIT\1_FINALV2.mov|C:\MOV\EDIT\2_FINALV2.mov|C:\MOV\EDIT\3_FINALV2.mov" -y -codec copy "%~2"