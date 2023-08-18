# Record the completion token in a hidden file named with $1
_tutr_record_completion() {
    if [[ -z $1 ]]; then
        echo "_tutr_record_completion(): No argument given"
        return 1
    elif [[ -n $_S ]]; then
        printf "%s\t%s\t%s\t%s\n" $1 $(command date +%s) $SECONDS $_S >> "${_ORIG_PWD+$_ORIG_PWD/}.$1"
    elif [[ -s "${_ORIG_PWD+$_ORIG_PWD/}.s" ]]; then
        printf "%s\t%s\t%s\t%s\n" $1 $(command date +%s) $SECONDS $(cat "${_ORIG_PWD+$_ORIG_PWD/}.s") >> "${_ORIG_PWD+$_ORIG_PWD/}.$1"
    else
        printf "%s\t%s\t%s\n" $1 $(command date +%s) $SECONDS >> "${_ORIG_PWD+$_ORIG_PWD/}.$1"
    fi
    git hash-object "${_ORIG_PWD+$_ORIG_PWD/}.$1" >> "${_ORIG_PWD+$_ORIG_PWD/}.$1"
}


# Check for the existence of the record token
_tutr_record_exists() {
    if [[ -z $1 ]]; then
        echo "_tutr_record_check(): No argument given"
        return 1
    else
        [[ -f "${_ORIG_PWD+$_ORIG_PWD/}.$1" ]]
    fi
}


# Ask user if they want to repeat the lesson
_tutr_record_repeat_prompt() {
	if _tutr_record_exists ${_TUTR#./}; then
		_tutr_warn printf "'You have already completed this lesson'"
		if ! _tutr_yesno "Would you like to do it again?"; then
			_tutr_info printf "'SEE YOU SPACE COWBOY...'"
			exit 1
		fi
	fi
}
