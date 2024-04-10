from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    from main import data_frame_dict
    stud = len(data_frame_dict['Студенты СПО'].index)
    ped = len(data_frame_dict['Педагогические работники СПО'].index)
    soc = len(data_frame_dict['Социальные партнеры СПО'].index)
    sh =  len(data_frame_dict['школьники'].index)

    return render_template("index.html",stud=stud,ped=ped,soc=soc,sh=sh)


@app.route("/que", methods=["POST"])
def que():
    question = request.form.get('submit_button')
    from main import get_sample_and_delete
    q = get_sample_and_delete(question)['Вопрос'].astype('category').values[0]

    return render_template("que.html",q=q)



if __name__ == "__main__":
    app.run(debug=True)
