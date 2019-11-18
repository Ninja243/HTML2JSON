import urllib.request as urllib
import h2j
import datetime

page_html = ""

try:
    raise Exception("Forced to use cache for testing")
    page_html = urllib.urlopen("https://mweya.duckdns.org", data=None).read()
except Exception as e:
    print("Can't use the internet using cached version")

#page_html = """<html> a</html>   """

    page_html = """<!DOCTYPE HTML>
        <html>
            <head>
                <title>Test page</title>
                <link href="test_resource" rel="stylesheet"/>
                <script href="test_script"/>
            </head>
            <body>
                <h1>Hello</h1>
                <i>This is a test</i>
                <img src="testSite"/>
            </body>
        </html>"""

try:
    res = h2j.convert(page_html)
    filename = "test-" + str(datetime.datetime.now()) + ".log.json"
    f = open(filename, "w")
    f.write(res)
    f.close()
    print("Log of result of conversion saved to "+filename)
    if res:
        if not (res == ""):
            print("Test passed")
        else:
            print("Test failed")
    else:
        print("Test failed")
except Exception as e:
    print(str(e))
