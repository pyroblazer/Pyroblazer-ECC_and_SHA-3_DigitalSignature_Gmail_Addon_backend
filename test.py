import chardet


test = "\u0011\u00c0'\u00d9hp\u000f\u00eb"
print(test)
#print(chardet.detect(test))
test = test.encode()
print(test)
test = test.decode("utf-8", "strict")
print(test)
# #test = bytes(test, "utf-8")
# #print(test)
