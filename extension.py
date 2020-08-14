mydict={"png":"image",
       "doc":"word file",
       "ppt":"power point presentation",
       "py":"python"}
myfile=input("enetr file name")
myfile,separator,extension=myfile.partition(".")
print(myfile)
print(extension)
print("the extension of file is:",mydict.get(extension) )
