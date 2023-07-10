import redback_function

@service
def set_invertor_mode(email,password, serialNumber, inverterMode, inverterPower, swVersion):
    if email =='secret':
        email = pyscript.config['secrets']['redback_email']
    if password =='secret':
        password = pyscript.config['secrets']['redback_password']
    if email =='' or password =='' or serialNumber =='' or inverterMode =='' or swVersion =='':
        return 'Error: Missing parameter'
    setInverter = redbackfunction.setInverterMode1(rbEmail= email, rbPassword=password, rbSerialNumber=serialNumber, rbInverterMode=inverterMode, rbInverterPower=inverterPower, rbRossVersion=swVersion)
