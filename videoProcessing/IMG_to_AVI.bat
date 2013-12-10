"%~3" /i "%~2" "%~1" "%~5.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
"%~4" -i "%~5.avi" -vcodec prores -profile:v 0 -s hd1080 -bits_per_mb 8000 "%~5_ProRes.mov"
del "%~5.avi"