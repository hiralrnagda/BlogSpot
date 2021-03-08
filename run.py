from flaskblog import create_app #now this will work as app is present in __init__.py file

app = create_app()

if __name__ == '__main__' :
     app.run(debug=True) 