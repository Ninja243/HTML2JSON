
errors = []
warnings = []
info = []

j = {}

def convert(s):
    # Check if html2json is installed
    try:
        j = {}
        from html2json import collect
        collect(s, j)
        if j == None:
            # Something went wrong when converting, use custom html2json
            warnings.append("Something went wrong converting using html2json from pip")
            j = convertWithoutModule(s)
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
    print("Warnings:")
    i = 0
    for warning in warnings:
        i = i+1
        print(str(i)+": "+warning)
    print("Info:")
    i = 0
    for notification in info:
        i = i+1
        print(str(i)+": "+notification)
    
    i = 0
    for entry in j:
        i = i+1
        if i > 0:
            return j
        return s

def convertWithoutModule(s):
    raise Exception("Function for converting without module not completed")
    return s

if __name__ == "__main__":
    print("Import this module from the Python3 shell or from another file to use it.")
    pass