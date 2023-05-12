#!/usr/bin/env python3
import configparser
import json

# catver2lpl.py: Build lpl playlists from catver.ini (and a few other things)
# See LICENSE in this repo for licensing info

def read_cfg(filename=None):
    cfg = configparser.ConfigParser()
    cfg.read(filename)
    return cfg

def read_json(filename=None):
    fp = open(filename, 'r')
    return json.load(fp)

def create_playlist(lpl=None):
    ''' The default playlist has all sorts of juicy settings.
        Let's just copy them and nuke the item list as a good 
        starting point for our new playlist.
    '''
    if lpl is None:
        return {}
    playlist = lpl.copy()
    playlist['items'] = []
    return playlist

if __name__ == '__main__':
    import argparse
    import pathlib
    import operator

    catver = None
    lpl = None
    playlists = {}

    p = argparse.ArgumentParser()
    p.add_argument('-i', '--ini', metavar='CATVER.INI',
            help='catver.ini path')
    p.add_argument('-l', '--lpl', metavar='BASE.LPL',
            help='path to main playlist db')
    p.add_argument('-o', '--output', metavar='OUT_PATH', 
            default=pathlib.Path.cwd(),
            help='output dir [optional]')
    args = p.parse_args()

    lpl = read_json(args.lpl)
    catver = read_cfg(args.ini)

    for item in lpl['items']:
        basename = pathlib.PurePath(item['path']).stem
        category = catver.get('Category', basename, fallback=None)
        if not category:
            continue
        if playlists.get(category, None) is None:
            playlists[category] = create_playlist(lpl)
        playlists[category]['items'].append(item)

    for category, playlist in playlists.items():
        # try to get the games in alphabetical order...
        playlist['items'].sort(key=operator.itemgetter('label'))
        # Clean up category name for use as a filename
        category = category.replace('/', '-')
        ppath = pathlib.PurePath(args.output, f'{category}.lpl')
        with open(ppath, 'w') as fp:
            fp.write(json.dumps(playlist, indent=4, sort_keys=True))

