# Containerized DB with Persistent Storage

1. Run a container with a database of any type of you prefer (MySql, PostgreSQL, Mongo, etc.)
  1. Use a mount point on the host for the database instead of using the container storage for that
  2. Explain why using the host storage instead of the container one might be a better choice
2. Verify the container is running


## Solution

```
# Create the directory for the DB on host
mkdir -pv ~/local/mysql
sudo semanage fcontext -a -t container_file_t '/home/USERNAME/local/mysql(/.*)?'
sudo restorecon -R /home/USERNAME/local/mysql

# Run the container
podman run --name mysql -e MYSQL_USER=mario -e MYSQL_PASSWORD=tooManyMushrooms -e MYSQL_DATABASE=university -e MYSQL_ROOT_PASSWORD=MushroomsPizza -d mysql -v /home/USERNAME/local/mysql:/var/lib/mysql/db

# Verify it's running
podman ps
```

It's better to use the storage host because in case the container ever gets removed (or storage reclaimed) you have the DB data still available.
