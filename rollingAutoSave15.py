import nuke
import glob
import time
import os
import datetime
import re

### Example that implements a rolling autosave using the autoSaveFilter callbacks
###
## autosaves roll from 0-9 eg myfile.autosave, myfile.autosave1, myfile.autosave2...
#
## To use just add 'import nukescripts.autosave' in your init.py


def onAutoSave(filename):

  fileNo = 1
  files = getAutoSaveFiles(filename)

  if len(files) > 0 :
    lastFile = files[-1]
    # get the last file number

    if len(lastFile) > 0:
      try:
        fileNo = int(lastFile[-3:])
      except:
        pass

      fileNo = fileNo + 1

  filename = filename + str(time.strftime("__%m-%d-%Y__%I-%M-%p__")) + 'v' + str('{0:03d}'.format(fileNo))

  if ( len(files) > 15 ):
    os.remove(files[0])

  return filename


def onAutoSaveRestore(filename):

  files = getAutoSaveFiles(filename)

  if len(files) > 0:
    filename = files[-1]

  return filename, re.IGNORECASE


def onAutoSaveDelete(filename):

  return None


def getAutoSaveFiles(filename):
  date_file_list = []
  files = glob.glob(filename + '*')
  files.extend( glob.glob(filename) )

  for file in files:
      # retrieves the stats for the current file as a tuple
      # (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
      # the tuple element mtime at index 8 is the last-modified-date
      stats = os.stat(file)
      # create tuple (year yyyy, month(1-12), day(1-31), hour(0-23), minute(0-59), second(0-59),
      # weekday(0-6, 0 is monday), Julian day(1-366), daylight flag(-1,0 or 1)) from seconds since epoch
      # note:  this tuple can be sorted properly by date and time
      lastmod_date = time.localtime(stats[8])
      #print image_file, lastmod_date   # test
      # create list of tuples ready for sorting by date
      date_file_tuple = lastmod_date, file
      date_file_list.append(date_file_tuple)

  date_file_list.sort()
  return [ filename for _, filename in date_file_list ]


nuke.addAutoSaveFilter( onAutoSave )
nuke.addAutoSaveRestoreFilter( onAutoSaveRestore )
nuke.addAutoSaveDeleteFilter( onAutoSaveDelete )

### As an example to remove the callbacks use this code
#nuke.removeAutoSaveFilter( onAutoSave )
#nuke.removeAutoSaveRestoreFilter( onAutoSaveRestore )
#nuke.removeAutoSaveDeleteFilter( onAutoSaveDelete )
