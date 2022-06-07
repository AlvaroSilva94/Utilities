::------------------------------------------------------------------------------------
:: Purpose: Simple utility script to launch barracuda VPN and auto-fill user/pass. 
::          It also simulates "enter" after filling the above mentioned fields.
::
:: Modification History
:: CR        Date       Name        Comment  
:: -------  ----------  --------  -----------------------------------------------------
:: 0000	   15/01/2020  amsilva   Initial version
::-------------------------------------------------------------------------------------

@if (@CodeSection == @Batch) @then


@echo off

set "user=xxx"
set "pass=xxxxx."
set wait=5
set wt=1

::start VPN
start /d "C:\Program Files\Barracuda\Network Access Client" nacvpn.exe
start /d "C:\Program Files\Barracuda\Network Access Client" cudanacsvc.exe

echo files opened
echo.

::wait 5 seconds for the user to click the right text box
timeout %wait%
echo.

::Use the buffer for the keyboard
CScript //nologo //E:JScript "%~F0" "%user%{tab}%pass%"

echo user and password okay
echo.

::After the timeout, simulate the "enter" key pressing
timeout %wt%
CScript //nologo //E:JScript "%~F0" {enter}

echo Done /n
echo.

::go to end of file
goto :EOF 

@end

WScript.CreateObject("WScript.Shell").SendKeys(WScript.Arguments(0));