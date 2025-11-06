
  # ---------- GitHub Setup for Google Colab ----------
# Author: Mohan Kumar N
# Purpose: Configure GitHub access in Colab using Personal Access Token (PAT)
# Includes: Clone, Commit, Push, and Branch Management

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
# STEP 5: Make your changes, then commit and push
!git add .
!git commit -m "Updated notebook or data"
!git push origin main

# ---------- Branching (for team collaboration) ----------

# Create a new branch (example: feature-branch)
!git checkout -b feature-branch

# Push your branch to remote
!git push origin feature-branch

# Switch back to the main branch
!git checkout main

# Merge your branch into main (after reviewing changes)
!git merge feature-branch

# Push updated main branch
!git push origin main