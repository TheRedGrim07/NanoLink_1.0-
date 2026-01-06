from flask import Flask, request, redirect
from models import db,Link

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///nanolink.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

with app.app_context():
    db.create_all()

#---APP ROUTES
@app.route('/', methods=['GET','POST'])
def Index():

    if request.method=='POST':
        original_url=request.form.get('url')
        new_link=Link(original_url=original_url)

        db.session.add(new_link)
        db.session.commit()

        short_link=new_link.generate_short_id()
        full_short_link=request.host_url+short_link

        return f"""
        <h1>🚀 Link Shortened!</h1>
        <p>Short Link: <a href="{full_short_link}">{full_short_link}</a></p>
        <a href="/">Shorten Another</a>
        """
    
    # Show the Input Form (Simple HTML string)
    return """
    <h1>🔗 NanoLink</h1>
    <form method="POST">
        <input type="url" name="url" placeholder="Paste long URL here..." required>
        <button type="submit">Shorten</button>
    </form>
    """

@app.route('/<short_link>')
def redirect_to_url(short_link):

    links=Link.query.all()
    for link in links:
        if link.generate_short_id()==short_link:
            return redirect(link.original_url)
    
    return "<h1>404 - Link Not Found</h1>", 404

if __name__=='__main__':
    app.run(debug=True)

