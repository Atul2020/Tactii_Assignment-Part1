from flask import Flask,render_template
app= Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)
