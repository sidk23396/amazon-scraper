# amazon-scraper

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all devices

**Definition**

`GET /logs`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "1",
        "date": "2019-06-23",
        "weight": "81",
        "body_fat": "28"
    },
    {
        "id": "2",
        "date": "2019-06-24",
        "weight": "81",
        "body_fat": "28"
    }
]
```

### Logging a new entry

**Definition**

`POST /logs`

**Arguments**

- `"id":numeric` a globally unique identifier for the log
- `"date":string` date of entry
- `"weight":float` weight in kilograms
- `"body_fat":float` body fat in percentage

If a device with the given identifier already exists, it will send an error message

**Response**

- `201 Created` on success

```json
{
    "id": "2",
    "date": "2019-06-24",
    "weight": "81",
    "body_fat": "28"
}
```
- `403 Forbidden` if failure


## Lookup log details

`GET /log/<id>`

**Response**

- `404 Not Found` if the log does not exist
- `200 OK` on success

```json
{
    "id": "2",
    "date": "2019-06-24",
    "weight": "81",
    "body_fat": "28"
}
```

## Delete a log

**Definition**

`DELETE /log/<id>`

**Response**

- `404 Not Found` if the log does not exist
- `204 No Content` on success
