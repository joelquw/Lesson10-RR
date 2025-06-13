Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, request
... import pandas as pd
... 
... list_of_companies_df = pd.read.csv("crunchbase_odm_orgs.csv")
... 
... app = Flask ("city_request")
... @app.route('/form', methods=['GET', 'POST'])
... def form():
...     if request.method == 'GET':
...         return '''<form method="POST">
...                     <label for ="city">Enter name of city:</label>
...                     <input type="text" id="citiy" name="city">
...                     <input type="submit">Submit</button>
...                 </form>
...                 '''
...     else:
...         try:
...             city = request.form.get["city"]
...             filter_city = list_of_companies_df[list_of_companies_df["city"] == city]
...             
...             return jsonify(filter_city.to_dict(orient="records"))
...         
SyntaxError: multiple statements found while compiling a single statement
>>> 
... 

================================ RESTART: Shell ================================
>>> app.run(host='localhost', port=5008)
... 

================================ RESTART: Shell ================================
