"%~3" /i "%~2" "%~1" "%~5.avi" /x
if %errorlevel% == 0  goto ok
:err
echo Error %errorlevel% with %~nx1
goto theend
:ok
echo Ok, done
:theend
"%~4" -i "%~5.avi" -y -vcodec prores -profile:v 0 -s hd1080 -bits_per_mb 8000 "%~5_preview.mov"
::del "%~5.avi"
"%~4" -i "%~5_preview.mov" -y -ss %~6 -to %~7 -y -vcodec prores -profile:v 0 -s hd1080 "%~5_cut.mov"
::"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe" "%~5_preview.mov"