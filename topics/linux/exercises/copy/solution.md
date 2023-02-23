# Copy Time

## Objectives

1. Create an empty file called `x` in `/tmp`
2. Copy the `x` file you created to your home directory
3. Create a copy of `x` file called `y`
4. Create a directory called `files` and move `x` and `y` there
5. Copy the directory "files" and name the copy `copy_of_files`
6. Rename `copy_of_files` directory to `files2`
7. Remove `files` and `files2` directories

## Solution

```
touch /tmp/x
cp x ~/
cp x y
mkdir files
cp x files
cp y files
cp -r files copy_of_files
mv copy_of_files files2
rm -rf files files2
```