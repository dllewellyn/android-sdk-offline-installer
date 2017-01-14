from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import requests
import os

PORT_NUMBER = 8084

DOWNLOAD = True

XML="Xml"
BINARY="Binary"
GOOGLE_REPO_UR="dl.google.com/android/repository/"

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        print self.path

		# Send the html message
        arr = self.path.split("/")
        p = arr[len(arr)-1]

        if "xml" in self.path:
            
            GOOGLE_REPO_UR=self.path
            xml = requests.get("{0}".format(GOOGLE_REPO_UR))

            if not os.path.exists("Xml/{0}".format(p)):
                with open("Xml/{0}".format(p), "wb") as xml_file:
                    xml_file.write(xml.content)
                    self.wfile.write(xml.content)
            else:
                with open("Xml/{0}".format(p)) as xml_file:
                    self.wfile.write(xml_file.read())
        elif "zip" in self.path:
            if not os.path.exists("{0}/{1}".format(BINARY, p)):
                response = requests.get(self.path, stream=True)

                handle = open("{0}/{1}".format(BINARY, p), "wb")
                for chunk in response.iter_content(chunk_size=512):
                    handle.write(chunk)

                with open("{0}/{1}".format(BINARY, p)) as zip_file:
                 self.wfile.write(zip_file.read())
            else:
                with open("{0}/{1}".format(BINARY, p)) as zip_file:
                 self.wfile.write(zip_file.read())


if not os.path.exists(XML):
    os.mkdir(XML)
#Create a web server and define the handler to manage the
#incoming request
server = HTTPServer(('', PORT_NUMBER), myHandler)
print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
server.serve_forever() 