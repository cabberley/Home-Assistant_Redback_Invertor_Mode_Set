from bs4 import BeautifulSoup
import requests

@pyscript_executor

def setInverterMode1(rbEmail, rbPassword, rbSerialNumber,  rbInverterMode,  rbInverterPower, rbRossVersion):
    loginUrl = "https://portal.redbacktech.com/Account/Login"
    configureurl = 'https://portal.redbacktech.com/productcontrol/Configure?serialNumber=' + rbSerialNumber
    inverterSetUrl = 'https://portal.redbacktech.com/productcontrol/Index'
    s = requests.Session()
    redbackLogin = s.get(loginUrl)
    soup = BeautifulSoup(redbackLogin.content , features="html.parser")
    form = soup.find("form", class_="login-form")
    hidden_input = form.find("input", type="hidden")
    globalAntiForgeryToken = hidden_input.attrs['value']
    redbackReq = s.post(loginUrl, data={"Email": rbEmail, "Password": rbPassword,"__RequestVerificationToken": globalAntiForgeryToken})
    redbackReq.raise_for_status()
    redbackSetInverter = s.get(configureurl)
    redbackSetInverter.raise_for_status()
    soup = BeautifulSoup(redbackSetInverter.content , features='html.parser')
    globalAntiForgeryToken = soup.find('form', id='GlobalAntiForgeryToken')
    hidden_input = globalAntiForgeryToken.find("input", type="hidden")
    globalAntiForgeryToken = hidden_input.attrs['value']
    inverterOperationType='Set'
    headers = {'X-Requested-With': 'XMLHttpRequest', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Referer': 'https://portal.redbacktech.com/productcontrol/Configure?serialNumber=' + rbSerialNumber}
    body = {'SerialNumber': rbSerialNumber,'AppliedTariffId':'','InverterOperation[Type]':inverterOperationType,'InverterOperation[Mode]':rbInverterMode, 'InverterOperation[PowerInWatts]':rbInverterPower, 'InverterOperation[AppliedTarrifId]':'','ProductModelName': '','RossVersion':rbRossVersion,'__RequestVerificationToken': globalAntiForgeryToken} 
    redbackSetInverter = s.post(inverterSetUrl, data = body,headers = headers)
    redbackSetInverter.raise_for_status()
    return redbackSetInverter.text
