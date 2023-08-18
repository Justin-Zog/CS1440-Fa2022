# vim: set expandtab tabstop=4 shiftwidth=4:

# Source this file only once
[[ -n $_TUTR_MAIN ]] && return 0
_TUTR_MAIN=sourced

source stdlib.sh


if [[ -n $ZSH_NAME ]]; then
    emulate -L zsh
    # Make the statusbar appear above the prompt in Zsh on MacOS
    setopt prompt_subst
fi


# Detect or install the rc-file shim
if [[ -z "$_TUTR" ]]; then
    case $SHELL in
        *zsh)
            if [[ ! -f "$HOME/.zshrc" ]]; then
                _tutr_install_shim "$HOME/.zshrc"
            elif ! grep -q "# shell tutorial shim DO NOT MODIFY" "$HOME/.zshrc"; then
                _tutr_install_shim "$HOME/.zshrc"
            fi
            ;;
        *bash)
            if [[ ! -f "$HOME/.bashrc" ]]; then
                _tutr_install_shim "$HOME/.bashrc"
            elif ! grep -q "# shell tutorial shim DO NOT MODIFY" "$HOME/.bashrc"; then
                _tutr_install_shim "$HOME/.bashrc"
            fi
            ;;
        *)
            _tutr_die printf "'Unable to install tutorial shim into your shell's startup file'"
            ;;
    esac

    export _TUTR=${ZSH_ARGZERO-$0} _TUTR_REV=$(git describe --always --dirty)

    # We want to run _tutr_begin() only once.  Because of the way we spawn a
    # subshell AND source the lesson script, _tutr_begin() would be invoked again
    # after the end of a lesson.
    #
    # This snippet of code returns 1 or 0 to ensure that _tutr_begin is only run
    # at the beginning of a lesson.
    if _tutr_has_function setup && ! setup ""; then
        _tutr_die printf "'$0 setup error: contact erik.falor@usu.edu for help'"
    fi
    $SHELL
    _DISPOSITION=$?
    _tutr_has_function cleanup && cleanup $_DISPOSITION
    [[ -f .s ]] && rm -f .s
    false
else
    _tutr_begin $@
fi
##
## WARNING!!! DO NOT ADD ANY COMMANDS BELOW THIS POINT!
##
## The last thing this script should do is run either `true` or `false` above.
## Adding another command can cause the prologue to be re-displayed upon exit
