from flask import Flask, render_template, request,redirect,session
import datetime
import random
from DBConnection import Db
app = Flask(__name__)
app.secret_key="abc"


@app.route('/',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        qry=db.selectOne("select * from login where username='"+username+"' and password='"+password+"'")
        if qry is not None:
            if qry['u_type']=='admin':
                session['log'] = "lo"
                return '''<script>alert('LOGIN SUCCESSFULLY');window.location="/admin_home"</script>'''
            elif qry['u_type'] == 'parent':
                session['log'] = "lo"
                session['lid'] = qry['login_id']
                return '''<script>alert('LOGIN SUCCESSFULLY');window.location="/parent_home"</script>'''
            elif qry['u_type'] == 'center':
                session['log'] = "lo"
                session['lid']=qry['login_id']
                return '''<script>alert('LOGIN SUCCESSFULLY');window.location="/center_home"</script>'''
            else:
                '''<script>alert('INVALID USER');window.location="/"</script>'''
        else:
            return '''<script>alert("USER NOT FOUND");window.location="/"</script>'''
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session['log']=""
    return redirect('/')



@app.route('/admin_home')
def admin_home():
    if session['log'] == "lo":
        return render_template('admin/admin_home.html')
    else:
        return redirect('/')



@app.route('/add_center',methods=['get','post'])
def add_center():
    if session['log'] == "lo":
        if request.method == "POST":
            cname=request.form['textfield']
            place=request.form['textfield2']
            pincode=request.form['number']
            phn=request.form['number2']
            email=request.form['textfield3']
            password=random.randint(0000,9999)
            db=Db()
            res=db.insert("insert into login VALUES ('','"+email+"','"+str(password)+"','center')")
            db.insert("insert into center VALUES ('"+str(res)+"','"+cname+"','"+place+"','"+pincode+"','"+phn+"','"+email+"')")
            return '''<script>alert("CENTER ADDED");window.location="/admin_home"</script>'''
        else:
            return render_template('admin/add_center.html')
    else:
        return redirect('/')


@app.route('/view_center')
def view_center():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from center")
        return render_template('admin/view_center.html',data=res)
    else:
        return redirect('/')


@app.route('/update_center/<a>',methods=['get','post'])
def update_center(a):
    if session['log'] == "lo":
        if request.method=="POST":
            cname = request.form['textfield']
            place = request.form['textfield2']
            pincode = request.form['number']
            phone = request.form['number2']
            email = request.form['textfield3']
            db = Db()
            db.update("update center set center_name='"+cname+"',center_place='"+place+"',center_pincode='"+pincode+"',phone_no='"+phone+"',email='"+email+"' where center_id='"+a+"'")
            return '''<script>alert("CENTER UPDATED");window.location="/view_center"</script>'''
        else:
            db=Db()
            res=db.selectOne("select * from center where center_id='"+a+"'")
            return render_template('admin/update_center.html', data=res)
    else:
        return redirect('/')


@app.route('/delete_center/<a>')
def delete_center(a):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from center where center_id='"+a+"'")
        return redirect('/view_center')
    else:
        return redirect('/')


@app.route('/view_vaccine')
def view_vaccine():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from vaccine,center where vaccine.center_id=center.center_id")
        return render_template('admin/view_vaccine.html',data=res)
    else:
        return redirect('/')


@app.route('/view_baby')
def view_baby():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from baby,parent where baby.parent_id=parent.parent_id ")
        return render_template('admin/view_baby.html',data=res)
    else:
        return redirect('/')




@app.route('/send_notification',methods=['get','post'])
def send_notification():
    if session['log'] == "lo":
        if request.method=="POST":
            notification=request.form['textarea']
            db=Db()
            db.insert("insert into notification VALUES ('','"+notification+"',curdate())")
            return '''<script>alert('ADDED SUCCESSFULLY');window.location="/admin_home"</script>'''
        else:
            return render_template('admin/send_notification.html')
    else:
        return redirect('/')


@app.route('/view_report')
def view_report():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from report,center,vaccine,baby where report.vaccine_id=vaccine.vaccine_id and vaccine.center_id=center.center_id and report.baby_id=baby.baby_id")
        return render_template('admin/view_report.html',data=res)
    else:
        return redirect('/')



# ///////////////////////////////////////////////////////////////PARENT///////////////////////////////////////////////////

@app.route('/parent_home')
def parent_home():
    if session['log'] == "lo":
        return render_template('parent/parent_home.html')
    else:
        return redirect('/')


@app.route('/register',methods=['get','post'])
def register():
    if request.method=="POST":
        parent_name=request.form['textfield']
        house_name=request.form['textfield2']
        place=request.form['textfield3']
        post=request.form['textfield4']
        pincode=request.form['number1']
        mob_no=request.form['number2']
        email_id=request.form['textfield5']
        password=request.form['textfield8']
        db=Db()
        s=db.insert("insert into login values ('','"+ email_id +"','"+password+"','parent')")
        db.insert("insert into parent VALUES ('"+str(s)+"','" + parent_name + "','" + house_name + "','" + place + "','" + post + "','" + pincode + "','" + mob_no + "','" + email_id + "')")
        return '''<script>alert("REGISTERED SUCCESSFULLY");window.location="/"</script>'''
    else:
        return render_template('parent/register.html')



@app.route('/baby_register',methods=['get','post'])
def baby_register():
    if session['log'] == "lo":
        if request.method=="POST":
            baby_name=request.form['textfield']
            dob=request.form['date']
            gender=request.form['RadioGroup1']
            weight=request.form['textfield2']
            db=Db()
            db.insert("insert into baby VALUES ('','"+str(session['lid'])+"','" + baby_name + "','" + dob + "','" + gender + "','" + weight + "')")
            return '''<script>alert('ADDED SUCCESSFULLY');window.location="/parent_home"</script>'''
        else:
            return render_template('parent/baby_register.html')
    else:
        return redirect('/')


@app.route('/baby_view')
def baby_view():
    if session['log'] == "lo":
        db=Db()
        res = db.select("select * from baby where baby.parent_id='"+str(session['lid'])+"'")
        return render_template('parent/baby_view.html',data=res)
    else:
        return redirect('/')


@app.route('/update_baby/<a>',methods=['get','post'])
def update_baby(a):
    if session['log'] == "lo":
        if request.method=="POST":
            baby_name = request.form['textfield']
            dob = request.form['date']
            gender = request.form['RadioGroup1']
            weight = request.form['textfield2']
            db = Db()
            db.update("update baby set baby_name='"+baby_name+"',dob='"+dob+"',gender='"+gender+"',weight='"+weight+"' where baby_id='"+a+"'")
            return '''<script>alert("BABY UPDATED");window.location="/parent_home"</script>'''
        else:
            db=Db()
            res=db.selectOne("select * from baby where baby.parent_id='"+str(session['lid'])+"' and baby.baby_id='"+a+"'")
            return render_template('parent/update_baby.html',data1=res)
    else:
        return redirect('/')


@app.route('/delete_baby/<a>')
def delete_baby(a):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from baby where baby_id='"+a+"'")
        return redirect('/baby_view')
    else:
        return redirect('/')


# @app.route('/parent_view_report')
# def parent_view_report():
#     db=Db()
#     db.select("select * from report,baby WHERE ")




@app.route('/parent_view_vaccine/<baby_id>')
def parent_view_vaccine(baby_id):
    if session['log'] == "lo":
        db = Db()
        res=db.selectOne("select * from baby where baby_id='"+baby_id+"'")
        res2 = db.select("select * from vaccine,center where vaccine.center_id=center.center_id")
        age=res['dob']
        print(age)

        if "year" in age:
            age=age.strip("years").strip("year").strip(" ")
            ar = []
            for i in res2:
                i_age= i['age_group']
                print("Year : ",i_age)
                if "year" in i_age:
                    i_age = i_age.strip("years").strip("year").strip(" ")
                    # age_list = i_age.split(",")
                    # print("bbbbbbb",age_list)
                    if int(i_age) == int(age):
                        ar.append(i)
        elif "month" in age:
            age=age.strip("months").strip("month").strip(" ")
            ar = []
            for i in res2:
                i_age= i['age_group']
                if "month" in i_age:
                    i_age=i_age.strip("months").strip("month").strip(" ")
                    print("Months : ",i_age)
                    age_list=i_age.split("-")
                    if int(age_list[0]) <= int(age) and int(age) <= int(age_list[1]):
                        print(int(age_list[0]),int(age))
                        ar.append(i)
        return render_template('parent/view_vaccine.html',data=ar, baby_id=baby_id)
    else:
        return redirect('/')



@app.route('/request_vaccine/<baby_id>/<v>',methods=['get','post'])
def request_vaccine(baby_id,v):
    if session['log'] == "lo":
        db = Db()
        db.insert("insert into request VALUES ('','"+str(baby_id)+"','"+str(v)+"',curdate(),'pending')")
        return '''<script>alert("REQUEST ADDED");window.location="/baby_view"</script>'''
    else:
        return redirect('/')


@app.route('/parent_view_report')
def parent_view_report():
    db=Db()
    res=db.select("select * from report,center,vaccine,baby where report.vaccine_id=vaccine.vaccine_id and vaccine.center_id=center.center_id and report.baby_id=baby.baby_id and baby.parent_id='"+str(session['lid'])+"'")
    return render_template('parent/view_report.html',data=res)


@app.route('/view_not')
def view_not():
    db=Db()
    res=db.select("select * from notification")
    return render_template('parent/view_notification.html',data=res)



# /////////////////////////////////////////////////////////CENTER//////////////////////////////////////////////////////



@app.route('/center_home')
def center_home():
    if session['log'] == "lo":
        return render_template('vaccine_center/center_home.html')
    else:
        return redirect('/')


@app.route('/add_vaccine',methods=['get','post'])
def add_vaccine():
    if session['log'] == "lo":
        if request.method == "POST":
            vname=request.form['textfield']
            date=request.form['textfield2']
            slot=request.form['textfield3']
            age=request.form['textfield4']
            db=Db()
            db.insert("insert into vaccine VALUES ('','"+vname+"','"+str(session['lid'])+"','"+slot+"','"+date+"','"+age+"')")
            return '''<script>alert("VACCINE ADDED");window.location="/center_home"</script>'''
        else:

            return render_template('vaccine_center/add_vaccine.html')
    else:
        return redirect('/')


@app.route('/center_view_vaccine')
def center_view_vaccine():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from vaccine where vaccine.center_id='"+str(session['lid'])+"'")
        return render_template('vaccine_center/view_vaccine.html',data=res)
    else:
        return redirect('/')


@app.route('/update_vaccine/<a>',methods=['get','post'])
def update_vaccine(a):
    if session['log'] == "lo":
        if request.method=="POST":
            vname = request.form['textfield']
            date = request.form['textfield2']
            slot = request.form['textfield3']
            age = request.form['textfield4']
            db = Db()
            db.update("update vaccine set vaccine_name='"+vname+"',slot='"+slot+"',date='"+date+"',age_group='"+age+"' where vaccine_id='"+a+"'")
            return '''<script>alert("VACCINE UPDATED");window.location="/center_view_vaccine"</script>'''
        else:
            db=Db()
            res=db.selectOne("select * from vaccine where vaccine.center_id='"+str(session['lid'])+"' and vaccine_id='"+a+"'")
        return render_template('vaccine_center/update_vaccine.html', data=res)
    else:
        return redirect('/')



@app.route('/delete_vaccine/<a>')
def delete_vaccine(a):
    if session['log'] == "lo":
        db=Db()
        db.delete("delete from vaccine where vaccine_id='"+a+"'")
        return redirect('/center_view_vaccine')
    else:
        return redirect('/')


@app.route('/center_view_baby')
def center_view_baby():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from baby,parent where baby.parent_id=parent.parent_id")
        return render_template('vaccine_center/view_baby.html',data=res)
    else:
        return redirect('/')


@app.route('/view_request')
def view_request():
    if session['log'] == "lo":
        db=Db()
        res=db.select("select * from request,baby,vaccine where request.baby_id=baby.baby_id and request.vaccine_id=vaccine.vaccine_id  and vaccine.center_id='"+str(session['lid'])+"'")
        return render_template('vaccine_center/view_request.html',data=res)
    else:
        return redirect('/')


@app.route('/accept_request/<a>/<v>')
def accept_request(a,v):
    if session['log'] == "lo":
        db=Db()
        db.update("update request set status='approved' where request_id='"+a+"'")
        db.update("update vaccine set slot=slot-1 WHERE vaccine_id='"+v+"'")

        return '''<script>alert("REQUEST APPROVED");window.location="/view_request"</script>'''
    else:
        return redirect('/')

@app.route('/reject_request/<a>')
def reject_request(a):
    if session['log'] == "lo":
        db=Db()
        db.update("update request set status='out of stock' where request_id='"+a+"'")
        return '''<script>alert("REPLIED");window.location="/view_request"</script>'''
    else:
        return redirect('/')



@app.route('/upload_report/<vid>/<b>',methods=['get','post'])
def upload_report(vid,b):
    if session['log'] == "lo":
        if request.method=="POST":
            report=request.files['fileField']
            date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
            report.save(r"C:\Users\ruzai\PycharmProjects\baby_vaccination\static\pic\\"+date+'.pdf')
            ss="/static/pic/"+date+'.pdf'
            db=Db()
            db.insert("insert into report VALUES ('','"+str(vid)+"','"+str(b)+"',curdate(),'"+str(ss)+"')")
            return '''<script>alert('ADDED SUCCESSFULLY');window.location="/center_home"</script>'''
        else:
            return render_template('vaccine_center/upload_report.html')
    else:
        return redirect('/')


@app.route('/center_view_report')
def center_view_report():
    db=Db()
    res=db.select("select * from report,vaccine,baby where report.vaccine_id=vaccine.vaccine_id and report.baby_id=baby.baby_id and vaccine.center_id='"+str(session['lid'])+"'")
    return render_template('vaccine_center/view_report.html',data=res)


@app.route('/delete_report/<r>')
def delete_report(r):
    db=Db()
    db.delete("delete from report where report_id='"+r+"'")
    return '''<script>alert("DELETED");window.location="/center_view_report"</script>'''


if __name__ == '__main__':
    app.run(port=4000)
