def detectUser(user):
    if user.role==1:
        redirect_url="vendordashboard"
        return redirect_url
    if user.role==2:
        redirect_url="custdashboard"
        return redirect_url
    elif user.role==None and user.is_superadmin:
        redirect_url="/admin"
        return redirect_url