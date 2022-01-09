Remove-Item spec/x64 -Recurse
Remove-Item dist/x64 -Recurse
Remove-Item build/x64 -Recurse
pyinstaller --specpath spec/x64 --distpath dist/x64 --workpath build/x64 --onefile main.py