## Git - Squashing Commits - Solution

1. In a git repository, create a new file with the content "Mario" and commit the change:

```
echo "Mario" > new_file
git add new_file
git commit -m "New file"
```

2. Make a change to the content of the file you just created so it becomes "Mario & Luigi," then create another commit:

```
echo "Mario & Luigi" > new_file
git commit -a -m "Added Luigi"
```

3. Verify you have two separate commits by running:

```
git log
```

4. Squash the two commits you've created into one commit:

```
git rebase -i HEAD~2
```

You should see something similar to:

```
pick 5412076 New file
pick 4016808 Added Luigi
```

Change `pick` to `squash`:

```
pick 5412076 New file
squash 4016808 Added Luigi
```

Save it and provide a commit message for the squashed commit.

> **Note**: If running `git rebase -i HEAD~2` returns a fatal error (e.g., "invalid upstream 'HEAD~2'"), that usually means your second commit is actually the root commit and there's no valid parent before it. In that case, you can either:
> * Use `git rebase -i --root` to allow rewriting the root commit, **or**
> * Create an initial commit before these two commits so that `HEAD~2` points to valid commits.

### After you complete the exercise

**Answer the following:**

* **What is the reason for squashing commits?**  
  History becomes cleaner and it's easier to track changes without many small commits like "removed a character," for example.

* **Is it possible to squash more than 2 commits?**  
  Yes.
