# Containerized DB

1. Run a container with a database of any type of you prefer (MySql, PostgreSQL, Mongo, etc.)
2. Verify the container is running
3. Access the container and create a new table (or collection, depends on which DB type you chose) for students
4. Insert a row (or document) of a student
5. Verify the row/document was added


## Solution

```
# Run the container
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql

# Verify it's running
podman ps

# Add student row to the database
podman exec -it mysql /bin/bash
mysql -u root
use university;
CREATE TABLE Students (id int NOT NULL, name varchar(255) DEFAULT NULL, PRIMARY KEY (id));
insert into Projects (id, name) values (1,'Luigi');
select * from Students;
```
