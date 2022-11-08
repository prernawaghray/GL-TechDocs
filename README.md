
# TechDocs - Document Management System

It is a dockerized, mobile-ready, offline-storage compatible, JS-powered Latex editor.

- Marketing Pages [Home, Features, Help/FAQ, Pricing, Register, Login ]  
- Dashboard Pages [Dashboard-Home/MyDocuments, User Account, Latex Document Editor, Trash]

## Features

- Signup & Login With email-passowrd or with Google Account 
- Realtime Preview while editing the Latex document
- Save, Edit, View, Mark As Draft, Publish
- Sync Documents with Dropbox, Google Drive
- Share with specific permissions
- Manage Trash
- Download PWA Application into Mobile/Desktop 
- Edit in offline mode


## Tech



### Backend

### Frontend
Techdocs fronted uses a number of open source projects
- [Bootstrap] : great UI boilerplate for modern web apps
- [Python Flask]  : For URL Based Routing & Rendering HTML Templates
- [jQuery] - UI/UX Actions/Events on HTML Documents
- [LatexJS] - JS Library to preview latex document

## Installation

### [Frontend]
```bash
git clone https://github.com/prernawaghray/GL-TechDocs.git
cd GL-TechDocs/frontend

# Check the code in start.sh and make sure if port is 56733 for dev purpose and 80/443 for production purpose
sudo bash start.sh

# Docker container[techdocs-frontend] will be built & it will run. Get into docker and install node packages
docker exec -it techdocs-frontend bash
npm install
exit
```
Check http://localhost:56733 in the browser.
### [Backend]
```bash
cd /home/ec2-user
mkdir -p /techdocs_filesystem/log
touch /techdocs_filesystem/log/filemanager.log
git clone https://github.com/prernawaghray/GL-TechDocs.git
cd GL-TechDocs/backend
#Update the docker-compose.yml file line#11 with below:
/home/ec2-user/techdocs_filesystem:/tmp
docker-compose up --build --scale app=3 -d
```
## License


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Bootstrap]: <https://getbootstrap.com>
   [jQuery]: <http://jquery.com>
   [Python Flask]: <https://flask.palletsprojects.com/en/2.2.x/>
   [LatexJS]: <https://latex.js.org/>
