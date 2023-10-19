# TouchBarLyrics
forked from https://github.com/ChenghaoMou/touchbar-lyric 
- The objective is to display lyrics of any music app onto the touchbar of Macbook Pro devices from 2017-2023

When used in combination with LyricsX which stores the lyrics locally in local/src, it solves the problem of obtaining incorrect lyrics. 
convert.py converts lyrics from lyricsX in local/src to local/final
main.py searches for available lyrics in local/final and displays the lyric if available.

Known Issue: script process does not quit after running and the processes eventually clog up the memory
