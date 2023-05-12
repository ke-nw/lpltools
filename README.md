# lpltools
Some tools for dealing with RetroArch/Lakka playlist files (*.lpl)

catver2lpl takes a `catver.ini` file like the one [here](https://github.com/libretro/mame2003-plus-libretro/tree/master/metadata)
and the default [Retroarch](https://www.retroarch.com) playlist for your core, like the one in `~/.config/retroarch/MAME\ 2003-Plus.lpl`
and builds a ton of playlists that look okay to me.

Usage: `./catver2lpl.py --ini /path/to/catver.ini --lpl /path/to/retroarch/master/playlist/MAME\ 2003-Plus.lpl`

Add `--output /some/path/that/exists` to dump all the playlists (140+) to some directory
