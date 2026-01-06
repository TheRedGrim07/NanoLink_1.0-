from flask import Flask, request, redirect, render_template
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
        existing_link=Link.query.filter_by(original_url=original_url).first()

        if existing_link:
            short_link=existing_link.generate_short_id()
        else:
            new_link=Link(original_url=original_url)

            db.session.add(new_link)
            db.session.commit()

            short_link=new_link.generate_short_id() 

        full_short_link=request.host_url+short_link

        return render_template('index.html', short_url=full_short_link)
    
    
    return render_template('index.html')

@app.route('/<short_link>')
def redirect_to_url(short_link):

    original_url_id=Link.decode_id(short_link=short_link)
    if original_url_id is None:
        return "<h1>404 -Invalid Link</h1>", 404
    
    link=Link.query.get(original_url_id)

    if link:
        return redirect(link.original_url)
            
    return "<h1>404 - Link Not Found</h1>", 404

if __name__=='__main__':
    app.run(debug=True)

