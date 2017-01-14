import requests
import xml.etree.ElementTree as ET
import os

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


BASE="http://dl.google.com/android/repository/"

GOOGLE_REPO_UR="dl.google.com/android/repository/repository-11.xml"
xml = requests.get("http://{0}".format(GOOGLE_REPO_UR))

repos = os.listdir("Xml")

size = 0 
for repo in repos:
	print repo
	
	try:
		tree = ET.parse("Xml/{0}".format(repo))
		root = tree.getroot()

		rep = repo.split("-")[1]
		rep = rep.split(".")[0]

		ns = {"sdk": "http://schemas.android.com/sdk/android/repository/{0}".format(rep)}
	except:
		pass

		for child in root:
			if "license" in child.tag:
				print "License"
				continue # Don't care about license
			else:
				try:
					for sdk_archive in child.find("sdk:archives", ns).findall("sdk:archive", ns):
						
						size += int(sdk_archive.find("sdk:size", ns).text)
						filename = sdk_archive.find("sdk:url", ns).text
						
						url = "{0}{1}".format(BASE, filename)
						print filename, sizeof_fmt(int(sdk_archive.find("sdk:size").text))
						# response = requests.get(url, stream=True)

						# handle = open("Binary/{0}".format(filename), "wb")
						# for chunk in response.iter_content(chunk_size=512):
						# 	handle.write(chunk)
				except:
					pass
print sizeof_fmt(size)

