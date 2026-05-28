from django.shortcuts import render
import sqlite3
import datetime

# Create your views here.
def loadWelcomePage(request):
    return render(request, "WelcomePage.html")
def loadLoginPage(request):
    return render(request,"LoginPage.html")
def loadSignupPage(request):
    return render(request,"SignupPage.html")
def loadUserProfilePage(request):
    con=sqlite3.connect("C:\\Users\\hp\\ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from UserSignupTable"
    result=operations.execute(sql)
    records=result.fetchall()
    con.commit()
    con.close()
    return render(request,"Profile.html",{'list':records})
def loadUserViewsPage(request):
    return render(request,"Views.html")

def loadUserViewsBlogLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from BlogsTable order by BlogId desc "
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"Blogs.html",{'blogs':records})
def loadUserViewsPomodoroLink(request):
    return render(request,"PomodoroTimer.html")
def loadUserUpdateProfilePage(request):
    return render(request,"UpdateUserProfile.html")
def loadUserDeleteProfilePage(request):
    return render(request,"SendReqToDelProfile.html")
def loadUpdateUserProfileActionCode(request):
    userId=request.POST['userId']
    profilePic=request.POST['profilepic']
    emailId=request.POST['emailId']
    dateOfBirth=request.POST['DOB']
    gender=request.POST['gender']
    address=request.POST['address']
    occupation=request.POST['occupation']
    salary=request.POST['salary']
    description=request.POST['description']
    guardianName=request.POST['guardianName']
    guardianEmailId=request.POST['guardianEmailId']
    therapistIncharge=request.POST['inchargeTherapist']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "update UserSignupTable set profilePic=?,emailId=?,dateofbirth=?,gender=?,address=?,occupation=?,salary=?,description=?,guardianName=?,guardianemailId=?,inchargeTherapist=? where userId=?"
    values=(profilePic,emailId,dateOfBirth,gender,address,occupation,salary,description,guardianName,guardianEmailId,therapistIncharge,userId)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"UpdateUserProfile.html")
def loadUserProfileDeletionReqActionCode(request):
    userId=request.POST['userId']
    userRequest=request.POST['request']
    userType="Customer"
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql="insert into DeleteProfileRequestTable values(?,?,?)"
    values=(userId,userRequest,userType)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"SendReqToDelProfile.html")

def loadFeedbackPage(request):
    return render(request,"Feedback2.html")
def loadAppointmentPage(request):

    return render(request, "BookAppointment.html")

def loadNotificationsPage(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from NotificationsTable"
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"Notifications.html",{'list':records})
def loadBookAppointmentActionCode(request):
    userId=request.POST['userId']
    therapistName=request.POST['therapistName']
    appointmentDate=request.POST['appointmentDate']
    appointmentTime=request.POST['appointmentTime']
    status="Pending"
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into AppointmentTable values (?,?,?,?,?)"
    values=(userId,therapistName,appointmentDate,appointmentTime,status)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"BookAppointment.html")

def loadTherapistFeedbackActionCode(request):
    userId=request.POST['userId']
    feedback=request.POST['feedback']
    feedbacktype="For Therapist by Customer"
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into FeedbackTable(userId,feedback,feedbackType) values (?,?,?)"
    values=(userId,feedback,feedbacktype)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"Feedback2.html")
def loadAdminFeedbackActionCode(request):
    userId=request.POST['userId']
    feedback=request.POST['feedback']
    feedbacktype="For Admin by Customer"
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into FeedbackTable(userId,feedback,feedbackType) values (?,?,?)"
    values=(userId,feedback,feedbacktype)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"Feedback2.html")

def loadSignupActionCode(request):
    userId=request.POST['userId']
    userName=request.POST['userName']
    password=request.POST['password']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "insert into UserSignupTable(userId,userName,password) values(?,?,?)"
    values = (userId,userName,password)
    result = operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"LoginPage.html")
def loadLoginActionCode(request):
    userName=request.POST['userName']
    password=request.POST['password']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Select * from UserSignupTable where userName=? and password=?"
    values = (userName, password)
    result = operations.execute(sql, values)
    if(result.fetchone()):
        con.commit()
        con.close()
        return render(request,"UserDashboard.html")
    else:
        con.commit()
        con.close()
        return render(request,"LoginPage.html")

def loadLogoutActionCode(request):
    return render(request, "LoginPage.html")
