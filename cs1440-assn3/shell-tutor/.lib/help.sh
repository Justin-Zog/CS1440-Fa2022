# When this script is sourced with text redirected on STDIN,
# AND one the lesson gets one of the command line arguments -h|-help|--help
# Display the help message on STDIN
# Otherwise, error out b/c tutorials don't take command line arguments
#
# This script needs to be passed the lesson's cmdline args at the time it is sourced.
if [[ -z $_TUTR ]] && (( $# > 0 )); then
    case $1 in
        -h|-help|--help)
            if [[ -t 0 ]]; then
                1>&2 echo "Error: This tutorial does not accept command line arguments"
                1>&2 echo "       Try again without any extra arguments after the command"
                exit 2
            else
                cat
                exit 0
            fi
            ;;
        *)
            1>&2 echo "Usage: $0 [-h|-help|--help]"
            exit 1
            ;;
    esac
fi
