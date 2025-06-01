from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

def age(s):
    try:
        if type(s) == float:
            return "That's wrong"
        var = int(s)
        if var < 1 or var > 120:
            return "That's wrong"
    except:
        return "That's wrong"
    return var

def faculties(var):
    HEI = {"ФИТИКС", "фитикс", "ФИТиКС", "ФГО", "фго", "НХИ", "нхи", "ФТНГ", "фтнг"} #Список факультетов можно увеличить
    for i in HEI:
        if i == var:
            return i
    return "That's wrong"
def Groups(var):
    HEI = {"ПИН-241", "пин-241", "ИВТ-241", "ивт-241", "ИВТ-242", "ивт-242", "ИВТ-243", "ивт-243", "ИВТ-244", "ивт-244", "ИСТ-241", "ист-241", "ФИТ-241", "фит-241", "ФИТ-242", "фит-242", "ФИТ-243", "фит-243"} #Список можно увеличить
    for i in HEI:
        if i == var:
            return i
    return "That's wrong"

def names(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var

def secondnames(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var

def lastnames(var):
    if var == " ":
        return "That's wrong"
    try:
        int(var)
        return "That's wrong"
    except:
        try:
            float(var)
            return "That's wrong"
        except:
            return var

@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        str = ""
        firstname = request.form.get('name1')
        secondname = request.form.get('name2')
        lastname = request.form.get('name3')
        age1 = request.form.get('name4')
        faculty = request.form.get('name5')
        group = request.form.get('name6')

        str = "" + names(firstname) + " " + secondnames(secondname) + " " + lastnames(lastname) + " " + age(age1) + " " + faculties(faculty) + " " + Groups(group) + '\n'
        with open('answers.txt', 'a') as file:
            file.write(str)
        return render_template('main.html')

def start():
    app.run(debug=True)