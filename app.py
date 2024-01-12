# Import the create_app function from the 'app' module
from app import create_app

# Create the Flask application using the create_app function
app = create_app()

# Check if the script is executed as the main program
if __name__ == '__main__':
    # Run the Flask application on port 5555 with debugging enabled
    app.run(port=5555, debug=True)
