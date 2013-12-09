"%~3" /i "%~2" "%~1" "%~5.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
"%~4" -i "%~5.avi" -codec:v libx264 -profile:v high -preset slow -b:v 500k -maxrate 500k -bufsize 1000k -b:a 128k "%~5_ProRes.mov"
del "%~5.avi"