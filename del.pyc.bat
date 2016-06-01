@echo off
REM Delete .pyc on Windows.
for /r %%b in (*.*) do (
	if /i %%~xb EQU .pyc del %%b
)
pause