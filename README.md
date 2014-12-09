ClogFirefoxParser
=================
Log file stored in /tmp that logs mouse and keyboard events through the CoreGraphics framework of OS X.  Described in https://www.mozilla.org/en-US/security/advisories/mfsa2014-90/

Use this python script to parse the log file for KeyUp or KeyDown events and print the characters that were typed.  

#Usage
```
usage: cglog-firefox-parser.py [-h] [-v] [-k] file

Read event records from a CGLog file and parse them for KeyUp or KeyDown
events. Then parse the record for character being typed.

positional arguments:
  file           Path to CGLog file

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose output of full records
  -k, --KeyDown  Change mode to KeyDown (Default is KeyUp)
  ```

