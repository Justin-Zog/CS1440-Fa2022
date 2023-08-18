_cmd_not_found() {
	cat <<-:
	The command [0;32m$1[0m was not found.  It is required for this lesson.

	Contact erik.falor@usu.edu for help
	:
}

_assert_program_exists() {
	if [[ -z $1 ]]; then
		cat <<-:
		Usage: _assert_program_exists PROGRAM_NAME [ERROR_MESSAGE_CMD]
		:
		return
	fi

	if ! which $1 &>/dev/null; then
		if [[ -n $2 ]]; then
			_tutr_die $2 $1
		else
			_tutr_die _cmd_not_found $1
		fi
	fi
}
