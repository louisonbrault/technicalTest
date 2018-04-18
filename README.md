# technicalTest

This project is developped by Louison BRAULT

Before runing the app please follow those steps :

Go on top of the directory 
$ docker build -t mainapp .

Then go to /webSocket
$ docker build -t websocket .

Go back on top 
$ cd ..

Verify that you have the images 
$ docker image ls

Run the webSocket in the background, in detached mode
$ docker run -d -p 8888:8888 websocket

Run the mainapp in the same mode 
$ docker run -d -p 8000:80 mainapp

To stop the containers 
$ docker container ls
$ docker container stop IDWEBSOCKET
$ docker container stop MAINAPP

In your browser, go to http://localhost:8000

Now, you are ready to use the application
