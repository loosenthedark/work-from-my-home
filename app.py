import os
from wfmh import app

# Checks if the app.py file has executed directly and is not being imported
if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")), debug=0)
