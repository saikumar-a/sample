
text = editor.getText()
editor.clearAll()

#converts text to array
ids = text.replace("\n",",").replace("\r","").split(",")
out=""
for id in ids:
	out=out+"'"+id+"',"

#remove last comma	
out=out[:-1]

editor.addText("select * from hello where id in (%s)"%out)
editor.addText("\n\n")
editor.addText("select * from world where id in (%s)"%out)
