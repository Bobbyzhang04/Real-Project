Remove-Item msixpackage -Recurse
Remove-Item msixbundle -Recurse
makeappx pack /o /m appxmanifest64.xml /f mapping_x64.txt /p msixpackage/xcleaner_x64.msix
makeappx pack /o /m appxmanifest86.xml /f mapping_x86.txt /p msixpackage/xcleaner_x86.msix
makeappx bundle /o /d msixpackage /p msixbundle/xcleaner.msixbundle
