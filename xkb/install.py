#!/usr/bin/env python3

import sys
import os, shutil
from lxml import etree

lg = sys.argv[1]
xkbdir = "/usr/share/X11/xkb"


variants = etree.fromstring("""
	<variantList>
		<variant>
			<configItem>
				<name>tkslat</name>
				<shortDescription>lat</shortDescription>
				<description>Tks Latin</description>
			</configItem>
		</variant>
		<variant>
			<configItem>
				<name>tkscyr</name>
				<shortDescription>cyr</shortDescription>
				<description>Tks Cyrillic</description>
			</configItem>
		</variant>
		<variant>
			<configItem>
				<name>tksarb</name>
				<shortDescription>arb</shortDescription>
				<description>Tks Arabic</description>
			</configItem>
		</variant>
	</variantList>
""")

layout = etree.fromstring("""
	<layout>
		<configItem>
			<name>{}</name>
			<shortDescription>{}</shortDescription>
			<description>{}</description>
			<languageList>
				<iso639Id>{}</iso639Id>
			</languageList>
		</configItem>
	</layout>""".format(lg, lg, lg, lg))

shutil.copyfile(lg, xkbdir+"/symbols/"+lg)

root=etree.parse(xkbdir+"/rules/evdev.xml")

#xkbConfigRegistry → layoutList
#cr = root.find("xkbConfigRegistry")
#ll = cr.find("layoutList")
ll = root.find(".//layoutList")
ll.append(layout)
root.write(xkbdir+"/rules/evdev.xml", pretty_print=True)

