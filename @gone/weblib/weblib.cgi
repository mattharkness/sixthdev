#!c:\program files\python\python
#
# weblib.cgi : a wrapper script for weblib
# inspired by http://www.webtechniques.com/archives/1998/02/kuchling/
#
# USAGE:
#
# Either do #!/your_path/weblib.cgi at the top of your CGI script,
# or save this in your cgi-bin, and do this in your Apache .htaccess file:
#
# Action application/python-script /cgi-bin/weblib.cgi
# AddType application/python-script .py


## debugging help ################################################
## you can uncomment this temporarily if you need help 
## debugging Internal Server Errors..

#import sys
#print "content-type: text/plain"
#print
#sys.stderr = sys.stdout

## import required modules #######################################
import os.path, sys, string, weblib, StringIO

## allow imports from script directory ###########################

path = os.environ["PATH_TRANSLATED"]
dir = string.join(string.split(path,os.sep)[:-1], os.sep)
sys.path.append(dir)
import os
os.chdir(dir)

## handle binary mode issues for stdio on win32:
import os, sys
if sys.platform=="win32":
    import msvcrt
    msvcrt.setmode(sys.__stdin__.fileno(), os.O_BINARY)
    msvcrt.setmode(sys.__stdout__.fileno(), os.O_BINARY)

## build the engine ##############################################
eng = weblib.Engine()
eng.start()

## run .weblib.py ################################################

whichfile = dir+os.sep+".weblib.py"
if os.path.exists(whichfile):
    # we use execute instead of run because we only want
    # to run the setup once.
    eng.execute(open(whichfile))


## run the script ################################################

# eng.result is None if nothing's been run yet
if (eng.result is None) or (eng.result == eng.SUCCESS):
    whichfile = os.environ["PATH_TRANSLATED"]
    if os.path.exists(whichfile):
        eng.execute(open(whichfile))
    else:
        eng.stop()
        print "Status: 404"
        sys.exit()

## close down shop and show the results  ########################
eng.stop()

if eng.result in (eng.SUCCESS, eng.EXIT):
    ## print the results    
    print eng.response.getHeaders() + eng.response.buffer
else:
    ## print debug output
    print "Content-Type: text/html"
    print
    print weblib.trim("""
          <html>
          <head>
          <title>weblib error</title>
          <style type="text/css">
              body, p {
                  background: #cccccc;
                  font-family: verdana, arial;
                  font-size: 75%;
              }
              pre { font-size: 120%; }
              pre.traceback { color: red; }
              pre.output{ color : green }
          </style>
          </head>
          """)

    if eng.result == eng.FAILURE:
        print "<b>assertion failure:</b>", eng.error

    elif eng.result == eng.EXCEPTION:
    
        print "<b>weblib error while running %s</b><br>" \
              % whichfile
        print '<pre class="traceback">' \
              + weblib.htmlEncode(eng.error) + "</pre>"

        print "<b>script input:</b>"

        print '<ul>'
        print '<li>form: %s</li>' % eng.request.form
        print '<li>querystring: %s</li>' % eng.request.querystring
        print '<li>cookie: %s</li>' % eng.request.cookie
        print '</ul>'

	print '<b>session data:</b><br>'
        print '<ul>'
	for item in eng.sess.keys():
            print '<li>', item, ': '
            try:
               print eng.sess[item]
            except:
               print '(can\'t unpickle)'
	    print '</li>'
        print '</ul>'
	
        print "<b>script output:</b>"
        print '<pre class="output">' + \
              weblib.htmlEncode(eng.response.getHeaders()) + \
              weblib.htmlEncode(eng.response.buffer) + \
              "</pre>"
        
    print "<hr>"
    print '<a href="http://weblib.sourceforge.net/">weblib</a> ' + \
          '(c) copyright 2000 ' + \
          '<a href="http://www.zike.net/">Zike Interactive</a>. ' + \
          'All rights reserved.'    
    print "</html>"
