from wfmh import app

# Checks if the app.py file has executed directly and is not being imported
if __name__ == '__main__':
    app.run(debug=True)
