Backend Docs

Init google app engine with Python
https://console.developers.google.com/start/appengine

google app id: phonic-presence-582

To run locally (and allow everyone to see):
dev_appserver.py --host 0.0.0.0 <backend_path>

To deploy remote run:
appcfg.py -A phonic-presence-582 update app

To see the update go to:
http://phonic-presence-582.appspot.com/ams

git commands:

git clone <project url>

git pull

git status

git commit -am "comment"
git push

git reset --hard # hard reset, will revert my local changes
