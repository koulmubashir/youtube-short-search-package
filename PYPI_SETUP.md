# 🚀 Complete PyPI Publishing Setup Guide

## Step 1: Create Accounts

### Test PyPI Account (for testing uploads)
1. Go to: https://test.pypi.org/account/register/
2. Create an account and verify your email
3. Log in to Test PyPI

### Production PyPI Account (for real uploads)
1. Go to: https://pypi.org/account/register/
2. Create an account and verify your email
3. Log in to PyPI

## Step 2: Generate API Tokens

### For Test PyPI:
1. Go to: https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Enter a token name (e.g., "youtube-short-search-token")
4. Select scope: "Entire account" or specific project
5. Copy the generated token (starts with `pypi-`)

### For Production PyPI:
1. Go to: https://pypi.org/manage/account/token/
2. Follow the same process as Test PyPI

## Step 3: Upload to Test PyPI

```bash
# Use the virtual environment's Python and twine
"/Users/mubashirkoul/Library/Mobile Documents/com~apple~CloudDocs/Development/YouTubeShortSearch/.venv/bin/python" -m twine upload --repository testpypi dist/*

# When prompted for username, enter: __token__
# When prompted for password, enter your API token (starts with pypi-)
```

## Step 4: Test Installation from Test PyPI

```bash
# Install from Test PyPI to test
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ youtube-short-search
```

## Step 5: Upload to Production PyPI

```bash
# After testing is successful
"/Users/mubashirkoul/Library/Mobile Documents/com~apple~CloudDocs/Development/YouTubeShortSearch/.venv/bin/python" -m twine upload dist/*

# Use your production PyPI API token
```

## Alternative: Use .pypirc File

Create `~/.pypirc` file for easier authentication:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-production-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-token-here
```

Then you can upload without entering credentials:

```bash
# Upload to Test PyPI
"/Users/mubashirkoul/Library/Mobile Documents/com~apple~CloudDocs/Development/YouTubeShortSearch/.venv/bin/python" -m twine upload --repository testpypi dist/*

# Upload to Production PyPI
"/Users/mubashirkoul/Library/Mobile Documents/com~apple~CloudDocs/Development/YouTubeShortSearch/.venv/bin/python" -m twine upload dist/*
```

## What You Need to Do:

1. ✅ **Package is built and ready** (`dist/` folder contains the files)
2. 🔄 **Create Test PyPI account** at https://test.pypi.org/account/register/
3. 🔄 **Generate API token** in Test PyPI account settings
4. 🔄 **Run upload command** with your token
5. 🔄 **Test installation** from Test PyPI
6. 🔄 **Upload to production** PyPI when ready

The package build was successful - you just need the PyPI credentials to upload!
