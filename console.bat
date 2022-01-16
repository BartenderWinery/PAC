@echo off
echo Console; [start/run, build, clean, open, cls, reboot, exit/close]
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
    echo:
    echo [py, github]
    set /p con=":: " 
    call :subexec_%con%
    :subexec_py
        call RMDIR /s /q %~dp0\__pycache__ && call RMDIR /s /q %~dp0\mods\__pycache__ && call RMDIR /s /q %~dp0\memory\__pycache__
        echo Python cleanup complete.
        goto input
    :subexec_github
        call del README.md && call del /q .gitignore && call del /q .gitattributes && call RMDIR /s /q .git
        echo Github cleanup complete.
        goto input
:exec_open
    call %~dp0\app.py
    echo Opened
    goto input
:exec_cls
    call cls
    echo:
    goto input
:exec_reboot:
    call %~dp0\console.bat
:exec_exit
    exit
:exec_close
    exit