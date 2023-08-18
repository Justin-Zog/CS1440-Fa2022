#!/bin/sh

_HELP="
Demo Lesson
===========
* Demonstrate how lesson steps are tested
* Write helpful hints
* Show how to recover when put into a bad state

Commands used in this lesson
============================
* echo
* touch
* rm
"

PATH=$PWD/.:$PATH

. shell-compat-test.sh

source record.sh
if [[ -n $_TUTR ]]; then
	source generic-error.sh
	source nonce.sh
fi

setup() {
	_tutr_record_repeat_prompt
	source screen-size.sh 80 68
	export _BASE=$PWD/demo-lesson
	[[ -d "$_BASE" ]] && rm -rf "$_BASE"
	mkdir -p "$_BASE"
	touch "$_BASE/delete-me.txt"
}


prologue() {
	echo
	cat <<-PROLOGUE
	Demo Shell Lesson: How to write a shell lesson

	In this lesson you will learn how to

	* Use a lesson
	* Write hints

	Commands used in this lesson
	============================
	* echo
	* touch
	* rm

	Let's get started!

	PROLOGUE

	_tutr_pressanykey
}


cleanup() {
	# Remember that this lesson has been completed
	(( $# >= 1 && $1 == $_COMPLETE)) && _tutr_record_completion ${_TUTR#./}
	[[ -d "$_BASE" ]] && rm -rf "$_BASE"
	echo "You worked on the Demo Lesson for $(_tutr_pretty_time)"
}


epilogue() {
	cat <<-'EPILOGUE'
	  _____                        __       __     __  _             
	 / ___/__  ___  ___ ________ _/ /___ __/ /__ _/ /_(_)__  ___  ___
	/ /__/ _ \/ _ \/ _ `/ __/ _ `/ __/ // / / _ `/ __/ / _ \/ _ \(_-<
	\___/\___/_//_/\_, /_/  \_,_/\__/\_,_/_/\_,_/\__/_/\___/_//_/___/
	              /___/                                              

	EPILOGUE

	_tutr_pressanykey
}


echo_hello_world_prologue() {
	cat <<-MSG
	Let's start small with "echo hello world"
	MSG
}

echo_hello_world_test() {
	if _tutr_nonce; then return $PASS
	else _tutr_generic_test -c echo -a "[Hh][Ee][Ll][Ll][Oo]" -a world
	fi
}

echo_hello_world_hint() {
	_tutr_generic_hint $1 echo
}

echo_hello_world_epilogue() {
	cat <<-'MSG'
	Wow, I can't believe you figured out how to do that!

	You're a shell super star!
	             _    
	          /\| |/\ 
	          \ ` ' / 
	         |_     _|
	          / , . \ 
	          \/|_|\/ 
	                  
	MSG
}




touch_a_file_prologue() {
	cat <<-'MSG'
	Now let's make a file called 'a-file' with the 'touch' command
	MSG
}

touch_a_file_pre_nope() {
	[[ -f "$_BASE/a-file" ]] && rm -f "$_BASE/a-file" 
}

touch_a_file_test() {
	if _tutr_nonce; then return $PASS
	elif [[ $PWD != $_BASE ]]; then return $WRONG_PWD
	elif [[ -f "$_BASE/a-file" ]]; then return 0
		# Look at the form of the command to see if they did it right
	else _tutr_generic_test -c touch -a a-file
	fi
}

touch_a_file_hint() {
	_tutr_generic_hint $1 touch "$_BASE"
	cat <<-HINT

	Try running 'touch a-file'
	HINT
}

touch_a_file_epilogue() {
	cat <<-'MSG'
	 __        __          _   
	 \ \      / /__   ___ | |_ 
	  \ \ /\ / / _ \ / _ \| __|
	   \ V  V / (_) | (_) | |_ 
	    \_/\_/ \___/ \___/ \__|
	
	MSG
}




rm_a_file_prologue() {
	cat <<-MSG
	Okay, now that you know how to create, it's time to learn how to destroy

	Snap your fingers and make the file 'delete-me.txt' disappear
	MSG
}

rm_a_file_pre() {
	[[ ! -f "$_BASE/delete-me.txt" ]] && touch "$_BASE/delete-me.txt"
}

rm_a_file_test() {
	if _tutr_nonce cd pushd popd; then return $PASS
	elif [[ -f "$_BASE/delete-me.txt" ]]; then return 99
	# elif [[ ! -f "$_BASE/delete-me.txt" ]]; then return 0
	else _tutr_generic_test -c rm -a delete-me.txt -d "$_BASE"
	fi
}

rm_a_file_hint() {
	case $1 in
		99)
			cat <<-HINT
			No!!! You must destroy the file you love!!!
			HINT
			;;
		*)
			_tutr_generic_hint $1 rm "$_BASE"
			;;
	esac

	if [[ ! -f "$_BASE/delete-me.txt" ]]; then
		cat <<-HINT
		You've really screwed things up this time.

		I think you can run 'tutor fix' to put humpty-dumpty back together again
		HINT
	fi

	cat <<-HINT

	Try running 'rm delete-me.txt'
	HINT
}


source main.sh && _tutr_begin \
	echo_hello_world \
	touch_a_file \
	rm_a_file

# vim: set filetype=sh noexpandtab tabstop=4 shiftwidth=4 textwidth=76 colorcolumn=76:
