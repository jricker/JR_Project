@echo off
if %~1 == Run goto Run
if %~1 == Go goto GO
:Run
echo Run!
goto END
:GO
echo GO!
goto END
:END
echo FINISHED