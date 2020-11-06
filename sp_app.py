import joblib
model = joblib.load('bash-script/salary.pk1')

while True:
    condition = input("\n \n Enter yes to continue : ")
    if condition == "yes":
        exp = input("\n \n Enter experiance for salary to predict : ")
        predict = model.predict([[float(exp)]])
    else:
        exit()
    print()
    print(predict)
