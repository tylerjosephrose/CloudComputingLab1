# CloudComputingHW3
## Weather Forecast Website Docker Container
This docker container hosts the code found in my CloudComputingHW3 repository and provides API functionality as well as the website for the forecast that uses the APIs.

### APIs
This API provides access to the maximum and minimum tempratures for every day that is stored in the database and returns in json.
The availbility is as follows

Path | Data | Response | Types
--- | --- | --- | ---
`<address>/api/historical/` | All dates available in the database | [{"DATE": 20130101},] | GET, POST
`<address>/api/historical/YYYYMMDD | The max and min temperatures for the date at the end of the request | {"DATE": 20130101, "TMAX": 34.0, "TMIN": 26.0} | GET, DELETE
`<address>/api/forecast/YYYYMMDD | The forecast for the next 7 days as predicted | [{"DATE": 20130101, "TMAX": 39.8, "TMIN": 22.2},{"DATE": 20130102, "TMAX": 42.7, "TMIN": 22.7},] | GET

Please note that the post request requires a post body of `{"DATE": <Date to set>, "TMAX": <temp to set>, "TMIN": <temp to set>}`

### Website
This site has a form to select the date the user wants to display the forcast for. When the form is submitted, a table and chart appears through ajax that displays the predicted maximum and minimum temperature for the next seven days started at the date input by the user. The website can be found at `<address>/forecast`. If the date inputed is the current date, the prediction for the next 5 days will appear as well.

## Installation 
1. Build the docker image `docker build -t lab1 .`
2. Run the docker image `docker run -d -p 80:80`
3. In a browser navigate to http://127.0.0.1/forecast

## How To Use
Once you have it installed, you can view the website by navigating to the `127.0.0.1/forecast` From here you select your date using the dropdowns and hit submit. The table and chart will then appear underneath the form.
