@echo off
setlocal enabledelayedexpansion
for /f "delims=" %%b in ('git rev-parse --abbrev-ref HEAD') do set current_branch=%%b

set "pattern=!current_branch:er-=!"

if "!pattern!"=="!current_branch!" (
    echo Error: Current branch name does not match er-xxxx format
    exit /b 1
)

echo Extracted keyword from branch name: !pattern!

:: Target branch (modify as needed)
set target_branch=lijiang/hly-deploy

git fetch lijiang

:: Get all commit hashes in target branch containing the keyword (in chronological order)
set "commits="
for /f "delims=" %%c in ('git log --pretty=format:"%%H" --grep="!pattern!" !target_branch! --reverse') do (
    set "commits=!commits! %%c"
)

:: Check if any related commits found
if "!commits!"=="" (
    echo No commits containing !pattern! found in target branch !target_branch!
    exit /b 0
)

echo The following related commits will be cherry-picked:
for %%c in (!commits!) do (
    git log -1 --pretty=format:"%%h - %%s" %%c
)

:: Batch cherry-pick
for %%c in (!commits!) do (
    echo Cherry-picking commit: %%c
    git cherry-pick %%c
    if !errorlevel! neq 0 (
        echo Cherry-pick %%c failed, please resolve conflicts and run git cherry-pick --continue
        exit /b 1
    )
)

echo All related commits have been successfully cherry-picked to the current branch
endlocal