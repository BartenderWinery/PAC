@echo off
echo Console; start/run build clean
:input
    set /p cmd=">>: "
goto :exec_%cmd%
:exec_start
    start py %~dp0\app.py
    exit
:exec_run
    start py %~dp0\app.py
    exit
:exec_build
    echo Not yet supported; Probably going to be useless before its finished.
    goto input
:exec_clean
    echo What would you like to cleanup?
    echo [py, github]
    set /p con=":: " 
    2>NUL call :subexec_%con%
    if ERRORLEVEL 1 call :subexec_default
    :subexec_py
        call RMDIR /s /q %~dp0\__pycache__ && call RMDIR /s /q %~dp0\mods\__pycache__ && call RMDIR /s /q %~dp0\memory\__pycache__
        echo Python cleanup complete.
        goto input
    :subexec_github
        call del README.md && call del /q .gitignore && call del /q .gitattributes && call RMDIR /s /q .git
        echo Github cleanup complete.
        goto input
    :subexec_default
        echo Nul: Nothing found.
        goto input