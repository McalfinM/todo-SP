# TODO Soul Parking Test

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

ini adalah coding test, menggunakan python versi 3.8

untuk menjalankan ketikan "python -m uvicorn main:app --reload"

## Feature API

- Create Todo
- Update todo
- Deleted Todo
- Get All
- Get One
- Finish Todo

## API

### - Create

URL : localhost:8000/create

Request Body
| key | type |
| ------ | ------ |
| title | string |
| description | string |

### - Update

URL : localhost:8000/update/{id}

Params
| key | type |
| ------ | ------ |
| id | int |

Request Body
| key | type |
| ------ | ------ |
| title | string |
| description | string |

### - Delete

URL : localhost:8000/delete/{id}

Params
| key | type |
| ------ | ------ |
| id | int |

### - Get

URL : localhost:8000/get

### - Get One

URL : localhost:8000/get/{id}

Params
| key | type |
| ------ | ------ |
| id | int |

### - Finish Todo

URL : localhost:8000/finish/{id}

Params
| key | type |
| ------ | ------ |
| id | int |
