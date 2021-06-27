# Sepris Library

## Installation

Clone the repository:

```bash
git clone https://github.com/khodadoustan/SeprisLibraryTest.git
cd SeprisLibraryTest
docker-compose build
```

## Usage

Start the containers:

```bash
docker-compose up -d
```
Get container ID webservice image:
```bash
docker ps -aqf "name=sepristestlibrary_web"
```

Create Django admin superuser:

```bash
docker exec -it CONTAINER_ID python manage.py createsuperuser
```

Hit the browser with:

```bash
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
```

Swagger documentation available on:

```bash
http://127.0.0.1:8000/swagger/
```

### Requested Apis:

- Request all publishers:

```bash
  curl --location --request GET 'http://127.0.0.1:8000/api/publishers/'
  ```

- Request all writers:

```bash  
curl --location --request GET 'http://127.0.0.1:8000/api/writers/'
```

- Request books of specific writer:

```bash
curl --location --request GET 'http://127.0.0.1:8000/api/books/?writers=2'
```

- Request books of specific writers:

```bash
curl --location --request GET 'http://127.0.0.1:8000/api/books/?writers=1,2'
```

- Request books of specific publisher:

```bash
curl --location --request GET 'http://127.0.0.1:8000/api/books/?publisher=2'
```

- Request to add new book:

```bash
  curl --location --request POST 'http://127.0.0.1:8000/api/books/' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "title":"کتاب تست",
  "pages": 340,
  "writers": [1,4],
  "publisher": 1,
  "publish_year": 1390 }'
 ```

<h1>Note:</h1>
This is a test project and not supported any security for apis (like bearer or something).
