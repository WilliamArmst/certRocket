echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v241\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\tell.exe" CT156-36-2022 56644 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v241\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 31212) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 39100) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 48244) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 51212) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 43488) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 42720) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 50752) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 32472) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 15208) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 30132) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 46984) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 54280) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 40416) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 54196) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 21580) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 55020) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 30932) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 3992) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 37288) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 46024) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 39212) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 28104) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 51664) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 43868) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 54248) 
if /i "%LOCALHOST%"=="CT156-36-2022" (%KILL_CMD% 36292)
del "C:\Scratch\WA\certRocket\CFD\cleanup-fluent-CT156-36-2022-54248.bat"
