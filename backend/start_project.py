import os
import subprocess

# Function to start MongoDB
def start_mongodb():
    try:
        subprocess.run(['net', 'start', 'MongoDB'], check=True)
        print('MongoDB started successfully.')
    except subprocess.CalledProcessError:
        print('Failed to start MongoDB. Please ensure it is installed as a service.')

# Function to install Python dependencies
def install_dependencies():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        print('Python dependencies installed successfully.')
    except subprocess.CalledProcessError:
        print('Failed to install Python dependencies. Please check your setup.')

# Function to start the Flask server
def start_flask():
    try:
        subprocess.run(['python', '-m', 'flask', 'run'], check=True)
        print('Flask server started successfully.')
    except subprocess.CalledProcessError:
        print('Failed to start Flask server. Please check your setup.')

if __name__ == '__main__':
    start_mongodb()
    install_dependencies()
    start_flask() 