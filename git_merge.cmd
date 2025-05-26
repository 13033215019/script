@echo off
setlocal enabledelayedexpansion
set "sprint_name=250620"

set "ENABLE_BRANCHS="
:loop
if "%1"=="" goto :continue
set "ENABLE_BRANCHS=%ENABLE_BRANCHS% %1"
shift
goto :loop
:continue

echo apply:****** ENABLE_BRANCHS=%ENABLE_BRANCHS%
echo apply:****** sprint_name=%sprint_name%

echo apply:****** git fetch lijiang
git fetch lijiang

if "%ENABLE_BRANCHS%"=="" (
    for /f "tokens=*" %%i in ('git branch -r ^| findstr "lijiang" ^| findstr "%sprint_name%" ^| findstr /r /c:"lijiang/.*"') do (
        set "branch=%%i"
        set "branch=!branch:lijiang/=!"
        
        echo apply:****** Merging branch: !branch!
        echo apply:****** git merge "lijiang/!branch!" --no-edit
        git merge "lijiang/!branch!" --no-edit
        if errorlevel 1 (
            echo apply:****** Error merging branch !branch! ************************ 
            exit /b 1
        ) else (
            echo apply:****** Successfully merged branch: !branch! ************************
        )
    )
) else (
    for %%p in (%ENABLE_BRANCHS%) do (
        for /f "tokens=*" %%i in ('git branch -r ^| findstr "lijiang" ^| findstr "%%p" ^| findstr "%sprint_name%" ^| findstr /r /c:"lijiang/.*"') do (
            set "branch=%%i"
            set "branch=!branch:lijiang/=!"
            
            echo apply:****** Merging branch: !branch!
            echo apply:****** git merge "lijiang/!branch!" --no-edit
            git merge "lijiang/!branch!" --no-edit
            if errorlevel 1 (
                echo apply:****** Error merging branch !branch! ************************
                exit /b 1
            ) else (
                echo apply:****** Successfully merged branch: !branch! ************************
            )
        )
    )
)

echo apply:****** All branches merged successfully

endlocal