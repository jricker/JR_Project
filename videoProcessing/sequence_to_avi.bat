"c:\Program Files\virtualDub\VDub64.exe" /i "%~2" "%~1" "%~1.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
pause