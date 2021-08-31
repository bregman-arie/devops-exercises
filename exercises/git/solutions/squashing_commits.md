## Git - Squashing Commits - Solution


1. In a git repository, create a new file with the content "Mario" and commit the change

```
git add new_file
echo "Mario" -> new_file
git commit -a -m "New file"
```

2. Make change to the content of the file you just created so the content is "Mario & Luigi" and create another commit

```
echo "Mario & Luigi" > new_file
git commit -a -m "Added Luigi"
```

3. Verify you have two separate commits - `git log`

4. Squash the two commits you've created into one commit

```
git rebase -i HEAD~2
```

You should see something similar to:

```
pick 5412076 New file
pick 4016808 Added Luigi
```

Change `pick` to `squash`


```
pick 5412076 New file
squash 4016808 Added Luigi
```

Save it and provide a commit message for the squashed commit

### After you complete the exercise

Answer the following:

* What is the reason for squashing commits? - history becomes cleaner and it's easier to track changes without commit like "removed a character" for example. 
* Is it possible to squash more than 2 commits? - yes
