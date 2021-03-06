::Master BAT
if %~1 == PRORES goto PRORES
if %~1 == IMG2MOV goto IMG2MOV
if %~1 == EXR2IMG goto EXR2IMG
if %~1 == EXR2IMG2MOV goto EXR2IMG2MOV
if %~1 == MOV2CUTDOWN goto MOV2CUTDOWN
if %~1 == EDL2MOV goto EDL2MOV
if %~1 == OPENFOLDER goto OPENFOLDER
::
:PRORES
"%~2" -i %3 -y -vcodec prores -profile:v %~5 -s hd1080 -bits_per_mb 8000 "%~4"
goto END
::
:IMG2MOV
::
"%~4" /i "%~3" %2 %6.avi /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
%5 -i %6.avi -y -vcodec prores -profile:v 0 -s hd1080 -bits_per_mb 8000 %6.mov
del %6.avi
::touch -m "%~6.mov"
::%7 %6.mov
goto END
::
:EXR2IMG
::%8 "%~6-10000.exr" "%6_temp.jpg" -resize 1280 720
%2 %3 %4 -resize 1920 1080
goto END
::
:EXR2IMG2MOV
%8 %9 %2 -resize 1280 720
goto IMG2MOV
::
:MOV2CUTDOWN
"%~2" -i "%~3" -y -ss %~5 -to %~6 -y -vcodec prores -profile:v 0 -s hd1080 "%~4"
goto END
::
:EDL2MOV
"%~2" -oac pcm -ovc copy -o %~3
goto END
::
:OPENFOLDER
%SystemRoot%\explorer.exe %2
goto END
::
:END
echo DONE