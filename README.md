# Closest Points API

To determine which points on a grid are nearest to one another, this Django application offers an API endpoint. In a database, it also keeps the points that were received and their proximity points## Prerequisites

### Preliquisites
Before setting up this application, ensure that you have the following prerequisites installed on your system:

- Python (version 3)
- Pip (Python package installer)
- [Any other dependencies or tools required by your specific Django app as listed in the requirements.txt file]

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/kepha-okari/closest_points.git


### Create and activate a virtual environment:
`python3 -m venv venv`
`source venv/bin/activate`

### Install dependancies:
`pip install -r requirements.txt`

### Apply the database migrations:
`python manage.py migrate`

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



## Admin
to access the django admin portal. use the link below:
`http:\\localhost:8000\admin`

```bash
    username : admin
    password : !23qweASD





