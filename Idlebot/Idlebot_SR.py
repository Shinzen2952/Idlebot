from flask import Flask, redirect, url_for, render_template

app=Flask(__name__,template_folder='templates')


@app.route('/')
def zero(): 
    return redirect(url_for('web')) 

@app.route('/user/func')
def web():
    return render_template("Idlebot.html")

@app.route('/about_us')
def about():
    return render_template('about_us.html')

@app.route('/blackhole')
def black_holes():
    return render_template('blackhole.html')

@app.route('/SpaceTime')
def space_time():
    return render_template('Space_Time.html')
    
@app.route('/laws_of_motions')
def newton():
    return render_template('laws.html')
@app.route('/physics')
def law_physics():
    return render_template('physics.html')
@app.route('/chemistry')
def chemicals():
    return render_template('chemistry.html')
@app.route('/astronomy')
def astrology():
    return render_template('astronomy.html')
    
if __name__ == '__main__':
    app.run(debug=True)


