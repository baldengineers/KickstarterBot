#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetKeyDelay, 100

chromePageWait()
	{
	global
	Loop 50
		{
		while (A_Cursor = "AppStarting")
			continue
		Sleep, 100
		}
	}

Eval(x)
{
   StringGetPos i, x, +, R
   StringGetPos j, x, -, R
   If (i > j)
      Return Left(x,i)+Right(x,i)
   If (j > i)
      Return Left(x,j)-Right(x,j)
   StringGetPos i, x, *, R
   StringGetPos j, x, /, R
   If (i > j)
      Return Left(x,i)*Right(x,i)
   If (j > i)
      Return Left(x,j)/Right(x,j)
   Return x
}

Left(x,i)
{
   StringLeft x, x, i
   Return Eval(x)
}
Right(x,i)
{
   StringTrimLeft x, x, i+1
   Return Eval(x)
}

no_zero(number)
{
	return RegExReplace(RegExReplace(number,"(\.\d*?)0*$","$1"),"\.$")
}

^j::
	Run, C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
	Run, https://www.kickstarter.com/signup?ref=nav
	sleep, 100
	Run, https://10minutemail.com/10MinuteMail/index.html
	sleep, 100
	Run, http://www.pseudorandom.name/
	sleep, 100
	Run, https://lastpass.com/generatepassword.php
	WinMaximize A
	;while (A_Cursor = "AppStarting")
	;		continue
	;sleep, 1000
	chromePageWait()
	sleep, 1000
	;MsgBox, done loading
	
	;copy password, x out window, store it in variable
	Send {Tab}{Tab}{Tab}{Tab}{Tab}{Tab}{Tab}^c
	sleep, 100
	Send ^+{Tab}
	sleep, 500
	pass = %clipboard%
	;MsgBox, pass is %pass%
	
	
	;copy the random name, x out window, and store it in a variable
	Send ^a
	sleep, 100
	Send ^c
	sleep, 100
	Send ^+{Tab}
	sleep, 500
	fullname = %clipboard%
	;MsgBox, name is %fullname%
	
	;copy email address
	Send, ^c
	sleep, 500
	email = %clipboard%
	
	;get randomly generated name (obsolete)
	;fullname := % ComObjCreate("WScript.Shell").Exec("cmd.exe /c names").StdOut.ReadAll()
	
	;save credentials into file
	Loop, Read, accounts.txt
	{
		total_lines = %A_Index%
	}

	if (no_zero(Eval(total_lines)) != 0) {
		i = % no_zero(Eval(total_lines/4))
	} else {
		i = 0
	}
	FileAppend, [user%i%]`nname=%fullname%`nemail=%email%`npass=%pass%`n, accounts.txt
	
	;Send ^1
	;Send ^w 						;close the new tab window and now focused on the kickstarter window
	Send ^+{Tab}
	sleep, 500
	;Send {Tab}{Tab}
	sleep, 100
	Send %fullname%
	Send {Tab}^v ;paste the email from clipboard
	Send {Tab}^v
	Send {Tab}%pass%
	Send {Tab}%pass%
	
Return