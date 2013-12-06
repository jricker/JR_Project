"%~3" /i "%~2" "%~1" "%~5.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
"%~4" -i "%~5.avi" -c:v libx264 -preset slow -s hd1080 -crf 20 -c:a libvo_aacenc -b:a 128k "%~5_H264.mp4"
del "%~5.avi"
"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" "%~5_H264.mp4"