@echo off
REM Trên Window khi truy cập SSH đến server nào thì window sẽ nhớ host đó lại
REM SSH nhớ host đó tại file C:\Users\yourname\.ssh\known_hosts
REM Tìm chuỗi trong file và xóa line nào có chứa chuỗi đó.
setlocal enabledelayedexpansion

set "file=known_hosts"
set "tempfile=temp.txt"
set "search=127.0.0.1"
echo Looking to string "%search%" ...
if not exist "%file%" (
    echo File "%file%" not found.
    exit /b
)

set "newline="
(for /f "delims=" %%a in (%file%) do (
    set "line=%%a"
    echo !line! | findstr /C:"%search%" >nul || echo %%a
)) > %tempfile%

move /y %tempfile% %file% >nul

echo Lines containing "%search%" have been deleted from %file%.

pause