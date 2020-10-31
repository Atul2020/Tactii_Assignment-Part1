from flask import Flask,render_template,url_for
from forms import RegistrationForm,loginForm
app= Flask(__name__)
  app.config['SECRET_KEY']='5435rtee45ww0495jtre49tjpbmnt'
posts=[
    {
    'Book_Name':'Diary of a Wimpy Kid',
    'Author':'Jeff Kinney',
    'Price':'Rs 475',
    'DatePostedonBlog':'July 15,2017',
    },
    {
    'Book_Name':'Harry Potter-Deathly Hallows',
    'Author':'J K Rowling',
    'Price':'Rs 600',
    'DatePostedonBlog':'August 19,2017',
    }
]

@app.route("/")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)


@app.route("/login")
def login():
    form=loginForm()
    return render_template('login.html',title='Login',form=form)




if __name__=='__main__':
    app.run(debug=True)