def loadUserDashboardReturnActionCode(request):
    return render(request,"UserDashboard.html")
def loadUserProfileReturnActionCode(request):
    return render(request,"Profile.html")
#Therapist dashboard responses
def loadTherapistLoginPage(request):
    return render(request,"TherapistLoginPage.html")
def loadTherapistLoginActionCode(request):
    userId = request.POST['userId']
    userName = request.POST['userName']
    password = request.POST['password']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Select * from TherapistSignupTable where TherapistId=? and TherapistName=? and Password=?"
    values = (userId, userName, password)
    result=operations.execute(sql, values)
    if result.fetchone():
        con.commit()
        con.close()
        return render(request,"TherapistDashboard.html")
    else:
        return render(request,"TherapistLoginPage.html")
def loadTherapistSignupPage(request):
    return render(request,"TherapistSignupPage.html")
def loadTherapistSignupActionCode(request):
    userId=request.POST['userId']
    userName=request.POST['userName']
    password=request.POST['password']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into TherapistSignupTable(TherapistId,TherapistName,Password) values(?,?,?)"
    values=(userId,userName,password)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"TherapistSignupPage.html")

def loadTherapistProfilePage(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from TherapistSignupTable"
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"TherapistProfile.html",{'list':records})
def loadTherapistProfileActionCode(request):
    return render(request,"TherapistProfile.html")
def loadTherapistUpdateProfileLink(request):
    return render(request,"UpdateTherapistProfile.html")
def loadUpdateTherapistProfileActionCode(request):
    therapistId=request.POST['therapistId']
    therapistName=request.POST['therapistName']
    password=request.POST['password']
    profilePic=request.POST['profilepic']
    emailId=request.POST['emailId']
    dateOfBirth=request.POST['DOB']
    gender=request.POST['gender']
    experience=request.POST['experience']
    qualifications=request.POST['qualifications']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "update TherapistSignupTable set therapistName=?,password=?,profilePic=?,EmailId=?,DateOfBirth=?,Gender=?,Experience=?,Qualifications=? where TherapistId=? "
    values =(therapistName,password,profilePic,emailId,dateOfBirth,gender,experience,qualifications,therapistId)
    operations.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "UpdateTherapistProfile.html")
def loadTherapistDeleteProfileLink(request):
    return render(request,"TherapistSendReqToDelProfile.html")

def loadTherapistProfileDeletionRequestActionCode(request):
    userId=request.POST['therapistId']
    userRequest=request.POST['request']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "insert into TherapistDeleteProfileRequestTable values(?,?)"
    values = (userId, userRequest)
    operations.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "TherapistSendReqToDelProfile.html")

def loadTherapistBlogLink(request):
    return render(request,"TherapistBlogs.html")

def loadTherapistBlogCreationActionCode(request):
    title=request.POST['title']
    category=request.POST['category']
    content=request.POST['content']
    date=datetime.datetime.now()
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into BlogsTable(Title,Content,Category,Date) values (?,?,?,?)"
    values=(title,category,content,date)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"TherapistBlogs.html",{'message':'Record updated successfully'})

def loadTherapistFeedbackLink(request):
    return render(request,"TherapistFeedback.html")

def loadTherapistFeedbackActionCode(request):
    userId=request.POST['userId']
    feedback=request.POST['feedback']
    feedbackType="For Admin by therapist"
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "insert into FeedbackTable(userId,feedback,feedbackType) values(?,?,?)"
    values = (userId,feedback,feedbackType)
    operations.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "TherapistFeedback.html")

def loadTherapistAppointmentLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Select * from AppointmentTable"
    result=operations.execute(sql)
    records=result.fetchall()
    con.commit()
    con.close()
    return render(request, "TherapistAppointment.html",{'list':records})
def loadTherapistAppointmentActionCode(request):
    userId=request.POST['userId']
    status=request.POST['status']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="update AppointmentTable set status=? where userId=?"
    values=(userId,status)
    operations.execute(sql,values)
    sql2="Select * from AppointmentTable"
    result=operations.execute(sql2)
    records=result.fetchall()
    con.commit()
    con.close()
    return render(request,"TherapistAppointment.html")
def loadTherapistNotificationsLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from NotificationsTable"
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"TherapistNotifications.html",{'list':records})
def loadTherapistNotificationsActionCode(request):
    senderType="Therapist"
    notifications=request.POST['notifications']
    date=datetime.datetime.now()
    recieverType=request.POST['recieverType']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into NotificationsTable(SenderType,Notifications,Date,RecieverType) values (?,?,?,?)"
    values=(senderType,notifications,date,recieverType)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"TherapistNotifications.html")
