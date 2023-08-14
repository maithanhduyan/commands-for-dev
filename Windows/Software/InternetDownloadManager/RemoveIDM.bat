@echo off
reg delete "HKEY_USERS\S-1-5-21-285869090-2900473179-1325365908-1001\Software\Classes\WOW6432Node\CLSID\{07999AC3-058B-40BF-984F-69EB1E554CA7}" /f
echo Key deleted successfully.
pause