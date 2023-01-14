from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cpp_to_latex():
    if request.method == 'POST':
        code = request.form['code']
        latex_code = '\\documentclass{article}\n'+'\\usepackage{minted}\n'+'\\begin{document}\n'+'\\begin{minted}[bgcolor=gray!30,fontsize=\Large,rulecolor=\color{blue},linenos,escapeinside=||,xleftmargin=5mm,xrightmargin=5mm,numbersep=5mm,frame=lines,framesep=2mm,fontfamily=tt]{c++}\n' + code + '\n\\end{minted}'+ '\n\\end{document}'
        return render_template('index.html', latex_code=latex_code)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
