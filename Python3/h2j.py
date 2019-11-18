
errors = []
warnings = []
info = []

j = {}
needComma = False
r = "{"


def convert(s):
    # Check if html2json is installed
    try:
        j = {}
        from html2json import collect
        collect(s, j)
        # Test if J is empty.
        # If so, something has probably gone wrong in the conversion.
        if not (j):
            raise SystemError(
                "The html2json module installed did not return any elements")
    except Exception as e:
        warnings.append(str(e))
        # Use custom html2json if not installed
        try:
            j = convertWithoutModule(s)
        except Exception as e:
            errors.append(str(e))

    print("Errors:")
    i = 0
    for error in errors:
        i = i+1
        print(str(i)+": "+error)
    if i == 0:
        print("None")

    print("Warnings:")
    i = 0
    for warning in warnings:
        i = i+1
        print(str(i)+": "+warning)
    if i == 0:
        print("None")

    print("Info:")
    i = 0
    for notification in info:
        i = i+1
        print(str(i)+": "+notification)
    if i == 0:
        print("None")

    if not j:
        return s
    return j


def convertWithoutModule(s):
    import json
    from html.parser import HTMLParser

    def start_object(name):
        global needComma
        global r
        if needComma:
            r = r + ","
        r = r + "\n \"" + name + "\": {"
        needComma = False

    def end_object(name):
        global r
        global needComma
        needComma = True
        r = r+"\n"+"}"

    def object_data(name):
        global r
        r = r+"\n\"data\":"+"\""+name+"\""

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            #print("Encountered a start tag:", tag)
            start_object(tag)

        def handle_endtag(self, tag):
            #print("Encountered an end tag :", tag)
            end_object(tag)

        def handle_data(self, data):
            object_data(data)
            #print("Encountered some data  :", data)

    parser = MyHTMLParser()
    parser.feed(s)
    parser.close()

    global r
    r = r + "}"

    try:
        r = json.loads(r)
        return json.dumps(r, indent=4, sort_keys=True)
    except Exception as e:
        warnings.append(str(e))
        return r

    # Algo for parsing json string:
    # 1) Find first }
    # 2) Select everything between } and the first { to the left of the } found (this is data)
    # 3) Get name of object between { and { selected in 2


if __name__ == "__main__":
    print("Import this module from the Python3 shell or from another file to use it.")
    pass
