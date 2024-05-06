import pyinputplus as pyip

name = input('請輸入姓名:')
height = pyip.inputFloat('請輸入身高(120~230)(cm):', min=120, max=230)
weight = pyip.inputFloat('請輸入體重(40~170)(kg):', min=40, max=170)

bmi = weight / (height / 100) ** 2
print(f'{name}, 您的BMI: {bmi:.2f}')