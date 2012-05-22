#!/usr/bin/env python
import optparse,pycurl
import os
import requests

BASE_URL = 'http://localhost:9876'

def create_album(album_title):
    payload = {'album_title':album_title}
    r = requests.post("%s/api/album/create/" % BASE_URL,data=payload)
    print r.text
    
def add_to_album(album_title,arguments):
    for filename in arguments:
        print 'Adding %s to %s' % (filename,album_title)
        if not os.path.isfile(filename):
            print '\tFile does not exist!'
    
def list_album(album_title):
    r = requests.get("%s/api/album/list/?album_title=%s" % (BASE_URL,album_title))
    print r.text
    
def delete_from_album(album_title,arguments):
    for filename in arguments:
        print 'Deleting %s from %s' % (filename,album_title)
        if not os.path.isfile(filename):
            print '\tFile does not exist!'

def main():
    
    p = optparse.OptionParser()
    
    p.add_option('--create_album','-c',metavar="ALBUM_TITLE",help='Create an album with title ALBUM_TITLE')
    p.add_option('--add_to_album','-a',metavar="ALBUM_TITLE",help="""Add file(s) to album with title ALBUM_TITLE
    
    photos.py -a album1 /path/to/photo1 /path/to/photo2 """)
    p.add_option('--list_album','-l',metavar="ALBUM_TITLE",help='List all photos in ALBUM_TITLE')
    p.add_option('--delete_from_album','-d',metavar="ALBUM_TITLE",help="""Delete given photo(s) from ALBUM_TITLE
    
    photos.py -d album1 /path/to/photo_to_delete""")
    
    (options, arguments) = p.parse_args()
    
    if options.create_album:
        create_album(options.create_album)
    elif options.add_to_album:
        if not arguments: 
            print "Need to specify photo(s) to add to this album!"
        else:
            add_to_album(options.add_to_album,arguments)
    elif options.list_album:
        list_album(options.list_album)
    elif options.delete_from_album:
        if not arguments: 
            print "Need to specify photo(s) to delete from this album!"
        else:
            delete_from_album(options.delete_from_album,arguments)
    else:
        p.print_help()

if __name__=="__main__":
    main()