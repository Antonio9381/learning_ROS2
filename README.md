# learning_ROS2
following:

https://www.youtube.com/watch?v=QyvHhY4Y_Y8&list=PLunhqkrRNRhYYCaSTVP-qJnyUPkTxJnBt&index=6

https://wiki.sydneyrover.com/docs/guides/fundamentals/03_ros2-launch-files/

## how to start everything
- open vscode new window
- click "f1" button on keyboard, type "wsl", click "wsl: connect to wsl using distro", click "ubuntu-22.04"

## how to use git
### the start
```
git init                  # Create a new repo in current folder
git clone <url>           # Copy a remote repo locally
```
### identify author
```
git config --global user.email "ant938153@gamil.com"
git config --global user.name "Antonio938153"
```
### everyday workflow
```
git status                # See what's changed
git diff                  # See exact line changes (unstaged)
git diff --staged         # See changes you've already staged

git add <file>            # Stage a specific file
git add .                 # Stage everything

git commit -m "message"   # Commit with a message
git commit --amend        # Edit the last commit (message or content)
```
### branching
```
git branch                # List branches
git branch feature/your-task         # Create a branch
git switch feature/your-task         # Switch to a branch (modern)
git switch -c feature/your-task      # Create + switch in one step

git merge <branch>        # Merge branch into current
git rebase <branch>       # Rebase current onto branch
git branch -d feature/your-task      # Delete a branch (safe)
git push origin --delete setup/make_workspace #delete branch on github
```
### remote
```
git remote -v             # List remotes
git fetch                 # Download changes (don't apply)
git pull                  # Fetch + merge
git push                  # Push current branch
git push -u origin <name> # Push new branch and set upstream
```
```
# if you want to set the upstream so future git pull works without arguments:
git branch --set-upstream-to=origin/setup/make_workspace
git pull
```
### undoing things
```
git restore <file>        # Discard unstaged changes to a file
git restore --staged <file> # Unstage a file
git revert <commit>       # New commit that undoes a commit (safe)
git reset --hard HEAD~1   # Delete last commit entirely (destructive)
```
### useful extra
```
git log --oneline --graph # Compact visual history
git stash                 # Temporarily shelve changes
git stash pop             # Bring them back
git cherry-pick <commit>  # Apply a specific commit to current branch
```
---

# Creating and Connecting a GitHub Repository

This guide shows how to take an **existing local folder**, turn it into a Git repository, connect it to GitHub, and push your files.

---

## 1. Go into the folder

Open a terminal and navigate to the folder you want to put on GitHub.

### Windows PowerShell

```powershell
cd "C:\path\to\your\folder"
```

For example:

```powershell
cd "$HOME\Documents\myfile\2026\usyd\sem2\space1"
```

Check that you are in the correct place:

```powershell
pwd
```

and:

```powershell
ls
```

---

## 2. Initialize Git

Turn the folder into a Git repository:

```bash
git init
```

Check it:

```bash
git status
```

You should see something similar to:

```text
On branch master

No commits yet
```

> `git init` does **not** upload anything to GitHub. It only creates a local Git repository.

---

## 3. Create a `.gitignore`

Create:

```text
.gitignore
```

inside the root of your project.

For example, for a LaTeX project:

```gitignore
# LaTeX build files
*.acn
*.acr
*.alg
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.glo
*.glg
*.gls
*.ist
*.lof
*.log
*.lot
*.out
*.run.xml
*.synctex.gz
*.toc

# Temporary files
*.tmp
*.bak
```

Check what Git sees:

```bash
git status
```

Files matched by `.gitignore` should no longer appear as untracked files.

---

## 4. Add your files to Git

Stage everything:

```bash
git add .
```

Check:

```bash
git status
```

You should now see your files under:

```text
Changes to be committed:
```

---

## 5. Make the first commit

```bash
git commit -m "Initial commit"
```

A **commit** is basically a saved checkpoint of your project.

