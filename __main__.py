#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-14 15:29:12
# @Author  : Chenghao Mou (chenghao@gmail.com)

import typer
import logging.config

from hanziconv import HanziConv
from loguru import logger
from touchbar_lyric.utility import get_info
from touchbar_lyric.service import universal_search

import os, os.path
import touchbar_lyric.convert as convert
from touchbar_lyric.__init__ import Song

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
    }
)


def run(
    app: str = typer.Option(default="Spotify", help="Application to track"),
    debug: bool = typer.Option(
        default=False, is_flag=True, help="To show debug messages or not"
    ),
    traditional: bool = typer.Option(
        default=False,
        is_flag=True,
        help="Translate lyrics into Traditional Chinese if possible",
    ),
):  # pragma: no cover
    {True: logger.enable, False: logger.disable}[debug]("touchbar_lyric")

    if not debug:
        logger.disable("touchbar_lyric")
        logger.disable("__main__")

    media_info = get_info(app)
    if media_info is None:
        return

    convert.run()
    file_name = media_info.name + " - " + media_info.artists + ".txt"
    file_name = file_name.replace("  "," ")
    dir = os.path.join(os.path.dirname(__file__),"local/final")
    listdir = os.listdir(dir)
    #print(file_name)
    files = [name for name in listdir if os.path.isfile(os.path.join(dir, name))]
    #print(files)
    if(file_name in files):
        #print("outputting local")
        path = os.path.join(dir,file_name)
        f = open(path,"r")
        songs = []
        songs.append(
            Song(
                    title=media_info.name,
                    artists=",".join(media_info.artists),
                    target_title=media_info.name,
                    target_artists=media_info.artists,
                    lyric=f.read(),
                )
        )
    else:
        songs = universal_search(media_info.name, media_info.artists)
    
    for song in songs:
    
        #print(song.title+" "+song.artists)
        #print(song.lyric)
        
        if song.anchor(media_info.position):
            line: str = song.anchor(media_info.position)
            if traditional:
                line = HanziConv.toTraditional(line)
            print(line)
            break


if __name__ == "__main__":  # pragma: no cover
    typer.run(run)
