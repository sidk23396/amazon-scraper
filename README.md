# amazon-scraper

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all products

**Definition**

`GET /products`

**Response**

- `200 OK` on success

```json
{
    "data": {
        "products": [
            {
                "id": "ef6a0151385a44bfb22b45bc4c1d6c5a",
                "name": "sony_headphones_wh1000xm3",
                "url": "https://www.amazon.co.uk/Sony-WH-1000XM3-Wireless-Cancelling-Headphones-Black/dp/B07GDR2LYK/ref=sr_1_1?keywords=wh1000xm3&qid=1581884163&sr=8-1"
            },
            {
                "id": "677c16b2fda546c898e59e697b2938a2",
                "name": "samsung_galaxy_note10plus",
                "url": "https://www.amazon.co.uk/Samsung-Hybrid-SIM-6-3-Inch-Android-Smartphone-Aura-Black/dp/B07VVJXTJH/ref=sr_1_3?keywords=note+10+plus&qid=1581893662&sr=8-3"
            }
        ]
    }
}
```

### Adding a new product

**Definition**

`POST /products`

**Arguments**

- `"name":string` name of the product, no whitespaces
- `"url":string` amazon url of product

**Response**

- `201 Created` on success

```json
{
    "data": {
        "product": {
            "id": "76dba5d16b3e4122b0c5387d4d9a2661",
            "name": "product_3_name",
            "url": "product_3_url"
        }
    }
}
```

TODO: Add error responses to send

## Lookup a product

`GET /products/<id:string>`

**Response**

- `404 Not Found` if the product does not exist
- `200 OK` on success

```json
{
    "data": {
        "product": {
            "id": "ef6a0151385a44bfb22b45bc4c1d6c5a",
            "name": "sony_headphones_wh1000xm3",
            "url": "https://www.amazon.co.uk/Sony-WH-1000XM3-Wireless-Cancelling-Headphones-Black/dp/B07GDR2LYK/ref=sr_1_1?keywords=wh1000xm3&qid=1581884163&sr=8-1"
        }
    }
}
```

## Delete a product

**Definition**

`DELETE /products/<id:string>`

**Response**

- `404 Not Found` if the product does not exist
- `204 No Content` on success

## Get prices of a product

**Definition**

`GET /prices/<id:string>`

**Response**

- `404 Not Found` if the product does not exist
- `200 OK` on success

```json
{
    "data": {
        "prices": [
            {
                "price": 306.29,
                "date": "2020-02-16 20:18:10.732512"
            },
            {
                "price": 306.29,
                "date": "2020-02-16 20:18:55.845545"
            }
        ]
    }
}
```