You can view your commits with:

```bash
git log --oneline
```

---

## 6. Create the GitHub repository

Go to GitHub and create a **New repository**.

Choose a repository name, for example:

```text
space1
```

If your local folder already contains files, **do not initialize the GitHub repository with**:

- README
- `.gitignore`
- License

This keeps the remote repository empty and makes the first push easier.

Create the repository.

---

## 7. Connect the local folder to GitHub

GitHub will give you a repository URL similar to:

```text
https://github.com/YOUR-USERNAME/space1.git
```

Add it as your remote:

```bash
git remote add origin https://github.com/YOUR-USERNAME/space1.git
```

Check it:

```bash
git remote -v
```

You should see:

```text
origin  https://github.com/YOUR-USERNAME/space1.git (fetch)
origin  https://github.com/YOUR-USERNAME/space1.git (push)
```

---

## 8. Rename the branch to `main`

```bash
git branch -M main
```

Check:

```bash
git branch
```

You should see:

```text
* main
```

---

## 9. Push to GitHub

For the first push:

```bash
git push -u origin main
```

The `-u` connects your local `main` branch with GitHub's `main` branch.

After this, future pushes only need:

```bash
git push
```

---

# Normal Workflow After Setup

Once everything is connected, you **do not repeat `git init` or `git remote add`**.

After working on your project:

```bash
git status
```

Then:

```bash
git add .
```

Commit:

```bash
git commit -m "Describe what I changed"
```

Push:

```bash
git push
```

So your normal workflow is:

```text
Edit files
   ↓
git status
   ↓
git add .
   ↓
git commit -m "message"
   ↓
git push
   ↓
GitHub updated
```

---

# Getting Changes From GitHub

If the GitHub repository has newer changes:

```bash
git pull
```

A common workflow before starting work is:

```bash
git pull
```

Then work normally:

```bash
git add .
git commit -m "Updated assignment"
git push
```

---

# Useful Commands

### Check repository status

```bash
git status
```

### See commit history

```bash
git log --oneline
```

### See connected GitHub repository

```bash
git remote -v
```

### See current branch

```bash
git branch
```

### See what you changed

```bash
git diff
```

### Stage everything

```bash
git add .
```

### Commit

```bash
git commit -m "My commit message"
```

### Upload commits

```bash
git push
```

### Download changes

```bash
git pull
```

---

# Quick Setup — Existing Folder → New GitHub Repo

For a brand-new local project, the complete sequence is:

```bash
cd "path/to/project"

git init

git add .
git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/YOUR-USERNAME/REPOSITORY.git

git push -u origin main
```

After that, your everyday workflow is simply:

```bash
git pull

# work on files...

git status
git add .
git commit -m "Describe changes"
git push
```

---

# Important: Don't Run `git init` Every Time

You only need:

```bash
git init
```

**once per repository.**

Git creates a hidden directory:

```text
.git/
```

That directory contains the repository information and history.

You can check whether your current folder is already a Git repository with:

```bash
git status
```

If it gives you normal repository information, **do not run `git init` again**.

---

# Important: `.gitignore` Does Not Remove Already Tracked Files

If Git was already tracking a file before you added it to `.gitignore`, adding it to `.gitignore` does not automatically remove it from Git.

For example:

```bash
git rm --cached example.aux
```

removes the file from Git tracking while leaving the actual file on your computer.

For an entire directory:

```bash
git rm -r --cached directory_name
```

Then commit the change:

```bash
git commit -m "Stop tracking generated files"
git push
```

---

# Mental Model

Think of Git and GitHub as separate things:

```text
Your project files
       │
       │ git add
       ▼
   Staging Area
       │
       │ git commit
       ▼
Local Git Repository
       │
       │ git push
       ▼
     GitHub
```

And in reverse:

```text
GitHub
   │
   │ git pull
   ▼
Your local repository/files
```

**Git** manages versions on your computer.

**GitHub** stores and shares your Git repository online.
