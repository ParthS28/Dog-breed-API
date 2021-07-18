# Dog-breed-API
An API for predicting the breed of a dog.

## How to use

Run
`docker build -t dog-breed .` and then
`docker run -p 80:80 dog-breed`

Or 
Create a virtual environment using `virtualenv venv` and activate it using `source venv/bin/activate`

Download requirements using `pip install -r requirements.txt` and then `cd app` where you run `uvicorn main:app --reload`

After that you can go to `http://127.0.0.1:8000/docs` to see the swagger UI and test the API. 

