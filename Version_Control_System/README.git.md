

# Git: Version Control Sytem

video link: [Git: Version Control System](https://www.youtube.com/watch?v=SWYqp7iY_Tc)

#### Why need a VCS?
Records the changes made to the code overtime in a special database called repository. We can see who has made the 
changes, when and what changes were made. And if something goes south we can revert back to previous state of the code.
Without version control we have to constantly copy the updated code in different directories and keep track of changes manually.
This is very slow and doesn't scale at all specially if multiple people are working on the same codebase. You have to 
constantly toss around the changes in the code through emails and manually merge them. 

In Nutshell, VCS helps in:
- Track history of changes 
- Work together

Type of VCS:
- Centralized VCS: Subversion, Team foundation server (Code hosted on a single server, single point of failure.)
- Distributed VCS: Git, Mercurial (Every team member has a copy of the codebase and history, even if the central server is off we can still work on the codebase and share with others directly.)

## Git
 - Free
 - Open Source
 - Super Fast
 - Scalable
 - Cheap Branching / Merging

## Using Git
 - The command line
 - Code editors & IDEs
 - GUIs


## Installing Git
- Download from [Git](https://git-scm.com/downloads)

## Configuring Git
- `git config --global user.name "Your Name"`
- `git config --global user.email """
- `git config --global core.editor "code --wait"`


## Git Training

### Initalization and deletition a local repository
  - Create a project directory
  - Initialize a git repository using `git init`
  - You can see what's inside .git directory (the git repository) using `open .git`
  - To remove a git repository use `rm -rf .git`

### Git Workflow
#### Intial Commit:

Git repository `.git` is a hidden subdirectory inside the project directory. When we changes the files in the project
directory,  and we want to save the state of the projectm we can stage the changes and commit them to the repository.
Commit is like taking an  snapshot of the project. 
- Create and add code in file1, file2. 
- Git status to see the status of working dir and staging area. i.e. `git status`. There you will see commits and untracked files that you want to add to the staging area to track.
- Add file1, file2 to staging area. i.e. `git add file1 file2` or `git add *.txt` or `git add .`
- Git status again.
- Commit the changes to the repository. i.e. `git commit -m "inital commit"`

#### Staging:

When we change code in the file, we "add" it into the staging area, where we can review all such modified files 
before committing them to the repository.
- Change code in file1, file2. i.e fixing a bug.
- Add file1, file2 to staging area. i.e. `git add file1 file2`
- Commit the changes to the repository. i.e. `git commit -m "Fixing a bug"`

#### Delete a file from the project directory and staging area:

updated/added files always persists in the staging area, even when we commit. So what if we want to delete the file2 
from everywhere including staging area.
- Remove file2 from the project directory. i.e. `rm file2`
- git ls-files to see the files in the staging area. i.e. `git ls-files`
- Add changes to the staging area. i.e. `git add file2`. This will remove the file2 from the staging area.
- Commit the changes to the repository. i.e. `git commit -m "Removing file2"`

#### Rename or move a file:
- mv file1.txt main.txt
- git status
- git add file1.txt main.txt
- git status
- git commit -m "Renaming file1.txt to main.txt"

Instead of using above use git move.
- `git mv file1.txt main.txt` -> changes both in the project directory and staging area.
- `git status`
- `git commit -m "Renaming file1.txt to main.txt"`

#### Ignoring files:
We don't want to track some files in the project directory. i.e. log files, temp files, build files etc.
- Copy paste all relative paths (from project directory) of the files that you want to ignore in the `.gitignore` file.
- `git status` to see the ignored files.
- `git add .gitignore`
- `git commit -m "Adding .gitignore file"`

#### How to delete a already staged and committed file/dir and add into .gitignore:
Adding a file/dir into .gitignore will not remove it from the staging area or repository. We have to remove it manually.
- `git ls-files`. To see if the file/dir we want to remove is in stagin area.
- `git rm --cached -r bin/` to remove the bin directory from the staging area (indexed dir)
- `git ls-fies` you will see that the bin directory is removed from the staging area.
- `git status` to see the changes.  

#### Git Commit:
Git doesn't store the deltas, it stores the full content every time we commit the changes. But git is very efficient in
storing the snapshots of the project. It compresses the content and doesn't store the duplicate content.

Each commit contains following things
- ID
- Message
- Date/Time
- Author
- Complete snapshot of the project

**Commiting best practices:**
- Commit often. i.e. different commits for different features. i.e. bug fix, feature addition, typo.

#### Git Log:
- `git log` to see the history of commits.
- `git log --oneline` to see the history of commits in one line.
- `git log --oneline --graph` to see the history of commits in one line with graph.

#### Do we need to add the changes to the staging area everytime before commit?**
- No, we can directly commit the changes to the repository using `git commit -am "message"`. This will add all the changes to the staging area and commit them to the repository.
- But this is not recommended as we can't review the changes before committing them to the repository.

#### Push the local repository to remote repository on Github:
- First generate a ssh key pair or use the existing one.
- start the ssh-agent using `eval "$(ssh-agent -s)"`
- `cat ~/.ssh/config` to check which private key has been added to the ssh-agent.
- Copy the public key using `pbcopy < ~/.ssh/id_rsa.pub` and paste it in the github settings.
- `ssh -T git@github.com` to test the connection.
- Create a repository on Github.
- `git remote add origin git@github.com:viveksolanki216/REPONAME.git`
- `git branch -M main`
- `git push -u origin main`

#### Issue with https git urls
https git urls asks for username and passwords everytime you push the changes to the remote repository, even if you had setup the ssh key.
You need to set the ssh url to it i.e.
- `git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
`