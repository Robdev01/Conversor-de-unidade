from flask import Flask, render_template, request

app = Flask(__name__)

def quilogramas_para_libras(kg):
    return kg * 2.20462

def libras_para_quilogramas(lb):
    return lb / 2.20462

def quilogramas_para_gramas(kg):
    return kg * 1000

def gramas_para_quilogramas(g):
    return g / 1000

def libras_para_oncas(lb):
    return lb * 16

def oncas_para_libras(oz):
    return oz / 16

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        unit = request.form["unit"]
        value = float(request.form["value"])
        
        if unit == "kg_lb":
            result = f"{value} kg = {quilogramas_para_libras(value)} lb"
        elif unit == "lb_kg":
            result = f"{value} lb = {libras_para_quilogramas(value)} kg"
        elif unit == "kg_g":
            result = f"{value} kg = {quilogramas_para_gramas(value)} g"
        elif unit == "g_kg":
            result = f"{value} g = {gramas_para_quilogramas(value)} kg"
        elif unit == "lb_oz":
            result = f"{value} lb = {libras_para_oncas(value)} oz"
        elif unit == "oz_lb":
            result = f"{value} oz = {oncas_para_libras(value)} lb"
        elif unit == "c_f":
            result = f"{value} °C = {celsius_para_fahrenheit(value)} °F"
        elif unit == "f_c":
            result = f"{value} °F = {fahrenheit_para_celsius(value)} °C"
        elif unit == "c_k":
            result = f"{value} °C = {celsius_para_kelvin(value)} K"
        elif unit == "k_c":
            result = f"{value} K = {kelvin_para_celsius(value)} °C"
        elif unit == "f_k":
            result = f"{value} °F = {fahrenheit_para_kelvin(value)} K"
        elif unit == "k_f":
            result = f"{value} K = {kelvin_para_fahrenheit(value)} °F"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
