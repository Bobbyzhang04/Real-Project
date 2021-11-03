pyinstaller --onefile main.py
makeappx pack /m .\appxmanifest64.xml /f .\MyMapping.txt /p xcleaner_x64.msix
makeappx pack /m .\appxmanifest86.xml /f .\MyMapping.txt /p xcleaner_x86.msix