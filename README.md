# Closest Points API

This Django application provides an API endpoint to find the closest points among a given set of points on a grid. It also stores the received set of points and their closest points in a database.

### Create and activate a virtual environment:
`python3 -m venv venv`
`source venv/bin/activate`

### Install dependancies:
`pip install -r requirements.txt`

### Apply the database migrations:
`python manage.py migrateß`

## Running Tests:
To run the tests for the Closest Points API, use the following command:
`python manage.py test`

## Usage
To use the Closest Points API, you can send a POST request to the /api/closest_points/ endpoint with the following parameters:

* `points`: A string representing the points on a grid, separated by semicolons (;). Each point should be in the format `x,y`.

Example request
`POST /api/closest_points/ Content-Type: application/json { "points": "2,2;-1,30;20,11;4,5"}`

The API will respond with the closest points among the provided set of points.

Example response:

`HTTP/1.1 201 Created
Content-Type: application/json
{
  "closest_points": "2,2;4,5"
}`







