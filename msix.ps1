makeappx pack /o /m appxmanifest64.xml /f mapping_x64.txt /p msix/xcleaner_x64.msix
makeappx pack /o /m appxmanifest86.xml /f mapping_x86.txt /p msix/xcleaner_x86.msix
makeappx bundle /o /d msix /p xcleaner.msixbundle
