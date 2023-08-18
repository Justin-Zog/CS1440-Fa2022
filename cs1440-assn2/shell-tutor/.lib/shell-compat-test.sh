# vim: set expandtab tabstop=4 shiftwidth=4:

# Exit when launched from an unsupported shell
#   Uses expernal `expr` program b/c I can't be sure whether this is being
#   evaluated in a shell with a sane `case` statement
if ! expr $SHELL : ".*/bash" \| $SHELL : ".*/zsh" >/dev/null; then
	1>&2 echo "Your current shell, $SHELL, is incompatible with the tutor"
	1>&2 echo "This tutorial may be run from Bash or Zsh"
	1>&2 echo
	exit 1
fi


# Check that /bin/sh supports built-in `[[` conditional expressions
if ! eval "[[ 1 == 1 ]]" >/dev/null 2>&1; then
	1>&2 echo "Your system's default shell '/bin/sh' isn't compatible with the tutor."
    1>&2 echo "Restart the lesson with '$(basename $SHELL) $0'"
    1>&2 echo
    exit 1
fi

# WIP - try to detect and work around Ubu's /bin/dash
# echo _=$_ 0=$0 SHELL=$SHELL
# if [ -z "$BASH" -a -z "$ZSH" ]; then
# 	case $(readlink /bin/sh) in
# 		*dash)
# 			echo "Your system's default shell isn't compatible with the tutor."
# 			if which bash >/dev/null 2>&1; then
# 				echo "Re-run the tutor with 'bash $0'"
# 			elif which zsh >/dev/null 2>&1; then
# 				echo "Re-run the tutor with 'zsh $0'"
# 			else
# 				echo Contact erik.falor@usu.edu for assistance
# 			fi
# 			#exit 1
# 			;;
# 	esac
# fi
