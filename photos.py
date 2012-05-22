#!/usr/bin/env python
import optparse,pycurl
import os
import requests
import json

BASE_URL = 'http://localhost:9876'

def create_album(album_title):
    payload = {'album_title':album_title}
    r = requests.post("%s/api/album/create/" % BASE_URL,data=payload)
    json_response = json.loads(r.text)
    if json_response.has_key('error'):
        print json_response['error']
    else:
        if json_response['created']:
            print "Created new album with title: %s" % album_title
        else:
            print "Album with this title (%s) already exists!" % album_title
    
def add_to_album(album_title,arguments):
    #First make sure this album exists (if not create)
    requests.post("%s/api/album/create/" % BASE_URL,data={'album_title':album_title})
    for filename in arguments:
        print 'Adding %s to %s' % (filename,album_title)
        if not os.path.isfile(filename):
            print '\tFile does not exist!'
        else:
            r = requests.post("%s/api/album/add/" % BASE_URL,data={'album_title':album_title,'filename':filename})
            json_response = json.loads(r.text)
            if json_response.has_key('error'):
                print '\t%s' % json_response['error']
            else:
                print "\tSuccessfully added this photo!"
    
def list_album(album_title):
    r = requests.get("%s/api/album/list/?album_title=%s" % (BASE_URL,album_title))
    json_response = json.loads(r.text)
    if json_response.has_key('error'):
        print json_response['error']
    else:
        for photo in json_response['album']['photos']:
            absolute_url = '%s%s' % (BASE_URL,photo['relative_path'])
            print '%s\t%s' % (photo['id'],absolute_url)
    
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