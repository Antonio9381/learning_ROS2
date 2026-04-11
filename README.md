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
git push --set-upstream origin learn/vid7
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
