# Written by James Habben
# https://github.com/JamesHabben/ClogFirefoxParser

import sys
import re
import argparse

argParser = argparse.ArgumentParser(description='Read event records from a CGLog file and parse them for KeyUp or '
                                                'KeyDown events. Then parse the record for character being typed. ')
argParser.add_argument('-v', '--verbose', help='Verbose output of full records', action='store_true')
argParser.add_argument('-k', '--KeyDown', help='Change mode to KeyDown (Default is KeyUp)', action='store_true')
argParser.add_argument('file', help='Path to CGLog file')
args = argParser.parse_args()

print ' processing file {0}'.format(args.file)

tmpFile = open('/tmp/CGLog_Firefox_4287', 'r')
count = 0
for line in tmpFile :
    if (not args.KeyDown and line.find('KeyUp') >=0) or (args.KeyDown and line.find('KeyDown') >= 0) :
        if args.verbose :
            print line
        count += 1
        print unichr(int(re.search('char (\d+);', line).group(1))).strip(' '),

print '\n{0} lines found with {1}'.format(count, 'KeyDown' if args.KeyDown else 'KeyUp')
