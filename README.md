# TechDocs - Document Management System

## For Windows
1. Create a empty folder
2. Inside the empty folder create another empty folder named log
3. Inside the log folder create an empty file named 'filemanager.log'
4. Create an empty database 'glcaptest'
5. Clone the repo
6. Edit the sql username and password in the .env.local file
7. Run the python script 'def_Tables.py' inside Schema folder
8. In docker compose file line number 11 edit the first '/tmp' to the location of your newly created folder in step 1 
    
    volumes:
        - "C:/Users/Dell/Desktop/backend_test:/tmp"
9. Build and up the docker-compose (docker-compose up --build)
10. Navigate to 'http://127.0.0.1:5000/' to check if the server is running