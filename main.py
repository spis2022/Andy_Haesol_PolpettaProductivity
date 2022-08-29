from flask import Flask
from flask import render_template
from flask import request
import random
app = Flask(__name__)


@app.route('/')

def render_home():

    return render_template('home.html')


@app.route('/ctof')

def render_ctof():

    return render_template('ctof.html')

@app.route('/ctof_result')

def render_ctof_result():

    try:

        ctemp_result = float(request.args['ctemp'])

        ftemp_result = ctof(ctemp_result)

        return render_template('ctof_result.html', 

                               ctemp=ctemp_result, 

                               ftemp=ftemp_result)

    except ValueError:

        return "Sorry: something went wrong."

@app.route('/ftoc')

def render_ftoc():

    return render_template('ftoc.html')

@app.route('/ftoc_result')

def render_ftoc_result():

    try:

        ftemp_result = float(request.args['ftemp'])

        ctemp_result = ftoc(ftemp_result)

        return render_template('ftoc_result.html',

                              ftemp=ftemp_result, 

                              ctemp=ctemp_result)

    except ValueError:

        return "Sorry: something went wrong."

@app.route('/mtokm')

def render_mtokm():

    return render_template('mtokm.html')

@app.route('/mtokm_result')

def render_mtokm_result():

    try:

        miles_result = float(request.args['miles'])

        kilometers_result = miles_to_km(miles_result)

        return render_template('mtokm_result.html',

                              miles = miles_result, 

                              kilometers = kilometers_result)

    except ValueError:

        return "Sorry: something went wrong."

@app.route('/ranNum')

def render_ranNum():

    return render_template('ran_num_gen.html')

@app.route('/ranNumGen_result')

def render_ranNum_result():

    try:

        max = float(request.args['maximum'])

        num = randomNum(max)

        return render_template('ranNumGen_result.html',
                              
                              maxNum = max,
                              
                              randomNumber = num)
    except ValueError:

        return "Sorry: something went wrong."

def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)

@app.route('/ftoc/<ftemp_str>')

def convert_ftoc(ftemp_str):

    ftemp = 0.0

    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Fahrenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"

def ctof(ctemp):

    return (ctemp * (9/5)) + 32

@app.route('/ctof/<ctemp_str>')

def convert_ctof(ctemp_str):

    ctemp = 0.0

    try:

        ctemp = float(ctemp_str)

        ftemp = ctof(ctemp)

        return "In Celcius: " + ctemp_str + " In Fahrenheit: " + str(ftemp)

    except ValueError:

        return "Sorry. Could not convert " + ctemp_str + " to a number"   

def miles_to_km(miles): 

    return miles * 1.609

@app.route('/mtokm/<miles_str>')

def mtokm(miles_str):
    
    miles = 0.0

    try:

        miles = float(miles_str)

        km = miles_to_km(miles)

        return "In miles: " + miles_str + " In kilometers: " + str(km)

    except ValueError:

        return "Sorry. Could not convert " + miles_str + " to a number"  

def randomNum(limit):
    return int(limit * random.random() + 1)

@app.route('/ranNumGen/<limit_str>')

def ranNumGen(limit_str):

    limit = 0

    try:

        limit = float(limit_str)

        ranNum = randomNum(limit)

        return "Your random number is: " + str(ranNum)

    except ValueError:

        return "Sorry. Could not generate a random number"
        
if __name__ == "__main__":

   app.run(host='0.0.0.0')
    
    