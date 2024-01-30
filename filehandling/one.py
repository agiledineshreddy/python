#syntax: fp.open('file name.txt','mode')
#fp:: file poinder
fp=open('hyd.txt','w+')
fp.write("hgfdsaswdefrgthjkaaaaaaaaaaahaaaaaaama")
fp.seek(0)
data=fp.read()
print(data)