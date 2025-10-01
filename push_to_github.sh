#!/bin/bash

# GitHub Push Commands
# Replace YOUR_USERNAME with your actual GitHub username

echo "🚀 Pushing YouTube Short Search Package to GitHub..."
echo "=================================================="

# Add GitHub remote (replace YOUR_USERNAME with your actual username)
git remote add origin https://github.com/YOUR_USERNAME/youtube-short-search-package.git

# Set main branch and push
git branch -M main
git push -u origin main

# Create and push release tag
git tag -a v0.1.0 -m "Release v0.1.0 - Initial release of YouTube Short Search Package"
git push origin v0.1.0

echo "✅ Successfully pushed to GitHub!"
echo "🏷️ Release tag v0.1.0 created"
echo "🌍 Your project is now live on GitHub!"
