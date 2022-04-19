from flask import Flask, render_template, request
import pickle
#from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        #Kms_Driven2 = np.log(Kms_Driven)
        Owner=int(request.form['Owner'])
        Fuel_Type=request.form['Fuel_Type_Petrol']

        Fuel_Type_Diesel=0
        Fuel_Type_Petrol= 0
        if(Fuel_Type=='Petrol'):
                Fuel_Type_Petrol=1       
        elif Fuel_Type == "Diesel":
            Fuel_Type_Diesel=1

        Year=2022-Year
        Seller_Type_Individual=request.form['Transmission_Mannual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,
        Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="You Can Sell The Car at {} lakhs".format(output))
    
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

