#!flask_ml/bin/python


from api import app
app.run(debug=True, host='0.0.0.0', port=5000)
