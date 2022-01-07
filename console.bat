@echo off
echo Console; start/run build
:input
    set /p cmd=">>: "
goto :exec_%cmd%
:exec_start
    start py app.py
    exit
:exec_run
    start py app.py
    exit
:exec_build
    echo Not yet supported
    goto input