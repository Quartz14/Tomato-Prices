from flask import Flask, request, render_template
import pickle
import numpy as np

#[0 'April',1 'August',2'December',3 feb ,4 jan ,5'July',6'June',7'March',8'May',9'November',10'October',11'September']
#my_dict = {1: 'apple', 2: 'ball'}  print(my_dict['age'])
months = {0: 'April',1: 'August',2:'December',3: 'February' ,4: 'January' ,5: 'July',6: 'June',7: 'March',8: 'May',9: 'November',10: 'October',11:'September'}

areas = {0:'Arasikere', 1:'Bagepalli', 2:'Bangarpet', 3:'Belur',
       4:'Binny Mill (F&V), Bangalore', 5:'Channapatana', 6:'Channarayapatna',
       7:'Chickkaballapura', 8:'Chikkamagalore', 9:'Chintamani', 10:'Davangere',
       11:'Doddaballa Pur', 12:'Gowribidanoor', 13:'Gundlupet', 14:'Hassan',
       15:'Holalkere', 16:'Holenarsipura',17: 'Honnali', 18:'Hoskote',19: 'Hospet',
       20:'Hunsur', 21:'K.R. Pet',22:'K.R.Nagar', 23:'Kanakapura', 24:'Kolar',
       25:'Kollegal', 26:'Kudchi', 27:'Maddur', 28:'Malur', 29:'Mulabagilu',
       30:'Mysore (Bandipalya)', 31:'Nagamangala', 32:'Ramanagara', 33:'Shimoga',
       34:'Somvarpet', 35:'Srinivasapur', 36:'T. Narasipura', 37:'Tarikere',38: 'Tumkur',
       39:'Udupi'}
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('monthly_tomato_home.html')

@app.route('/price',methods=['POST','GET'])
def get_price():
    if request.method=='POST':
        result=request.form
        area = result['area']
        tonnes = result['tonnes']
        month = result['month']

        months = {0: 'April',1: 'August',2:'December',3: 'February' ,4: 'January' ,5: 'July',6: 'June',7: 'March',8: 'May',9: 'November',10: 'October',11:'September'}

        areas = {0:'Arasikere', 1:'Bagepalli', 2:'Bangarpet', 3:'Belur',
         4:'Binny Mill (F&V), Bangalore', 5:'Channapatana', 6:'Channarayapatna',
         7:'Chickkaballapura', 8:'Chikkamagalore', 9:'Chintamani', 10:'Davangere',
        11:'Doddaballa Pur', 12:'Gowribidanoor', 13:'Gundlupet', 14:'Hassan',
        15:'Holalkere', 16:'Holenarsipura',17: 'Honnali', 18:'Hoskote',19: 'Hospet',
        20:'Hunsur', 21:'K.R. Pet',22:'K.R.Nagar', 23:'Kanakapura', 24:'Kolar',
        25:'Kollegal', 26:'Kudchi', 27:'Maddur', 28:'Malur', 29:'Mulabagilu',
        30:'Mysore (Bandipalya)', 31:'Nagamangala', 32:'Ramanagara', 33:'Shimoga',
        34:'Somvarpet', 35:'Srinivasapur', 36:'T. Narasipura', 37:'Tarikere',38: 'Tumkur',
        39:'Udupi'}

        mon = months[int(month)]
        market = areas[int(area)]
        ton = tonnes
        pkl_file = open('monthly_gbr_model.pkl', 'rb')
        logmodel = pickle.load(pkl_file)

        array = np.array([int(month),int(area),float(tonnes),])
        new_array = array.reshape(1,-1)
        prediction2 = logmodel.predict(new_array)
    
        return render_template('tomato_result.html', prediction=prediction2, mon=mon, market=market, ton=ton)
        
        #return render_template('tomato_result.html',prediction=prediction2)

    
if __name__ == '__main__':
    app.debug = True
    app.run()


