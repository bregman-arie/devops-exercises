

##  Description
Your task is to **compare the contents of two directories** in Linux and find out:
- Which files are **different**.
- Which files are **missing** in one of the directories.
- Whether the two directories are **identical**.

This is useful for:
- Verifying backups.
- Checking if deployment directories match.
- Spotting accidental file changes.

---

##  Command
You can use the **`diff`** command with the `-r` flag to compare directories **recursively**.

```bash
diff -r folder1/ folder2/
