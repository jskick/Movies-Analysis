


# In[3]:


from flask import (
    Flask,
    render_template,
    jsonify)


# In[4]:


from flask_sqlalchemy import SQLAlchemy




# In[6]:


app = Flask(__name__)


# In[7]:


# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie_data.sqlite"

db = SQLAlchemy(app)


# In[8]:


class Movie_data(db.Model):
    __tablename__ = 'movie_data'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)
    production_company = db.Column(db.String)
    director = db.Column(db.String)
    budget = db.Column(db.Integer)
    overview = db.Column(db.String)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    revenue = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    status = db.Column(db.String)
    tagline = db.Column(db.String)
    title = db.Column(db.String)
    vote_average = db.Column(db.Integer)
    vote_count = db.Column(db.Integer)
    profit = db.Column(db.Integer)

    def __repr__(self):
        return '<Movie_data %r>' % (self.name)


# In[9]:


# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


# In[10]:


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("top_movies.html")


# In[11]:


@app.route("/profit")
def profit_data():

    # Query for the top 10
    results = db.session.query(Movie_data.title, Movie_data.profit).order_by(Movie_data.profit.desc()).limit(10).all()

    # Create lists from the query results
    title = [result[0] for result in results]
    profit = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": title,
        "y": profit,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/rating")
def vote_average_data():

    results = db.session.query(Movie_data.title, Movie_data.vote_average).order_by(Movie_data.vote_average.desc()).limit(10).all()

    # Create lists from the query results
    title = [result[0] for result in results]
    vote_average = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": title,
        "y": vote_average,
        "type": "bar"
    }
    return jsonify(trace)


@app.route("/budget")
def budget_data():

    results = db.session.query(Movie_data.title, Movie_data.budget).order_by(Movie_data.budget.desc()).limit(10).all()

    # Create lists from the query results
    title = [result[0] for result in results]
    budget = [int(result[1]) for result in results]

    # Generate the plot trace
    trace = {
        "x": title,
        "y": budget,
        "type": "bar"
    }
    return jsonify(trace)

@app.route('/movie_data.html')
def data():
    return render_template('movie_data.html')
    
@app.route('/movie_search.html')
def movie_search():
    return render_template('movie_search.html')
    
@app.route('/top_movies.html')
def factors():
    return render_template('top_movies.html')

@app.route('/release_date.html')
def release_data():
    return render_template('release_date.html')
    
@app.route('/profit_bubble.html')
def profit_bubble():
    return render_template('profit_bubble.html')
    
@app.route('/profit_bar.html')
def profit_bar():
    return render_template('profit_bar.html')


if __name__ == '__main__':
    app.run(debug=True)






# %%
