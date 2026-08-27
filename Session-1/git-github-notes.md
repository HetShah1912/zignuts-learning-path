# Git & GitHub — Learning Notes

> Learning Path: Zignuts
> Topic: Git & GitHub
> Reference: Complete Git and GitHub Tutorial for Beginners — Apna College

---

## 1. What is Version Control?

**Version Control System (VCS)** is a system that tracks changes made to files over time.

It helps developers:

* Track changes in a project
* Go back to previous versions
* Work on multiple features safely
* Collaborate with other developers
* Maintain a history of changes

### Example

Suppose we have:

```text
project/
├── index.html
├── style.css
└── script.js
```

We make changes to these files every day.

Without version control, it becomes difficult to know:

* What changed?
* Who changed it?
* When was it changed?
* How can I restore the previous version?

Git solves these problems.

---

# 2. What is Git?

**Git is a Distributed Version Control System (DVCS).**

It is installed on our computer and tracks changes in our project.

Git allows us to create versions of our code using **commits**.

### Important

Git ≠ GitHub

* **Git** → Version control software
* **GitHub** → Online platform for hosting Git repositories

---

# 3. What is GitHub?

GitHub is a cloud-based platform where Git repositories can be stored and shared.

It provides features such as:

* Remote repositories
* Collaboration
* Pull Requests
* Issues
* Code reviews
* Project management
* Open-source collaboration

### Simple relationship

```text
Git
 ↓
Tracks changes locally
 ↓
Commit
 ↓
GitHub
 ↓
Stores/shares repository online
```

---

# 4. Git Installation

After installing Git, verify the installation:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

---

# 5. Git Configuration

Before using Git, configure your identity.

### Set username

```bash
git config --global user.name "Your Name"
```

### Set email

```bash
git config --global user.email "your@email.com"
```

### View configuration

```bash
git config --list
```

### Why configure username and email?

Git uses this information to identify who created a commit.

---

# 6. Git Repository

A **repository (repo)** is a project whose changes are tracked by Git.

There are two common types:

### Local Repository

Repository stored on your computer.

### Remote Repository

Repository stored on a service such as GitHub.

```text
Local Repository  ←→  Remote Repository
   Computer              GitHub
```

---

# 7. Creating a Git Repository

Go to the project directory:

```bash
cd project-folder
```

Initialize Git:

```bash
git init
```

This creates a hidden `.git` directory.

```text
project/
├── .git/
├── index.html
└── style.css
```

The `.git` directory contains the information Git needs to track the repository.

### Check repository status

```bash
git status
```

---

# 8. Git Working Areas

Git can be understood using three main areas:

```text
Working Directory
       ↓
   git add
       ↓
Staging Area
       ↓
 git commit
       ↓
Git Repository
```

### Working Directory

The files you are currently working on.

### Staging Area

Files selected for the next commit.

### Repository

The permanent Git history containing commits.

---

# 9. git status

Command:

```bash
git status
```

It tells us:

* Current branch
* Modified files
* Untracked files
* Staged files
* Files ready to commit

This is one of the most useful Git commands.

---

# 10. Git Add

After modifying a file, we need to stage it.

### Add one file

```bash
git add filename
```

Example:

```bash
git add index.html
```

### Add all changed files

```bash
git add .
```

The `.` means the current directory and its contents.

---

# 11. Git Commit

A **commit** saves a snapshot of the staged changes.

```bash
git commit -m "Add homepage"
```

### Structure

```text
git commit -m "message"
│    │       │
│    │       └── Commit message
│    └────────── Commit command
└─────────────── Git
```

A good commit message should clearly describe what changed.

### Good examples

```bash
git commit -m "Add login page"
git commit -m "Fix navbar alignment"
git commit -m "Add user authentication"
```

---

# 12. Git Log

To view commit history:

```bash
git log
```

A shorter version:

```bash
git log --oneline
```

Example:

```text
a83f21d Add login page
72bc91a Fix navbar
4d92abc Initial commit
```

Each commit has a unique identifier called a **commit hash**.

---

# 13. Git Workflow

The basic Git workflow is:

```text
Create / Modify files
        ↓
    git status
        ↓
      git add
        ↓
     git commit
        ↓
      git push
        ↓
      GitHub
```

### Typical commands

```bash
git status
git add .
git commit -m "Describe changes"
git push
```

---

# 14. Connecting Local Repository to GitHub

First create a repository on GitHub.

Then connect your local repository with the remote repository:

```bash
git remote add origin <repository-url>
```

Check the remote:

```bash
git remote -v
```

### `origin`

`origin` is the conventional name given to the remote repository.

It is simply a nickname for the remote URL.

---

# 15. Main Branch

Modern Git repositories commonly use:

```text
main
```

as the default branch.

Rename the current branch:

```bash
git branch -M main
```

### Why use `-M`?

`-M` forcefully renames the current branch.

Example:

```bash
git branch -M main
```

means:

> Rename the current branch to `main`.

---

# 16. Git Push

To upload commits to GitHub:

```bash
git push origin main
```

Breakdown:

```text
git
│
└── push
      │
      ├── origin
      │
      └── main
```

### `git`

Runs Git.

### `push`

Uploads local commits to a remote repository.

### `origin`

The name of the remote repository.

### `main`

The branch to which the commits are pushed.

---

# 17. Upstream Branch

You can connect the local branch with the remote branch using:

```bash
git push -u origin main
```

`-u` means **set upstream**.

After doing this, Git remembers the relationship between the local and remote branch.

Later, you can usually simply use:

```bash
git push
```

instead of:

```bash
git push origin main
```

---

# 18. Git Pull

To download changes from the remote repository and integrate them into your current branch:

```bash
git pull
```

Or explicitly:

```bash
git pull origin main
```

### Basic idea

```text
GitHub
   ↓
git pull
   ↓
Local Repository
```

---

# 19. Git Fetch vs Git Pull

### git fetch

Downloads remote changes but does not automatically merge them.

```bash
git fetch
```

### git pull

Fetches remote changes and integrates them into the current branch.

```bash
git pull
```

Simple difference:

```text
git fetch → Download information
git pull  → Download + integrate changes
```

---

# 20. Branches

A **branch** is an independent line of development.

Branches allow us to work on features without directly modifying the main branch.

Example:

```text
main
 │
 ├── feature-login
 │
 └── feature-payment
```

---

# 21. Create a Branch

```bash
git branch feature-login
```

View branches:

```bash
git branch
```

The current branch is marked with `*`.

---

# 22. Switch Branch

Older/common command:

```bash
git checkout feature-login
```

Modern command:

```bash
git switch feature-login
```

---

# 23. Create and Switch to a Branch

Using checkout:

```bash
git checkout -b feature-login
```

Using switch:

```bash
git switch -c feature-login
```

This creates the branch and switches to it immediately.

---

# 24. Why Use Branches?

Suppose `main` contains stable code.

You want to develop a login feature.

Instead of directly changing `main`:

```text
main
 ↓
feature-login
```

You develop on `feature-login`.

Once the feature is complete and tested, it can be merged into `main`.

---

# 25. Merging Branches

Suppose:

```text
main
feature-login
```

You have completed the login feature.

First switch to the branch that should receive the changes:

```bash
git switch main
```

Then merge:

```bash
git merge feature-login
```

Conceptually:

```text
feature-login
      │
      │ merge
      ↓
     main
```

---

# 26. Merge Conflict

A **merge conflict** occurs when Git cannot automatically determine which changes should be kept.

Example:

Two branches modify the same part of a file differently.

Git may show:

```text
<<<<<<< HEAD
Your current branch changes
=======
Other branch changes
>>>>>>> feature-login
```

You must manually decide which version to keep.

Then:

```bash
git add .
git commit -m "Resolve merge conflict"
```

---

# 27. Deleting a Branch

Delete a local branch:

```bash
git branch -d branch-name
```

Force delete:

```bash
git branch -D branch-name
```

Delete a remote branch:

```bash
git push origin --delete branch-name
```

### Important

Deleting a local branch does **not** automatically delete the remote branch.

---

# 28. .gitignore

`.gitignore` tells Git which files or folders should not be tracked.

Example:

```gitignore
node_modules/
.env
*.log
```

Common things to ignore:

* Dependencies
* Environment variables
* Build files
* Logs
* IDE-specific files
* Secrets

### Never commit secrets

Do not push things such as:

```text
.env
API keys
passwords
private credentials
```

---

# 29. Git Remote

View remote repositories:

```bash
git remote -v
```

Add a remote:

```bash
git remote add origin <URL>
```

Remove a remote:

```bash
git remote remove origin
```

Change a remote URL:

```bash
git remote set-url origin <URL>
```

---

# 30. Git Clone

To copy an existing remote repository to your computer:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/user/project.git
```

This creates a local copy of the repository.

---

# 31. GitHub Collaboration

A common collaborative workflow is:

```text
Repository
     ↓
