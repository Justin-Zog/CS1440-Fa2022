# variables that identify system features
# _OS   - OS type (Linux, Mac, or Windows)
# _PLAT - Platform (like OS but disambiguates Linux from WSL, and Git+Bash)
# _ARCH - Architecture (x86 vs. ARM)
# _SH   - Shell (Bash vs. Zsh)

case $(uname -s) in
    Darwin)
        _OS=MacOSX
        _PLAT=Apple
        ;;
    *MINGW*)
        _OS=Windows
        _PLAT=MINGW
        ;;
    Linux)   
        _OS=Linux
        if [[ -n $WSL_DISTRO_NAME || -n $WSL_INTEROP ]]; then
            _PLAT=WSL
        else
            _PLAT=Linux
        fi
        ;;
    *)
        _OS=unknown
        _PLAT=unknown
        ;;
esac

_ARCH=$(uname -m)

case $SHELL in
    *zsh)  _SH=Zsh ;;
    *bash) _SH=Bash ;;
    *)     _SH=unknown ;;
esac

export _OS _PLAT _ARCH _SH
