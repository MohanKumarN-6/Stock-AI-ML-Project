
 # ---------- GitHub Setup for Google Colab ----------
# Author: Mohan Kumar N
# Purpose: Configure GitHub access in Colab using Personal Access Token (PAT)
# Includes: Clone, Commit, Push, Pull, and Branch Management for Collaboration

import os

# STEP 1: Set your GitHub credentials (replace values below)
os.environ['GITHUB_TOKEN'] = "your_personal_access_token_here"
os.environ['GITHUB_USER'] = "your_github_username"
os.environ['GITHUB_REPO'] = "your_repository_name"

# STEP 2: Configure Git (only once per Colab session)
!git config --global user.email "your_email@example.com"
!git config --global user.name "your_github_username"

# STEP 3: Set remote URL using token for authentication
!git remote set-url origin https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${GITHUB_REPO}.git

# STEP 4: Clone the repository (only once per session)
!git clone https://github.com/${GITHUB_USER}/${GITHUB_REPO}.git
%cd ${GITHUB_REPO}

# ---------- Basic Git Workflow ----------
# STEP 5: Always pull the latest version before making changes
# (Prevents merge conflicts and ensures you work on the latest code)
!git pull origin main

# STEP 6: Make your code or data changes, then stage and commit
!git add .
!git commit -m "Updated notebook or data"

# STEP 7: Push your updates to the main branch
!git push origin main

# ---------- Branching (for team collaboration) ----------
# Create a new branch (for feature or bug fix)
!git checkout -b feature-branch

# Push your branch to remote
!git push origin feature-branch

# Switch back to the main branch
!git checkout main

# Merge your feature branch into main (after review or testing)
!git merge feature-branch

# Push the updated main branch to GitHub
!git push origin main

# ---------- Sync Changes from Remote ----------
# If other collaborators have pushed new commits, use:
!git pull origin main

# This fetches and merges their updates into your local copy.
