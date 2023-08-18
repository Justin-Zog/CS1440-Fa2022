# Functions for Git repositories

# Convert the current Git repo's $1 remote URL into HTTPS
# If $1 is unspecified, use 'origin'
# Store converted URL in $REPLY; unset $REPLY on error
_tutr_git_repo_https_url() {
	local URL
	if git status >/dev/null 2>&1 ; then
		URL=$(git remote get-url ${1:-origin})
		if [[ $URL == git@* ]]; then
			URL=${URL/:/\/}
			URL=${URL/git@/https:\/\/}
		elif [[ $URL = https://* ]]; then
			:
		else
			_tutr_warn echo "Unrecognized URL '$URL'"
			unset REPLY
			return
		fi
		REPLY=${URL/ (*)//}
	else
		echo This is not a Git repository
		unset REPLY
	fi
}


# Return codes for by _tutr_git_status
_GF_CHANGED=1
_GF_STAGED=2
_GF_ADDED=4
_GF_DELETED=8
_GF_UNTRACKED=16
_GF_IGNORED=32
_GF_RENAMED=64
_GB_AHEAD=128
_GB_BEHIND=256

# Get status of a file (optional) + current branch in only one call to `git status`
_tutr_git_status() {
    local stat=0

    # `git status` pipes to a curly braced command list because, in Bash,
    # variable scope behaves differently when piping directly to a `while` loop
    # when run in an interactive shell vs. a script.
    #
    # Somehow, the curly brace makes this OK.
    # It worked in Zsh without this chicanery.
    git status --branch --ignored --porcelain=v1 | {
        while IFS=$'\n' read line; do
			if [[ $line == "## "*...*/* ]]; then
				if [[ $line = *ahead* ]]; then
					(( stat |= _GB_AHEAD ))
				elif [[ $line = *behind* ]]; then
					(( stat |= _GB_BEHIND ))
				fi
				continue
			fi
			(( $# == 0 )) && break
            [[ $line != *$1 ]] && continue
            case $line in
                "MM $1")         (( stat |= _GF_CHANGED | _GF_STAGED )) ;;
                A[\ MTD]" $1")   (( stat |= _GF_ADDED )) ;;
                ?"M $1")         (( stat |= _GF_CHANGED )) ;;
                "M  $1")         (( stat |= _GF_STAGED )) ;;
                "D  $1")         (( stat |= _GF_DELETED | _GF_STAGED )) ;;
                " D $1")         (( stat |= _GF_DELETED )) ;;
                "?? $1")         (( stat |= _GF_UNTRACKED )) ;;
                "!! $1")         (( stat |= _GF_IGNORED )) ;;
                R[\ MTD]" "*$1*) (( stat |= _GF_RENAMED )) ;;
            esac
        done
        return $stat
    }
}


# return 0 iff file $1 has no changes; ignores branch status
_tutr_file_clean() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_clean takes 1 argument
	_tutr_git_status $1
	(( ($? & 127) == 0))
}

# return 0 iff file $1 has only unstaged changes
_tutr_file_unstaged() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_unstaged takes 1 argument
	_tutr_git_status $1
	(( $? & (_GF_CHANGED|_GF_DELETED) ))
}


# return 0 iff file $1 has only staged changes
_tutr_file_staged() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_staged takes 1 argument
	_tutr_git_status $1
	(( $? & (_GF_STAGED|_GF_ADDED) ))
}


# return 0 iff file $1 has been added to the index
_tutr_file_added() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_added takes 1 argument
	_tutr_git_status $1
	(( $? & _GF_ADDED ))
}


# return 0 iff file $1 has staged and/or unstaged changes
_tutr_file_changed() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_changed takes 1 argument
	_tutr_git_status $1
	(( $? & (_GF_CHANGED|_GF_DELETED|_GF_STAGED|_GF_ADDED) ))
}


# return 0 iff file $1 has been deleted
_tutr_file_deleted() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_deleted takes 1 argument
	_tutr_git_status $1
	(( $? & _GF_DELETED ))
}


# return 0 iff file $1 is untracked
_tutr_file_untracked() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_untracked takes 1 argument
	_tutr_git_status $1
	(( $? & _GF_UNTRACKED ))
}


# return 0 iff file $1 is ignored
_tutr_file_ignored() {
    (( $# == 1 )) || _tutr_die echo _tutr_file_ignored takes 1 argument
	_tutr_git_status $1
	(( $? & _GF_IGNORED ))
}


# Return the number of commits the current branch is ahead of its remote
# IMPORTANT!!!
# 0/non-zero DOES NOT indicate success/failure
_tutr_branch_ahead_count() {
    local stat=0

    # `git status` pipes to a curly braced command list because, in Bash,
    # variable scope behaves differently when piping directly to a `while` loop
    # when run in an interactive shell vs. a script.
    #
    # Somehow, the curly brace makes this OK.
    # It worked in Zsh without this chicanery.
    git status --branch --ignored --porcelain=v1 | {
        while IFS=$'\n' read line; do
			if [[ $line == "## "*...*/* ]]; then
				if [[ $line = *ahead* ]]; then
					stat=$line
					stat=${stat##* }
					stat=${stat%']'*}
					(( stat |= _GB_AHEAD ))
				elif [[ $line = *behind* ]]; then
					stat=$line
					stat=${stat##* }
					stat=${stat%']'*}
					(( stat |= _GB_BEHIND ))
				fi
				break
			else
				break
			fi
        done
        return $stat
    }
}


# return 0 iff the current branch is ahead of its remote
_tutr_branch_ahead() {
	_tutr_git_status
	(( $? & _GB_AHEAD ))
}


# return 0 iff the current branch is behind its remote
_tutr_branch_behind() {
	_tutr_git_status
	(( $? & _GB_BEHIND ))
}


# vim: set filetype=sh noexpandtab tabstop=4 shiftwidth=4 textwidth=76 colorcolumn=76:
