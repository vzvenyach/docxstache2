#!/usr/bin/env python2.7

import zipfile
import string
import pystache

def read_docx(filepath):
    # todo: Add test to make sure it's a docx
    zfile = zipfile.ZipFile(filepath)

    # return the xml
    return zfile.read("word/document.xml")

def replace_hash(kp, input_string):
	outstring = input_string
	for key, value in kp.iteritems():
		outstring = string.replace(outstring, key, value)
	return outstring

def replace_docx(filepath, newfilepath, newfile):
	zin = zipfile.ZipFile(filepath, 'r')
	zout = zipfile.ZipFile(newfilepath, 'w')
	for item in zin.infolist():
		buffer = zin.read(item.filename)
		if (item.filename != 'word/document.xml'):
			zout.writestr(item, buffer)
		else:
			zout.writestr('word/document.xml', newfile)
	zin.close()
	zout.close()
	return True

def docxstache(filename, kp, newfile):
	filexml = read_docx(filename)
	outxml = pystache.render(filexml.decode('utf-8'), kp, decode_errors="ignore")
	replace_docx(filename, newfile, outxml.encode('utf-8'))
	return True