echo off
::Master BAT
if %~1 == PRORES goto PRORES
if %~1 == IMG2MOV goto IMG2MOV
if %~1 == EXR2IMG goto EXR2IMG
if %~1 == EXR2IMG2MOV goto EXR2IMG2MOV
if %~1 == MOV2CUTDOWN goto MOV2CUTDOWN
if %~1 == EDL2MOV goto EDL2MOV
::
:PRORES
"%~1" -i "%~2" -y -vcodec prores -profile:v %~4 -s hd1080 -bits_per_mb 8000 "%~3"
::
:IMG2MOV
"C:\Program Files (x86)\djv 0.8.3\bin\djv_convert" "scGP01_sh030_EXR_0001-0010.exr" "C:\EXR\test_01.jpg" -resize 1280 720
::
::
::
"%~3" /i "%~2" "%~1" "%~5.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
"%~4" -i "%~5.avi" -y -vcodec prores -profile:v 0 -s hd1080 -bits_per_mb 8000 "%~5_preview.mov"
del "%~5.avi"
"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" "%~5_preview.mov"
::
::
::
:EXR2IMG
"C:\Program Files (x86)\djv 0.8.3\bin\djv_convert" "scGP01_sh030_EXR_0001-0010.exr" "C:\EXR\test_01.jpg" -resize 1280 720
goto IMG2MOV
:EXR2IMG2MOV
"C:\Program Files (x86)\djv 0.8.3\bin\djv_convert" "scGP01_sh030_EXR_0001-0010.exr" "C:\EXR\test_01.jpg" -resize 1280 720
:MOV2CUTDOWN
"%~1" -i "%~2" -y -ss %~4 -to %~5 -y -vcodec prores -profile:v 0 -s hd1080 "%~3"
:EDL2MOV
"%~1" -oac pcm -ovc copy -o %~2
:END
echo DONE