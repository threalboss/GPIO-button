import xkcd as xkcd
comic = xkcd.getRandomComic()
comic.download(output='/home/pi/Documents/XKCD', outputFile='{}.png'.format(comic.number))
