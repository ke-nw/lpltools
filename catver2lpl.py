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

if __name__ == '__main__':
    import argparse
    import pathlib
    catver = None
    lpl = None

    p = argparse.ArgumentParser()
    p.add_argument('--ini', metavar='CATVER.INI',
            help='catver.ini path')
    p.add_argument('--lpl', metavar='BASE.LPL',
            help='path to main playlist db')
    p.add_argument('--output', metavar='OUTPUT_PATH', default=pathlib.Path.cwd(),
            help='output dir')
    args = p.parse_args()

    lpl = read_json(args.lpl)
    catver = read_cfg(args.ini)

    for item in lpl['items']:
        basename = pathlib.PurePath(item['path']).stem
        category = catver.get('Category', basename, fallback=None)
