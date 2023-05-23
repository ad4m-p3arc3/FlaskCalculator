from flask import Blueprint, request, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")
    numbers = []

@views.route("/calculate" ,methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        final = 0
        numbers = ""
        function = ""
        if request.form.get('num1') == 1:
            numbers.append(1)
        elif request.form.get('num2') == 2:
            numbers.append(2)
        elif request.form.get('num3') == 3:
            numbers.append(3)
        elif request.form.get('num4') == 4:
            numbers.append(4)
        elif request.form.get('num5') == 5:
            numbers.append(5)
        elif request.form.get('num6') == 6:
            numbers.append(6)
        elif request.form.get('num7') == 7:
            numbers.append(7)
        elif request.form.get('num8') == 8:
            numbers.append(8)
        elif request.form.get('num9') == 9:
            numbers.append(9)
        elif request.form.get('num0') == 0:
            numbers.append(0)
        elif request.form.get('plus' == "+"):
            function = "+"
        elif request.form.get('equals') == "=":
            if function == "+":
                numbers.split()
                final = numbers[0] + numbers[2]
        return render_template("index.html", value=final)
    else:
        return render_template("index.html")






'''@views.route("/calculation/<number1>/<function>/<number2>")
def calculate(number1, function, number2):
    number1 = int(number1)
    number2 = int(number2)
    numbers.append(number1)
    numbers.append(number2)
    if function == "+":
        calculation = numbers[0] + numbers[1]
    return render_template("index.html", calculate=calculation)'''

