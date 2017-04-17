# WAN_IP
Initial wanip.py - simplified to return a Wide Area Network I.P. Address and Time stamp. Creates two files under the /tmp/ directory on a Linux System. 
1. /tmp/wanip.tmp - Contains unmodified .html from the web. Utilizes simple web scrapping technique.
2. /tmp/data.ip - Contains a file created containing #Commented Entry and Time stamp. And The Users WAN-IP Address. 
Designed and released as a sample or module. To create persistent record of Dynamic Addressing Space from I.S.P.'s.

Requires - python or python3, with module built-ins for "bs4" to support BeautifulSoup
For python - apt-get install python-bs4, or pip install bs4
For python3 - apt-get install python3-bs4, or pip3 install bs4

Additional Dependency a variation of html5lib for bs4 support
Recommended - apt-get install python-html5lib 
Variations - (apt-get install python3-html5lib, pip install python-html5lib) or use lxml support in place of html5lib

Built Under a Debian Template.
