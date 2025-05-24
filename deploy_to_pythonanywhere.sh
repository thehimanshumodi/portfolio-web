#!/bin/bash

# Automated deployment script for Django project to PythonAnywhere

echo "Starting deployment to PythonAnywhere..."

# Step 1: Install PythonAnywhere CLI if not installed
if ! command -v pa_autoconfigure_django &> /dev/null
then
    echo "PythonAnywhere CLI not found. Installing..."
    pip install pythonanywhere
fi

# Step 2: Configure PythonAnywhere Django app
echo "Configuring PythonAnywhere Django app..."
pa_autoconfigure_django --python=3.10 --nuke --force --noinput --domain=yourusername.pythonanywhere.com .

# Step 3: Push latest code to GitHub (optional, if not already pushed)
echo "Pushing latest code to GitHub..."
git add .
git commit -m "Deploying to PythonAnywhere"
git push origin main

# Step 4: Reload the web app on PythonAnywhere
echo "Reloading web app on PythonAnywhere..."
pa_reload_webapp yourusername.pythonanywhere.com

echo "Deployment completed. Please check your PythonAnywhere dashboard for status."
