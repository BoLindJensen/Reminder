START /WAIT "Lets Scons" /Dc:\godot /B cmd /c scons platform=android target=release -j8
START /WAIT "Lets gradle" /Dc:\godot\platform\android\java /B cmd /c gradlew build
START /WAIT "Lets gradle" /Dc:\godot\ /B cmd /c echo "--- WE are Le'Done ---"

pause
@echo on
exit /b