Create branch
     ↓
Make changes
     ↓
Commit
     ↓
Push branch
     ↓
Pull Request
     ↓
Code Review
     ↓
Merge
```

---

# 32. Pull Request (PR)

A **Pull Request** is a request to merge changes from one branch into another.

Example:

```text
feature-login
      │
      │ Pull Request
      ↓
     main
```

A PR allows developers to:

* Review code
* Discuss changes
* Suggest modifications
* Run automated checks
* Approve changes
* Merge the branch

---

# 33. Fork

A **fork** creates your own copy of someone else's GitHub repository under your GitHub account.

Typical open-source workflow:

```text
Original Repository
        ↓
       Fork
        ↓
Your Repository
        ↓
Clone
        ↓
Make Changes
        ↓
Push
        ↓
Pull Request
```

> Practice this workflow using repositories where contributions are welcome. Avoid creating unnecessary PRs against unrelated production repositories.

---

# 34. Useful Git Commands

| Command                   | Purpose                        |
| ------------------------- | ------------------------------ |
| `git --version`           | Check Git version              |
| `git config --list`       | View Git configuration         |
| `git init`                | Initialize repository          |
| `git status`              | Check repository status        |
| `git add .`               | Stage all changes              |
| `git commit -m "message"` | Create commit                  |
| `git log`                 | View commit history            |
| `git log --oneline`       | Compact commit history         |
| `git branch`              | List branches                  |
| `git branch name`         | Create branch                  |
| `git switch name`         | Switch branch                  |
| `git switch -c name`      | Create and switch branch       |
| `git merge name`          | Merge branch                   |
| `git branch -d name`      | Delete local branch            |
| `git clone URL`           | Clone repository               |
| `git remote -v`           | View remotes                   |
| `git push`                | Upload commits                 |
| `git pull`                | Download and integrate changes |
| `git fetch`               | Download remote information    |

---

# 35. Complete Local → GitHub Workflow

For a new project:

```bash
cd my-project

git init

git branch -M main

git add .

git commit -m "Initial commit"

git remote add origin <repository-url>

git push -u origin main
```

After the repository is connected:

```bash
git add .
git commit -m "Update project"
git push
```

---

# 36. Feature Development Workflow

```bash
git switch -c feature-login

# Make changes

git status

git add .

git commit -m "Add login feature"

git push -u origin feature-login
```

Then create a Pull Request on GitHub.

After approval, merge the feature into `main`.

---

# 37. Important Concepts to Remember

### Git

Local version control system.

### GitHub

Online platform for hosting and collaborating on Git repositories.

### Repository

Project tracked by Git.

### Commit

A saved snapshot of changes.

### Branch

Separate line of development.

### Remote

A repository located somewhere outside your local machine.

### Origin

Common name for the main remote repository.

### Push

Upload local commits to a remote repository.

### Pull

Download and integrate remote changes.

### Fetch

Download remote changes without automatically integrating them.

### Merge

Combine changes from different branches.

### Pull Request

Request to merge changes into another branch.

---

# 38. Mental Model

Remember Git using this flow:

```text
             GitHub
                ↑
              push
                │
          Local Repository
                ↑
             commit
                ↑
          Staging Area
                ↑
             add
                ↑
        Working Directory
```

When receiving changes:

```text
GitHub
   ↓
 fetch / pull
   ↓
Local Repository
```

---

# 39. Quick Revision

```text
git init
```

Start Git tracking in a project.

```text
git status
```

Check what changed.

```text
git add .
```

Stage changes.

```text
git commit -m "message"
```

Save a snapshot.

```text
git push
```

Upload commits.

```text
git pull
```

Get remote changes.

```text
git branch
```

View branches.

```text
git switch -c feature
```

Create and switch to a branch.

```text
git merge feature
```

Merge a branch.

```text
git clone URL
```

Copy a remote repository locally.

---

## 40. Final Takeaway

Git provides a structured way to track and manage changes in software projects. GitHub builds on Git by providing a remote platform for storing repositories and collaborating with other developers.

The most important workflow to remember is:

```text
Modify
  ↓
git status
  ↓
git add
  ↓
git commit
  ↓
git push
  ↓
GitHub
```

For collaboration:

```text
Branch
  ↓
Develop
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

---

## Reference

**Lecture:** Complete Git and GitHub Tutorial for Beginners — Apna College
**Video:** https://youtu.be/Ez8F0nW6S-w

