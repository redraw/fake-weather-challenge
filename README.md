# fake-weather-challenge

## Install
Clone the repo,

```bash
$ git clone --recurse-submodules git@github.com:redraw/fake-weather-challenge.git
```

or 

```bash
$ git clone git@github.com:redraw/fake-weather-challenge.git
$ git submodule update --init
```

That way we can also fetch the `mock-weather-api` submodule.

## Run

```bash
$ docker-compose up
```
Go to `http://localhost:8000`

## API 
### `GET /api/temp`

- lat: latitude
- lon: longitude
- providers: separated by comma. Possible values: noaa, accuweather, weatherdotcom
- unit: default is celsius. Possible values: celsius, fahrenheit

```
GET /api/temp/?lat=33.3&lon=22.5&providers=noaa,accuweather
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "avg": {
        "celsius": 12.0
    },
    "query": {
        "lat": 33.3,
        "lon": 22.5,
        "unit": "celsius",
        "providers": [
            "accuweather",
            "noaa"
        ]
    }
}
```
