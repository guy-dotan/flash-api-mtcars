# MTCars Flask API


This is a simple example of a Flask API. The environment again is created through a `docker-compose` command, that again references the corresponding Dockerfile and requirements.txt file. 

First as usual you will need to sync your repo to pull the new files. To run this API, change your directory to the docker folder and run:

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. You will need to open a new terminal (be in the same directory) and run the following curl command to get a response

`curl http://localhost:5000/`

This API simply is an example of a very simple model to predict miles per gallon (mpg) using the mtcars dataset. You are allowed to input the following variables:
* model
* cyl
* disp
* hp
* drat
* wt
* qsec
* vs
* am
* gear
* carb

But only `cyl`, `disp`, `hp`, `drat`, `wt`, and `qsec` will be utiltized in the model.

Run the following curl command to see the results:

`curl -H "Content-Type: application/json" -X POST -d '{"model": "Duster 360", "cyl": 8, "disp": 360, "hp": 245, "drat": 3.21, "wt": 3.57, "qsec": 15.84, "vs": 0, "am": 0, "gear": 3, "carb": 4}' "http://localhost:5000/pred_mpg"`

The result should output about 15.75 mpg

To stop your server running the API, type `ctrl-C`. As usual, check to see if you have any docker containers running using `docker container ls` and stop them through `docker container kill <container-name>`
