@echo off
echo Console; [embed, start/run, build, clean, open, cls, reboot, exit/close]
:input
    set /p cmd=">>: "
    goto :exec_%cmd%
:exec_embed
    echo ==--------------------------==Embedded script==-----------------------==
    call py %~dp0\app.py
    echo ==--==End script==----------------------------------------------------==
    goto input
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
    echo [py, github, vs]
    set /p con=":: " 
    call :subexec_%con%
    :subexec_py
        call RMDIR /s /q %~dp0\__pycache__ && call RMDIR /s /q %~dp0\mods\__pycache__ && call RMDIR /s /q %~dp0\memory\__pycache__
        echo Python cleanup complete.
        goto input
    :subexec_github
        call del %~dp0\README.md && call del /q %~dp0\.gitignore && call del /q %~dp0\.gitattributes && call RMDIR /s /q %~dp0\.git
        echo Github cleanup complete.
        goto input
    :subexec_vs
        call RMDIR /s /q %~dp0\.vs
        echo VS cleanup complete.
        goto input
:exec_open
    echo Visual studio is required for this command to run.
    call code %~dp0
    echo:
    echo Done
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