def loadTherapistLogoutActionCode(request):
    return render(request,"TherapistLoginPage.html")
def loadTherapistDashboardReturnActionCode(request):
    return render(request,"TherapistDashboard.html")
#Admin Dashboard Responses
def loadAdminLoginLink(request):
    return render(request,"AdminLoginPage.html")
def loadAdminLoginActionCode(request):
    adminId=request.POST['userId']
    password=request.POST['password']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Select * from AdminSuperLoginTable where adminId=? and password=?"
    values = (adminId,password)
    result = operations.execute(sql, values)
    if result.fetchone():
        con.commit()
        con.close()
        return render(request, "AdminDashboard.html")
    else:
        return render(request, "AdminLoginPage.html")

def loadAdminBlogsLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from BlogsTable order by BlogId desc "
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"AdminBlogs.html",{'blogs':records})
def loadAdminRequestsLink(request):
    return render(request,"AdminRequests.html")
def loadAdminUserRequestLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from DeleteProfileRequestTable"
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"AdminUserRequests.html",{'list':records})
def loadAdminTherapistRequestLink(request):
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Select * from TherapistDeleteProfileRequestTable"
    result = operations.execute(sql)
    records = result.fetchall()
    return render(request,"AdminTherapistRequests.html",{'list':records})
def loadAdminProfilesLink(request):
    return render(request,"AdminProfiles.html")

def loadAdminUserProfilesLink(request):
    return render(request,"AdminUserProfiles.html")
def loadAdminUserProfileDeletionActionCode(request):
    userId=request.POST['userId']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Delete from DeleteProfileRequestTable where userId=?"
    values=(userId,)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"AdminUserProfiles.html",{'message':'Profile Deleted Successfully'})
def loadAdminTherapistProfilesLink(request):
    return render(request,"AdminTherapistProfiles.html")

def loadAdminTherapistProfileDeletionActionCode(request):
    therapistId = request.POST['therapistId']
    con = sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations = con.cursor()
    sql = "Delete from TherapistDeleteProfileRequestTable where therapistId=?"
    values = (therapistId,)
    operations.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "AdminTherapistProfiles.html", {'message': 'Therapist Profile Deleted Successfully'})
def loadAdminNotificationsLink(request):
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="Select * from NotificationsTable"
    result=operations.execute(sql)
    records=result.fetchall()
    return render(request,"AdminNotifications.html",{'list':records})

def loadAdminNotificationsActionCode(request):
    senderType="Admin"
    notifications=request.POST['notifications']
    date=datetime.datetime.now()
    recieverType=request.POST['recieverType']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    sql="insert into NotificationsTable(SenderType,Notifications,Date,RecieverType) values(?,?,?,?)"
    values=(senderType,notifications,date,recieverType)
    operations.execute(sql,values)
    con.commit()
    con.close()
    return render(request,"AdminNotifications.html",{'alert':'Record inserted successfully'})
def loadAdminFeedbacksLink(request):
    return render(request,"AdminFeedback.html")

def loadAdminFeedbackActionCode(request):
    feedbackType=request.POST['feedbackType']
    con=sqlite3.connect("C:/Users/hp/ManoVijayDatabase.db")
    operations=con.cursor()
    if feedbackType=="For Admin by Customer":
        sql="Select * from FeedbackTable where feedbackType=?"
        values=(feedbackType,)
        result=operations.execute(sql,values)
        record=result.fetchall()
        return render(request,"AdminFeedback.html",{'list':record})
    elif feedbackType=="For Admin by therapist":
        sql = "Select * from FeedbackTable where feedbackType=?"
        values = (feedbackType,)
        result = operations.execute(sql, values)
        record = result.fetchall()
        return render(request, "AdminFeedback.html", {'list': record})
    else:
        return render(request,"AdminFeedback.html",{'message':'Some error occured'})
def loadAdminDashboardReturnLink(request):
    return render(request,"AdminDashboard.html")
def loadAdminRequestsReturnLink(request):
    return render(request,"AdminRequests.html")
def loadAdminProfileReturnLink(request):
    return render(request,"AdminProfiles.html")
def loadAdminLogoutLink(request):
    return render(request,"AdminLoginPage.html")


