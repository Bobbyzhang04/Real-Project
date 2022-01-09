Remove-Item spec/x86 -Recurse
Remove-Item dist/x86 -Recurse
Remove-Item build/x86 -Recurse
pyinstaller --specpath spec/x86 --distpath dist/x86 --workpath build/x86 --onefile main.py