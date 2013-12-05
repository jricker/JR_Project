"c:\virtualdub\VDub64.exe" /i "c:\goPro_v02.vcf" "%~1" "%~1.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
pause