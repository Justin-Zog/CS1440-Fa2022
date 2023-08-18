#!/bin/sh


PATH="$PWD/.lib:$PATH"

. shell-compat-test.sh

source help.sh $@ <<HELP
Using Git Tags in a Project

* Add development phase tags to commits in a project
* Push tags to remote repository

Commands used in this lesson
============================
* git clone
* git log
* git remote
* git tag
* git push
HELP


_REPO_NAME=project
_REPO_URL_SSH=git@gitlab.cs.usu.edu:erik.falor/$_REPO_NAME

# Short hand repo name
# The suggested remote repository name for the student to use
_SUGGESTED_REMOTE_REPO_NAME=project

# Git commit ID as given by `git rev-parse --short HEAD`
_REPO_STARTER_COMMIT=dfd422f

# The short commit hash each tag should be on
_ANALYZED_COMMIT=c07e9db
_DESIGNED_COMMIT=7b49684
_IMPLEMENTED_COMMIT=98e4d57
_TESTED_COMMIT=67fb8a7
_DEPLOYED_COMMIT=$_REPO_STARTER_COMMIT

source ansi-terminal-ctl.sh
DuckieCorp()   { echo ${_Y}DuckieCorp${_z} ; }
_Git()         { (( $# == 0 )) && echo $(blu Git)          || echo $(blu $*); }
_analyzed()    { (( $# == 0 )) && echo $(ylw_ analyzed)    || echo $(ylw_ $*); }
_designed()    { (( $# == 0 )) && echo $(grn_ designed)    || echo $(grn_ $*); }
_implemented() { (( $# == 0 )) && echo $(cyn_ implemented) || echo $(cyn_ $*); }
_tested()      { (( $# == 0 )) && echo $(blu_ tested)      || echo $(blu_ $*); }
_deployed()    { (( $# == 0 )) && echo $(mgn_ deployed)    || echo $(mgn_ $*); }
_md()          { (( $# == 0 )) && echo $(blu MARKDOWN)     || echo $(blu $*) ; }
_local()       { (( $# == 0 )) && echo $(ylw local)        || echo $(ylw $*); }
_remote()      { (( $# == 0 )) && echo $(mgn remote)       || echo $(mgn $*); }
_origin()      { (( $# == 0 )) && echo $(red origin)       || echo $(red $*); }


source record.sh
if [[ -n $_TUTR ]]; then
	source generic-error.sh
	source git.sh
	source nonce.sh
	source open.sh
fi


repo_warning() {
	cat <<-MSG
	${_Y}        .         ${_Z}
	${_Y}       / \        ${_Z} The repository $(path ../../$_REPO_NAME) already exists.
	${_Y}      / _ \       ${_Z} This lesson requires you to re-clone this
	${_Y}     / | | \      ${_Z} repository to begin from scratch.
	${_Y}    /  | |  \     ${_Z}
	${_Y}   /   |_|   \    ${_Z} To proceed, you may delete that existing
	${_Y}  /     _     \   ${_Z} repository with $(cmd "rm -rf ../../$_REPO_NAME"),
	${_Y} /     (_)     \  ${_Z} or rename it with the $(cmd mv) command.
	${_Y}/_______________\ ${_Z}

	This repository will also be present on your Gitlab account.
	Later in this lesson you will be asked to choose a name for this
	$(_remote) repository.  Choose something unique to avoid a clash.
	MSG
}

warn_not_in_repo() {
	cat <<-MSG
	This step $(bld must) be completed inside the repository directory.
	You will be unable to complete this step outside of the repository.
	MSG
}

must_be_in_repo() {
	if [[ "$PWD" != "$_REPO_PATH" ]]; then
		_tutr_warn warn_not_in_repo
	fi
}

# Open the current Git repo's 1st remote web page (if present)
browse_to_repo() {
	_tutr_git_repo_https_url
	_tutr_open $REPLY || _tutr_warn echo "Open '$REPLY' in your web browser"
}

_progress() {
	if [[ -n $ZSH_NAME ]]; then
		emulate -L zsh
		setopt ksh_arrays
	fi

	PRAISE=(Excellent! Superb! Awesome! "So close!" "You did it!")
	local i=${1:-1}

	if (( i == ${#PRAISE[@]} )); then
		echo ${PRAISE[$i-1]}
	else
		echo "${PRAISE[$i-1]}  You are $i/5 of the way there!"
	fi

	if (( i >= 1 )); then
		echo $(_analyzed 0. analyzed)
	else
		echo $(_analyzed 0.) $(blk analyzed)
	fi

	if (( i >= 2 )); then
		echo $(_designed 1. designed)
	else
		echo $(_designed 1.) $(blk designed)
	fi

	if (( i >= 3 )); then
		echo $(_implemented 2. implemented)
	else
		echo $(_implemented 2.) $(blk implemented)
	fi

	if (( i >= 4 )); then
		echo $(_tested 3. tested)
	else
		echo $(_tested 3.) $(blk tested)
	fi

	if (( i >= 5 )); then
		echo $(_deployed 4. deployed)
	else
		echo $(_deployed 4.) $(blk deployed)
	fi

	echo
	_tutr_pressanykey
}


setup() {
	_tutr_record_repeat_prompt
	source screen-size.sh 80 30
	export _ORIG_PWD="$PWD"
	export _GPARENT="$(cd ../.. && pwd)"
	export _REPO_PATH="$_GPARENT/$_REPO_NAME"
	# Check if repo for lesson already exists
	if [[ -d "$_REPO_PATH/.git" ]]; then
		_tutr_err repo_warning
		return 1
	fi
}


prologue() {
	[[ -z $DEBUG ]] && clear
	cat <<-PROLOGUE
	Using Git Tags in a Project

	In this lesson you will learn how to

	* Add development phase tags to commits in a project
	* Push tags to $(_remote) repository

	Commands used in this lesson
	============================
	* git clone
	* git log
	* git remote
	* git tag
	* git push

	PROLOGUE

	_tutr_pressanykey

	cat <<-PROLOGUE

	$(ylw "Note that an internet connection is required for this lesson.")

	$(ylw "If you aren't online now, restart this lesson when you are.")

	PROLOGUE

	_tutr_pressanykey

	cat <<-MSG

	As you work on projects at $(DuckieCorp) you will pass many milestones.
	You will use $(_Git) tags to mark commits that show your progress:

	* $(_analyzed)
	  * Marks the end of the $(_analyzed analysis) phase
	* $(_designed)
	  * Marks the end of the $(_designed design) phase
	* $(_implemented)
	  * Marks the end of the $(_implemented implementation) phase
	* $(_tested)
	  * Marks the end of the $(_tested testing) phase
	* $(_deployed)
	  * Marks the end of the $(_deployed deployment) phase

	Don't worry, I'll walk you through each of these tags and explain what
	each of them mean in this lesson.

	MSG
	_tutr_pressanykey
}



prepare_to_clone_rw() {
	cd $_ORIG_PWD
}

prepare_to_clone_ff() {
	cd $_GPARENT
}

prepare_to_clone_prologue() {
	cat <<-MSG
	Just like the last lesson, I have prepared a practice project for you to
	use in this lesson.  Before you can clone it, $(cmd cd) out of the
	assignment's repository.

	Go to the $(bld grandparent) directory with $(cmd cd ../..)

	MSG
}

prepare_to_clone_test() {
	if   [[ "$PWD" == "$_GPARENT" ]]; then return 0
	elif _tutr_nonce; then return $PASS
	else return $WRONG_PWD
	fi
}

prepare_to_clone_hint() {
	case $1 in
		$PASS) ;;
		$WRONG_PWD) _tutr_minimal_chdir_hint "$_GPARENT" ;;
		# *) _tutr_generic_hint $1 git "$_REPO_PATH" ;;
	esac
}



clone_rw() {
	rm -rf "$_REPO_PATH"
}

clone_ff() {
	git clone $_REPO_URL_SSH
}

clone_pre() {
	if [[ -d "$_REPO_PATH/.git" ]]; then
		_tutr_err repo_warning
		return 1
	fi
}

clone_prologue() {
	cat <<-MSG
	Now that you're here, clone the repository at

	  $(path $_REPO_URL_SSH)
	MSG
}

clone_test() {
	HTTPS_URL=99
	if   _tutr_nonce rm; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = clone && ${_CMD[2]} = http* ]]; then return $HTTPS_URL
	else _tutr_generic_test -c git -a clone -a "^($_REPO_URL_SSH(.git)?)$" -d "$_GPARENT"
	fi
}

clone_hint() {
	case $1 in
		$PASS)
			;;

		$STATUS_FAIL)
			cat <<-MSG
			'git clone' failed unexpectedly.

			If the above error message includes the phrases "fatal: unable to
			access" and "Connection refused", that indicates an issue with your
			network connection.  Ensure that you are connected to the internet and
			try again.

			If the error persists or is different, please contact
			erik.falor@usu.edu for help.
			Copy the full command and all of its output.

			MSG
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_GPARENT"
			;;

		$HTTPS_URL)
			cat <<-MSG
			You cloned the repository with an HTTPS URL.  In this class you
			should always use SSH URLs with Git.

			Remove the repo you just cloned:
			  $(cmd rm -rf $_REPO_NAME)

			Then re-clone it by running:
			  $(cmd git clone $_REPO_URL_SSH)

			If you do not have an SSH key set up, reach out to
			erik.falor@usu.edu for help.
			MSG
			;;

		*)
			_tutr_generic_hint $1 git

			cat <<-MSG

			Clone the demo repo by running
			  $(cmd git clone $_REPO_URL_SSH)
			MSG
			;;
	esac
}

clone_epilogue() {
	cat <<-:
	FYI, the repository that you just cloned will be automatically erased
	from your computer at the end of this tutorial.

	:
	_tutr_pressanykey
}



cd_rw() {
	cd "$_GPARENT"
}

cd_ff() {
	cd "$_REPO_PATH"
}

cd_prologue() {
	cat <<-MSG
	Now go into the directory $(path $_REPO_NAME)
	MSG
}

cd_test() {
	if   [[ "$PWD" == "$_REPO_PATH" ]]; then return 0
	elif _tutr_nonce; then return $PASS
	else return $WRONG_PWD
	fi
}

cd_hint() {
	[[ $1 == $PASS ]] && return
	_tutr_minimal_chdir_hint "$_REPO_PATH"
}

cd_post() {
	## What is this for?
	if [[ $_RES -ne 0 ]]; then
		_tutr_die printf "'Then send it to erik.falor@usu.edu.'"
	fi
	_ORIG_URL=$(git remote get-url origin)
}



inspect_repo_pre() {
	must_be_in_repo
}

inspect_repo_prologue() {
	cat <<-MSG
	I want you to have a look at the commits that have been made in this
	repository, and see them in a new way.  This means learning a new $(_Git git)
	$(_Git log) trick.

	Plain, old $(_Git git log) shows a commit's ID, when it was made by whom, and
	the message they wrote about it.  With this information you can't really
	tell just how big of a change to the project that commit is.

	$(_Git git log)'s $(cmd --stat) option shows the files that were changed in the commit
	along with $(bld how much) each file was changed.  This will help you to
	recognize which commit constitutes which development phase.

	When viewing the $(_Git log), recall that

	  * $(kbd Up Arrow)/$(kbd k) scrolls up
	  * $(kbd Down Arrow)/$(kbd j) scrolls down
	  * $(kbd Space Bar) moves down by one screenful
	  * $(kbd g) scroll back to the top
	  * $(kbd q) quits

	Run $(cmd git log --stat) now.
	MSG
}

inspect_repo_test() {
	if _tutr_nonce; then return $PASS
	else _tutr_generic_test -c git -a log -a --stat -x -d "$_REPO_PATH"
	fi
}

inspect_repo_hint() {
	case $1 in
		$PASS) ;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"

			cat <<-MSG

			Run $(cmd git log --stat) to view the detailed commit log.
			MSG
			;;
	esac
}


inspect_repo_epilogue() {
	cat <<-MSG
	That's a lot of output!  Even without the $(cmd --stat) option this is a rather
	long $(_Git Git log) to read, because there are so many commits.

	The $(grn "+") and $(red "-") symbols indicate, in relative terms, the number of lines
	added to and removed from every file in each commit.  This gives you a
	sense of the $(bld magnitude) of change the commit represents.  You can see at
	a glance if one commit changed many files a little bit, or if a few
	files were completely re-written.

	Such information lets you identify commits that belong to each phase of
	the project.  For example, commits made in the $(_implemented implementation) phase will
	show many changes to files in $(path src/), while these files ought to be
	untouched during the $(_analyzed analysis) phase.  The only activity in the
	$(_deployed deployment) phase may be updates to files in $(path doc/).

	A common sign of the end of a phase is a commit that changes the
	$(_md Signature.md) file.

	Wait: was that last thing $(bld too) much of a hint? ;)

	MSG
	_tutr_pressanykey
}



remote_rename_rw() {
	for REMOTE in $(git remote); do
		git remote remove $REMOTE
	done
	git remote add origin $_REPO_URL_SSH
}

remote_rename_ff() {
	git remote rename origin old-origin
}

remote_rename_pre() {
	must_be_in_repo
}

remote_rename_prologue() {
	cat <<-MSG
	Now is time again to rename $(_origin) to $(_origin old-origin) with $(cmd git remote rename).

	Replace $(cmd '<old>') and $(cmd '<new>') as appropriate.
	MSG
}

remote_rename_hint() {
	if [[ $1 == $PASS ]]; then return; fi

	_tutr_generic_hint $1 git "$_REPO_PATH"

	cat <<-MSG

	If you want to see the $(_remote) repositories and their URLs, run:
	  $(cmd git remote -v)

	To rename $(_origin) to $(_origin old-origin), run:
	  $(cmd git remote rename origin old-origin)
	MSG
}

remote_rename_test() {
	if _tutr_nonce; then return $PASS
	elif [[ $PWD != $_REPO_PATH ]]; then return $WRONG_PWD
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = help ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = status ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = log ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = -v ]]; then return $PASS
	else
		if   git remote | command grep -q -E '^old-origin$'; then return 0
		# We allow removing origin as a valid solution here
		elif [[ $( git remote | wc -l ) = 0 ]] ; then return 0
		else _tutr_generic_test -c git -a remote -a rename -a origin -a old-origin -d "$_REPO"
		fi
	fi
}

remote_rename_post() {
	# Enable us to adjust prose if origin gets removed instead of renamed
	if [[ $(git remote | wc -l) = 0 ]]; then
		_REMOVED_ORIGIN=yep
	else
		_REMOVED_ORIGIN=nope
	fi
}

remote_rename_epilogue() {
	if [[ $_REMOVED_ORIGIN = yep ]]; then
		echo "Well, that was ONE way to do it."
	else
		echo "Perfect!"
	fi

	cat <<-MSG

	The reason I asked you to rename $(_origin) instead of just deleting it
	is so that your repository will always remember where it came from.
	This way, if I ever need to fix a bug in the starter code, you can
	easily incorporate it into your repository.

	MSG

	if [[ $_REMOVED_ORIGIN = yep ]]; then
		cat <<-MSG
		I see that you removed $(_origin).  Don't do that on a real assignment.
		Because it's not critical to this lesson, we'll just continue on.

		MSG
	fi
	_tutr_pressanykey
}



remote_add_rw() {
	git remote remove origin
}

remote_add_ff() {
	_tutr_info printf "'Just guessing... using /tmp/project as the remote URL for origin'"
	if [[ ! -d /tmp/project ]]; then
		git clone --bare $_REPO_PATH /tmp/project
	fi
	git remote add origin /tmp/project
}

remote_add_pre() {
	must_be_in_repo
}

remote_add_prologue() {
	cat <<-MSG
	Add a new URL under the name $(_origin) URL with $(cmd git remote add).  Just like
	last time, it will look like this:

	  git@gitlab.cs.usu.edu:$(mgn "<your_gitlab_username>")/$(cyn "<repository_name>")

	Use something descriptive, like $(wht "'$_SUGGESTED_REMOTE_REPO_NAME'"), for the new
	$(cyn "<repository_name>").  If you've already used that name on another
	repository, put a number after it so that it is unique.

	The command to use is
	  $(cmd git remote add origin NEW_URL)
	MSG
}

remote_add_test() {
	NO_ORIGIN_URL=99
	URL_NOT_GITLAB=98
	URL_USER_IS_ERIK=97
	URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH=96
	URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH=95
	URL_SCHEME_WRONG=94

	if   [[ $PWD != $_REPO_PATH ]]; then return $WRONG_PWD
	elif _tutr_nonce; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = help ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = status ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = log ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = -v ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = remove ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} = remote && ${_CMD[2]} = rename ]]; then return $PASS
	elif [[ ${_CMD[0]} = git && ${_CMD[1]} != remote ]]; then return 95
	fi

	local URL=$(git remote get-url origin 2>/dev/null)
	if   [[ -z $URL ]]; then return $NO_ORIGIN_URL
	elif [[ $URL != *gitlab.cs.usu.edu* ]]; then return $URL_NOT_GITLAB
	elif [[ $URL = [/:]*erik.falor/* ]]; then return $URL_USER_IS_ERIK
	elif [[ $URL = https://gitlab.cs.usu.edu:* ]]; then return $URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH
	elif [[ $URL = git@gitlab.cs.usu.edu/* ]]; then return $URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH
	elif [[ $URL != https:* && $URL != git@* ]]; then return $URL_SCHEME_WRONG
	elif [[ $URL = https://gitlab.cs.usu.edu/*/* || $URL = git@gitlab.cs.usu.edu:*/* ]]; then return 0
	else _tutr_generic_test -c git -n -d "$_REPO_PATH"
	fi
}

remote_add_hint() {
	case $1 in
		$PASS)
			return
			;;

		$NO_ORIGIN_URL)
			cat <<-MSG
			There is no $(_remote) called $(_origin).  Create it with
			  $(cmd git remote add origin NEW_URL).

			Replace "NEW_URL" in the above command with an address as
			described above (run $(cmd tutor hint) to review the instructions).

			MSG
			;;

		$URL_NOT_GITLAB)
			cat <<-MSG
			The hostname of the URL should be 'gitlab.cs.usu.edu'.

			If you push your code to the wrong Git server it will not be submitted.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_USER_IS_ERIK)
			cat <<-MSG
			$(_origin) points to the address of MY repo, not YOURS! The
			$(mgn "<gitlab_username>") portion of the URL is $(mgn erik.falor) when it should
			be replaced with $(bld your) username.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_IS_HTTPS_AMALGATION_OF_HTTPS_AND_SSH)
			cat <<-MSG
			The HTTPS address you entered will not work because there is a colon ':'
			between the hostname 'gitlab.cs.usu.edu' and your username.  (Use $(cmd git)
			$(cmd remote -v) to see for yourself).

			Instead of a colon that character should be a front slash '/'.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;

		$URL_IS_SSH_AMALGATION_OF_HTTPS_AND_SSH)
			cat <<-:
			This SSH address will not work because there is a slash '/' between the
			hostname 'gitlab.cs.usu.edu' and your username.  (Use $(cmd git remote -v) to
			see for yourself).

			Instead of a slash that character should be a colon ':'

			Use $(cmd git remote remove origin) to erase this and try again.
			:
			;;

		$URL_SCHEME_WRONG)
			cat <<-MSG
			The URL must start with $(bld git@).  Otherwise, Git will be unable
			to talk to the server.

			Use $(cmd git remote remove origin) to erase this and try again.
			MSG
			;;
		*)
			_tutr_generic_hint $1 'git remote' "$_REPO_PATH"
			;;
	esac
	cat <<-MSG

	After you figure out what NEW_URL should be, use this command:
	  $(cmd git remote add origin NEW_URL)

	Use $(cmd tutor hint) to review the instructions about the new URL.
	MSG
}

remote_add_epilogue() {
	if [[ "$(git remote -v | grep origin)" == *"https://"* ]]; then
		cat <<-MSG
		You setup your repository with an HTTPS URL. This will work, but isn't
		ideal. Just a heads up, you will be asked for your GitLab credentials
		frequently because of it.

		MSG
		_tutr_pressanykey
	fi
}



# There is no good way to rewind this action
# push_repo_rw() {}

push_repo_ff() {
	git push -u origin master
}

push_repo_prologue() {
	cat <<-MSG
	I'm sure that you saw this coming.  $(cmd git push) this repo to your
	new $(_origin origin).

	Remember to use the $(cmd -u) flag to set the $(_origin) as the default push
	destination.
	MSG
}

push_repo_test() {
	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if [[ ${_CMD[*]} = "git help push" ]]; then return $PASS
	elif [[ ${_CMD[*]} = "git remote"* ]]; then return $PASS
	elif _tutr_nonce; then return $PASS
	fi
	_tutr_generic_test -c git -a push -a -u -a origin -a master
}

push_repo_hint() {
	case $1 in
		$PASS)
			return
			;;
		*)
			_tutr_generic_hint $1 git "$_REPO_PATH"
			;;
	esac

	cat <<-MSG
	Run $(cmd git push -u origin master) to proceed.

	If you are having trouble pushing to the $(_remote), inspect the output of
	$(cmd git remote -v) to check that the remote URL was set correctly.

	If you made a mistake, fix it with $(cmd git remote set-url origin NEW_URL)

	MSG
}

push_repo_epilogue() {
	cat <<-MSG

	${_Y}      _         ${_Z} Your repository is now on GitLab!
	${_Y}     /(|        ${_Z}
	${_Y}    (  :        ${_Z} 
	${_Y}  ___\  \  _____${_Z} 
	${_Y} (____)  \`|     ${_Z} 
	${_Y}(____)|   |     ${_Z} I'll open this repo's home page in your web 
	${_Y} (____).__|     ${_Z} browser so you can see what it looks like.  
	${_Y}  (___)__.|_____${_Z}

	MSG

	browse_to_repo

	if [[ -n $REPLY ]]; then
		cat <<-MSG

		If a browser window didn't pop up for you, go to
		  $(cmd $REPLY)

		MSG
	fi

	_tutr_pressanykey
}



analyzed_ff() {
	git tag analyzed $_ANALYZED_COMMIT
}

analyzed_rw() {
	git tag -d analyzed
}

analyzed_pre() {
	typeset -ix _FAIL=0
}

analyzed_prologue() {
	cat <<-:
	With that business out of the way, you can tag the commits that mark the
	ends of the various phases of this project.  This will be different than
	the workflow you should use for your own projects; instead of tagging
	commits after the fact, you should make your tags as you go.

	:

	_tutr_pressanykey

	cat <<-:

	The first tag you will make is $(_analyzed), marking the end of the first
	two phases.  In these phases you re-write the project requirements in
	your own words and identify the inputs and outputs of the overall
	program.  The product of these phases are changes to $(_md Plan.md) and
	$(_md Signature.md).

	:

	_tutr_pressanykey

	cat <<-:

	Using $(cmd git log --stat), locate the commit that represents the culmination
	of the $(_analyzed analysis) phase.  It will be one of the earliest commits in the
	log, and can be found near the bottom.  Make note of its commit ID, and
	run $(cmd git tag analyzed COMMIT_ID) to place the tag.  Note the spelling of
	this tag - it must be written in lower-case and in the past-tense.

	If you make a mistake, run $(cmd git tag -d TAG_NAME) to delete the tag
	and try again.
	:
}

analyzed_test() {
	ON_WRONG_COMMIT=99
	TAG_DOESNT_EXIST=98
	TAG_NAME_SHA1=97

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	fi

	TAG_ON_COMMIT=$(git rev-parse --short analyzed 2> /dev/null)

	if [[ "$PWD" != "$_REPO_PATH"* ]]; then
		return $WRONG_PWD
	elif git tag --list | command grep -q $_ANALYZED_COMMIT; then
		(( _FAIL++ ))
		return $TAG_NAME_SHA1
	elif [[ -z $TAG_ON_COMMIT ]]; then
		(( _FAIL++ ))
		return $TAG_DOESNT_EXIST
	elif [[ "$TAG_ON_COMMIT"* == "$_ANALYZED_COMMIT"* ]]; then
		return 0
	else
		(( _FAIL++ ))
		return $ON_WRONG_COMMIT
	fi
}

analyzed_hint() {
	case $1 in
		$PASS)
			return
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			return
			;;

		$ON_WRONG_COMMIT)
			cat <<-MSG
			That wasn't the right commit to tag $(_analyzed).

			Delete the tag with $(cmd git tag -d analyzed), look at the log again,
			and try tagging another commit.

			MSG
			;;

		$TAG_DOESNT_EXIST)
			if (( _FAIL < 4 )); then
				cat <<-MSG
				Find the ID of the commit you think best represents the
				culmination of the first two phases of this project, then run
				  $(cmd git tag analyzed COMMIT_HASH)
				to tag it $(_analyzed).

				MSG
			fi
			;;

		$TAG_NAME_SHA1)
			cat <<-MSG
			You created a tag with the name $(ylw_ $_ANALYZED_COMMIT) instead of $(_analyzed).

			Delete this tag by running
			  $(cmd git tag -d $_ANALYZED_COMMIT)

			Then look for the commit that best represents the culmination of
			the first two phases of this project, and tag that $(_analyzed).

			MSG
			;;
	esac

	if (( _FAIL < 4 )); then
		cat <<-MSG
		Remember, you are trying to place the tag $(_analyzed) on the commit that
		ends the $(_analyzed analysis) phase.  In this phase only the files $(_md Plan.md) and
		$(_md Signature.md) should be changed.

		The commit message will say something like
		  "The project has been analyzed".
		MSG
	else
		cat <<-MSG
		This command will place the $(_analyzed) tag on the right commit:
		  $(cmd git tag -f analyzed $_ANALYZED_COMMIT)

		MSG
	fi
}

analyzed_epilogue() {
	_progress 1
}



designed_ff() {
	git tag designed $_DESIGNED_COMMIT
}

designed_rw() {
	git tag -d designed
}

designed_pre() {
	typeset -ix _FAIL=0
}

designed_prologue() {
	cat <<-MSG
	The next tag to place is $(_designed).  This tag denotes the end of the
	phase where you write $(bld pseudocode) that describes the general shape
	that your program will take.  It is still too early to commit yourself
	to one specific implementation, which is why you are advised to forgo
	writing $(bld real) Python code.

	Therefore, this phase consists of changes to $(_md Plan.md) and $(_md Signature.md),
	and should $(bld not) include changes to any of the files in $(path src/).

	MSG

	_tutr_pressanykey

	cat <<-MSG

	Use $(cmd git log --stat) to locate the commit representing the end of the
	$(_designed design) phase.  It will still be an early commit, but one that comes after
	$(_analyzed).  Make note of its ID, and run $(cmd git tag designed COMMIT_ID) to
	place the tag.  Again, this tag's name is lower-case and past-tense.

	The commit messages in this repo are detailed and accurate.  This helps
	you identify which commit should be tagged $(_designed).
	MSG
}

designed_test() {
	ON_WRONG_COMMIT=99
	TAG_DOESNT_EXIST=98
	TAG_NAME_SHA1=97

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	fi

	TAG_ON_COMMIT=$(git rev-parse --short designed 2> /dev/null)

	if [[ "$PWD" != "$_REPO_PATH"* ]]; then
		return $WRONG_PWD
	elif git tag --list | command grep -q $_DESIGNED_COMMIT; then
		(( _FAIL++ ))
		return $TAG_NAME_SHA1
	elif [[ -z $TAG_ON_COMMIT ]]; then
		(( _FAIL++ ))
		return $TAG_DOESNT_EXIST
	elif [[ "$TAG_ON_COMMIT"* == "$_DESIGNED_COMMIT"* ]]; then
		return 0
	else
		(( _FAIL++ ))
		return $ON_WRONG_COMMIT
	fi
}

designed_hint() {
	case $1 in
		$PASS)
			return
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			return
			;;

		$ON_WRONG_COMMIT)
			cat <<-MSG
			That wasn't the right commit to tag $(_designed).

			Delete the tag with $(cmd git tag -d designed), look at the log again,
			and try tagging another commit.

			MSG
			;;

		$TAG_DOESNT_EXIST)
			if (( _FAIL < 4 )); then
				cat <<-MSG
				Find the ID of the commit you think best represents the end of the
				$(_designed design) phase, then run
				  $(cmd git tag designed COMMIT_HASH)
				to tag it $(_designed).

				MSG
			fi
			;;

		$TAG_NAME_SHA1)
			cat <<-MSG
			You created a tag with the name $(ylw_ $_DESIGNED_COMMIT) instead of $(_designed).

			Delete this tag by running
			  $(cmd git tag -d $_DESIGNED_COMMIT)

			Then look for the commit that best represents the culmination of
			the first two phases of this project, and tag that $(_designed).

			MSG
			;;
	esac

	if (( _FAIL < 4 )); then
		cat <<-MSG

		The $(_designed) tag belongs on the commit that wrapped up the $(_designed design)
		phase.  Look for a commit which changes $(_md Plan.md) and $(_md Signature.md), and
		has a message along the lines of "finished designing the project."
		MSG
	else
		cat <<-MSG
		This command will place the $(_designed) tag on the right commit:
		  $(cmd git tag -f designed $_DESIGNED_COMMIT)

		MSG
	fi
}

designed_epilogue() {
	_progress 2
}



implemented_ff() {
	git tag implemented $_IMPLEMENTED_COMMIT
}

implemented_rw() {
	git tag -d implemented
}

implemented_pre() {
	typeset -ix _FAIL=0
}

implemented_prologue() {
	cat <<-MSG
	After $(_designed design) comes $(_implemented implementation).  In this phase, you can (finally)
	write code!  If you spent your time in the $(_designed design) phase wisely, this
	part of the project goes smoothly as you translate $(bld pseudocode) into a
	working program.

	This is not to say that your program will be perfect at first; it will
	still need some testing and tweaking before it is just right.  But I
	think you will find that a thorough design gets you pretty close.

	MSG

	_tutr_pressanykey

	cat <<-MSG

	This time, look for a commit that changes files in $(path src/) and $(path doc/).

	Tag it $(_implemented).  Mind your spelling!  If you make a mistake, try
	again after $(cmd git tag -d TAG_NAME).
	MSG
}

implemented_test() {
	ON_WRONG_COMMIT=99
	TAG_DOESNT_EXIST=98
	TAG_NAME_SHA1=97

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	fi

	TAG_ON_COMMIT=$(git rev-parse --short implemented 2> /dev/null)

	if [[ "$PWD" != "$_REPO_PATH"* ]]; then
		return $WRONG_PWD
	elif git tag --list | command grep -q $_IMPLEMENTED_COMMIT; then
		(( _FAIL++ ))
		return $TAG_NAME_SHA1
	elif [[ -z $TAG_ON_COMMIT ]]; then
		(( _FAIL++ ))
		return $TAG_DOESNT_EXIST
	elif [[ "$TAG_ON_COMMIT"* == "$_IMPLEMENTED_COMMIT"* ]]; then
		return 0
	else
		(( _FAIL++ ))
		return $ON_WRONG_COMMIT
	fi
}

implemented_hint() {
	case $1 in
		$PASS)
			return
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			return
			;;


		$ON_WRONG_COMMIT)
			cat <<-MSG
			That wasn't the right commit to tag $(_implemented).

			Delete the tag with $(cmd git tag -d implemented), look at the log again,
			and try tagging another commit.

			MSG
			;;

		$TAG_DOESNT_EXIST)
			if (( _FAIL < 4 )); then
				cat <<-MSG
				Find the ID of the commit you think best represents the
				culmination of the $(_implemented implementation) phase, then run
				  $(cmd git tag implemented COMMIT_HASH)
				to tag it $(_implemented).

				MSG
			fi
			;;

		$TAG_NAME_SHA1)
			cat <<-MSG
			You created a tag with the name $(ylw_ $_IMPLEMENTED_COMMIT) instead of $(_implemented).

			Delete this tag by running
			  $(cmd git tag -d $_IMPLEMENTED_COMMIT)

			Then look for the commit that best represents the culmination of
			the $(_implemented implementation) phase, and tag that $(_implemented).

			MSG
			;;
	esac

	if (( _FAIL < 4 )); then
		cat <<-MSG
		Tag the commit that ends the $(_implemented implementation) phase with the name
		$(_implemented).  Look for a commit that changes source files in $(path src/)
		$(bld AND) documentation in $(path doc/).

		Look for a message that mentions fixing a $(bld syntax error).
		MSG
	else
		cat <<-MSG
		This command will place the $(_implemented) tag on the right commit:
		  $(cmd git tag -f implemented $_IMPLEMENTED_COMMIT)
		MSG
	fi
}

implemented_epilogue() {
	_progress 3
}



tested_ff() {
	git tag tested $_TESTED_COMMIT
}

tested_rw() {
	git tag -d tested
}

tested_pre() {
	typeset -ix _FAIL=0
}

tested_prologue() {
	cat <<-MSG
	The next tag is $(_tested), marking the end of the $(_tested testing) phase.
	A program is never truly bug-free, but there does come a point when it
	is not profitiable to search for more bugs.

	Documentation made during the $(_tested testing) phase details which tests were
	performed and what bugs were found (and fixed) as a result.

	Mark the last commit that involves testing with the $(_tested) tag.
	MSG
}

tested_test() {
	ON_WRONG_COMMIT=99
	TAG_DOESNT_EXIST=98
	TAG_NAME_SHA1=97

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	fi

	TAG_ON_COMMIT=$(git rev-parse --short tested 2> /dev/null)

	if [[ "$PWD" != "$_REPO_PATH"* ]]; then
		return $WRONG_PWD
	elif git tag --list | command grep -q $_TESTED_COMMIT; then
		(( _FAIL++ ))
		return $TAG_NAME_SHA1
	elif [[ -z $TAG_ON_COMMIT ]]; then
		(( _FAIL++ ))
		return $TAG_DOESNT_EXIST
	elif [[ "$TAG_ON_COMMIT"* == "$_TESTED_COMMIT"* ]]; then
		return 0
	else
		(( _FAIL++ ))
		return $ON_WRONG_COMMIT
	fi
}

tested_hint() {
	case $1 in
		$PASS)
			return
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			return
			;;


		$ON_WRONG_COMMIT)
			cat <<-MSG
			That wasn't the right commit to tag $(_tested).

			Delete the tag with $(cmd git tag -d tested), look at the log again,
			and try tagging another commit.

			MSG
			;;

		$TAG_DOESNT_EXIST)
			if (( _FAIL < 4 )); then
				cat <<-MSG
				Find the ID of the commit you think best represents the
				culmination of the first two phases of this project, then run
				  $(cmd git tag tested COMMIT_HASH)
				to tag it $(_tested).

				MSG
			fi
			;;

		$TAG_NAME_SHA1)
			cat <<-MSG
			You created a tag with the name $(ylw_ $_TESTED_COMMIT) instead of $(_tested).

			Delete this tag by running
			  $(cmd git tag -d $_TESTED_COMMIT)

			Then look for the commit that best represents the culmination of
			the $(_tested testing) phase of this project, and tag that $(_tested).

			MSG
			;;
	esac

	if (( _FAIL < 4 )); then
		cat <<-MSG
		Remember, you are trying to place the tag $(_tested) on the commit that
		ends the $(_tested testing) phase.

		Look for a commit message that mentions making bug fixes and meeting
		specifications.
		MSG
	else
		cat <<-MSG
		This command will place the $(_tested) tag on the right commit:
		  $(cmd git tag -f tested $_TESTED_COMMIT)

		MSG
	fi
}

tested_epilogue() {
	_progress 4
}



deployed_ff() {
	git tag deployed $_DEPLOYED_COMMIT
}

deployed_rw() {
	git tag -d deployed
}

deployed_pre() {
	typeset -ix _FAIL=0
}

deployed_prologue() {
	cat <<-MSG
	When your $(DuckieCorp) project is ready to show the world, tag it
	$(_deployed).  This signifies that the development work is over, and the
	project has shifted into maintenance mode.

	In your own projects, the $(_deployed) tag may be on the same commit as
	$(_tested); this is fine because $(_Git) commits can have multiple tags.

	This project, however, has separate commits for both phases.
	MSG
}

deployed_test() {
	ON_WRONG_COMMIT=99
	TAG_DOESNT_EXIST=98
	TAG_NAME_SHA1=97

	# nonce commands
	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git tag -d"* ]]; then return $PASS
	fi

	TAG_ON_COMMIT=$(git rev-parse --short deployed 2> /dev/null)

	if [[ "$PWD" != "$_REPO_PATH"* ]]; then
		return $WRONG_PWD
	elif git tag --list | command grep -q $_DEPLOYED_COMMIT; then
		(( _FAIL++ ))
		return $TAG_NAME_SHA1
	elif [[ -z $TAG_ON_COMMIT ]]; then
		(( _FAIL++ ))
		return $TAG_DOESNT_EXIST
	elif [[ "$TAG_ON_COMMIT"* == "$_DEPLOYED_COMMIT"* ]]; then
		return 0
	else
		(( _FAIL++ ))
		return $ON_WRONG_COMMIT
	fi
}

deployed_hint() {
	case $1 in
		$PASS)
			return
			;;

		$WRONG_PWD)
			_tutr_minimal_chdir_hint "$_REPO_PATH"
			return
			;;


		$ON_WRONG_COMMIT)
			cat <<-MSG
			That wasn't the right commit to tag $(_deployed).

			Delete the tag with $(cmd git tag -d deployed), look at the log again,
			and try tagging another commit.

			MSG
			;;

		$TAG_DOESNT_EXIST)
			if (( _FAIL < 4 )); then
				cat <<-MSG
				Find the ID of the commit you think best represents the
				culmination of the first two phases of this project, then run
				  $(cmd git tag deployed COMMIT_HASH)
				to tag it $(_deployed).

				MSG
			fi
			;;

		$TAG_NAME_SHA1)
			cat <<-MSG
			You created a tag with the name $(ylw_ $_DEPLOYED_COMMIT) instead of $(_deployed).

			Delete this tag by running
			  $(cmd git tag -d $_DEPLOYED_COMMIT)

			Then look for the commit that best represents the culmination of
			the $(_deployed deployment) phase of this project, and tag that $(_deployed).

			MSG
			;;
	esac

	if (( _FAIL < 4 )); then
		cat <<-MSG
		Look for the commit that mentions handing the project over to
		$(DuckieCorp) management.
		MSG
	else
		cat <<-MSG
		The last commit gets the tag $(_deployed).

		This command will put the $(_deployed) tag on that commit:
		  $(cmd git tag -f deployed $_DEPLOYED_COMMIT)

		MSG
	fi
}

deployed_epilogue() {
	_progress 5
}



push_all_tags_ff() {
	git push origin --tags
}

push_all_tags_rw() {
	git push origin -d analyzed designed implemented tested deployed
}

push_all_tags_prologue() {
	cat <<-MSG
	Tagging commits in your $(_local) repo is necessary, but not sufficient
	for getting a good grade.  Ultimately, these tags demonstrate to your
	grader that you followed the steps of the $(cyn Software Development Plan).

	Now it's time to push all of your tags up to GitLab.  You could do this
	one-by-one.  But I know that you would rather be $(bld lazy) and do it in
	one command:

	  $(cmd git push origin --tags)

	Push those tags now.
	MSG
}

push_all_tags_test() {
	ON_WRONG_COMMIT=99
	AT_LEAST_ONE_TAG_NOT_PUSHED=98

	[[ "$PWD" != "$_REPO_PATH"* ]] && return $WRONG_PWD

	if _tutr_nonce; then return $PASS
	elif [[ ${_CMD[*]} == *"--tags" ]]; then
		if (( ${#_CMD[@]} == 3)); then
			_tutr_generic_test -c git -a push -a "--tags"
		else
			_tutr_generic_test -c git -a push -a origin -a "--tags"
		fi
	elif [[ ${_CMD[*]} == "git remote"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git log"* ]]; then return $PASS
	elif [[ ${_CMD[*]} == "git help"* ]]; then return $PASS
	else
		git ls-remote origin &> .ls-remote
		ANALYZED_TAG_REF=$(command grep analyzed .ls-remote)
		DESIGNED_TAG_REF=$(command grep designed .ls-remote)
		IMPLEMENTED_TAG_REF=$(command grep implemented .ls-remote)
		TESTED_TAG_REF=$(command grep tested .ls-remote)
		DEPLOYED_TAG_REF=$(command grep deployed .ls-remote)

		if [[ -n $ANALYZED_TAG_REF && -n $DESIGNED_TAG_REF &&
			  -n $IMPLEMENTED_TAG_REF && -n $TESTED_TAG_REF &&
			  -n $DEPLOYED_TAG_REF ]]; then
			if [[ $ANALYZED_TAG_REF == "$_ANALYZED_COMMIT"* &&
				  $DESIGNED_TAG_REF == "$_DESIGNED_COMMIT"* &&
				  $IMPLEMENTED_TAG_REF == "$_IMPLEMENTED_COMMIT"* &&
				  $TESTED_TAG_REF == "$_TESTED_COMMIT"* &&
				  $DEPLOYED_TAG_REF == "$_DEPLOYED_COMMIT"* ]]; then
				# All tags are on gitlab and on the correct commits! Woo!
				return 0
			else
				return $ON_WRONG_COMMIT
			fi
		else
			return $AT_LEAST_ONE_TAG_NOT_PUSHED
		fi
	fi
}

push_all_tags_hint() {
	case $1 in
		$PASS)
			return
			;;

		$AT_LEAST_ONE_TAG_NOT_PUSHED)
			cat <<-MSG
			One (or more) tags are not pushed to GitLab.
			MSG
			;;

		$ON_WRONG_COMMIT)
			cat <<-MSG
			One (or more) of the tags were pushed to the wrong commits.

			Somehow, you arrived at the last step with a tag on the wrong commit.
			That $(bld really) should not have happened, unless you made some
			interesting changes since the step where you placed tags.

			So congratulations, I guess?

			To finish the lesson, you need to identify which tag is on the wrong
			commit, run
			  $(cmd 'git push -d <TAGNAME>')
			to delete it.  Then, place it on the correct commit and push again.
			MSG
			;;

		*)
			_tutr_generic_hint $1 "git push --tags" "$_REPO_PATH"
			;;
	esac
}


epilogue() {
	cat <<-EPILOGUE
	${_C}  _____                        __       __     __  _
	${_C} / ___/__  ___  ___ ________ _/ /___ __/ /__ _/ /_(_)__  ___  ___
	${_C}/ /__/ _ \\/ _ \\/ _ \`/ __/ _ \`/ __/ // / / _ \`/ __/ / _ \\/ _ \\(_-<
	${_C}\\___/\\___/_//_/\\_, /_/  \\_,_/\\__/\\_,_/_/\\_,_/\\__/_/\\___/_//_/___/
	${_C}              /___/

	Amazing!!! You consistently impress me with your success!

	You have correctly identified and tagged each development phase of this
	project.  Remember to do the same in your own projects from now on.

	FYI, the $(path $_REPO_NAME) repository that you cloned in this lesson will now
	be erased from your computer.  It is still on your account on GitLab.

	Run $(cmd ${SHELL##*/} make-certificate.sh) to generate your certificate of completion.

	EPILOGUE

	_tutr_pressanykey
}


cleanup() {
	if [[ -d "$_REPO_PATH" ]]; then
		echo "Cleaning up $_REPO_PATH..."
		rm -rf "$_REPO_PATH"
	fi

	if [[ -d /tmp/project ]]; then
		echo "Cleaning up /tmp/project..."
		rm -rf /tmp/project
	fi

	# Remember that this lesson has been completed
	(( $# >= 1 && $1 == $_COMPLETE)) && _tutr_record_completion ${_TUTR#./}
	echo "You learned about using Git tags in projects for $(_tutr_pretty_time)"
}



source main.sh \
	prepare_to_clone \
	clone \
	cd \
	inspect_repo \
	remote_rename \
	remote_add \
	push_repo \
	analyzed \
	designed \
	implemented \
	tested \
	deployed \
	push_all_tags


# vim: set filetype=sh noexpandtab tabstop=4 shiftwidth=4 textwidth=76 colorcolumn=76:
