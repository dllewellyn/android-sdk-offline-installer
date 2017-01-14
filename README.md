# README #

This python script is intended to allow someone to download the Android repository offline, and then host it offline.

### How do I get set up? ###

* First, start the script. It will listen on port 8084
* Start up the Android SDK manager
* Change the proxy settings to point to the server (if running locally, 127.0.0.1 port 8084 by default)
* Reload and download the packages you want (these will report failures in your repository)
* All done - to use the offline repository, simply point your SDK proxy to the server
