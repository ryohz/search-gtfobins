# Usage
following command searches all command specified in the given file.
```
python main.py file sample.txt
```
example of suported file format is below
```
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/umount
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/base64
/usr/bin/su
/usr/bin/fusermount
/usr/bin/at
/usr/bin/mount
```
you can also search with immediate arguments like below
```
python main.py imdt find ssh 
```