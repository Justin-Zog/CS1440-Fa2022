# an OS-agnostic function to open URLs and files in the user's Desktop environment
_tutr_open() {
    if (( $# == 0 )); then
        _tutr_err  echo Usage: _tutr_open URL_OR_FILENAME
        return 1
    fi

    export _OPEN
    if [[ -z $_OPEN ]]; then 
        local _OS=$(uname -s)
        case $_OS in
            Darwin)
                _OPEN=open
                ;;
            Linux)
                if [[ -n $WSL_DISTRO_NAME ]]; then
                    cmd.exe /c "start $1" 2>/dev/null
                    return    
                else
                    _OPEN=xdg-open
                fi
                ;;
            *MINGW*)
                _OPEN=start
                ;;
            *)
                _tutr_err echo Unsupported OS $_OS, contact erik.falor@usu.edu for help
                return 1
                ;;
        esac
    fi

    # All of these redirections are necessary to keep the tutorial
    # from hanging until the spawned program exits
    $_OPEN $1 0</dev/null 1>/dev/null 2>/dev/null &
}
