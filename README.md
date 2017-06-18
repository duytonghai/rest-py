# Rest-py
Create a simple RESTful api using python and falcon framework

# Install dependencies
Run `pip install -r requirements.txt`

# Run application
1. `cd rest-py`
2. Run `gunicorn main:api -b 127.0.0.1:3979 --reload`
3. Test with end-point `curl -v http://localhost:3979/quote`
