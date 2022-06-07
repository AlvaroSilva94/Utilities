::---------------------------------------------------------------------------------------
:: Purpose: Simple utility script to download file from remote folder. It created a local
::          folder with user inputed name and places the remote file copy inside that 
::          folder.
::
:: Modification History
:: CR        Date       Name        Comment  
:: -------  ----------  --------  ------------------------------------------------------
:: 0000	   22/01/2020  amsilva   Initial version
::--------------------------------------------------------------------------------------

@echo off

Title Get new EA master replica

set /p Folder=Please enter the EA copy folder name that you desire: 
echo.

::Setting the names to rename the file
set "NewName=FlexityInnsbruck_Alvaro02.eap"
set "OldName=FlexityInnsbruck_Master02.eap"
 
set "Here=%CD%"
set Naptime= 3000
set "NewFldr=%Here%\%Folder%"
set Source_Path="\\PATH_TO_FILE\FlexityInnsbruck_Master02.eap"

::Create folder to copy file into from remote
mkdir %NewFldr%

echo Folder created
echo.

echo Copying EA Master file
echo. 

::Here goes the copy part ------------------

for /f %%a in ('copy %Source_Path% %NewFldr%') do set "CR=%%a"

FOR /L %%n in (1,1,10) DO (
    call :show_progress %%n 10
    ping localhost -n 2 > nul
)

echo Done!
exit /b

:show_progress
setlocal EnableDelayedExpansion
set current_step=%1
set total_steps=%2
set /a "progress=(current_step * 100) / total_steps"

set /p ".=Progress: !progress!%%!CR!" <nul

if !progress! equ 100 echo.

::exit /b

::Here ends the copy part ------------------


echo Files copied succesfully

::timeout
timeout %Naptime%

echo renaming file
echo.

::rename of the file
rename %Folder%\%Oldname% %NewName%

echo Done
