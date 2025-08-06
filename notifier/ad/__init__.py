import json
import subprocess as sb

from notifier.config import OU_PATH


def get_max_pwd_age():
    cmd = 'Get-ADDefaultDomainPasswordPolicy|select MaxPasswordAge'
    result = sb.run(["powershell.exe", "-Command", cmd],
                    capture_output=True, text=True).stdout
    result = result.strip().split('\n')[2]
    return int(result.split('.')[0])


def get_data():
    cmd = 'get-aduser -searchbase "%s" -filter * -properties * | ' \
          'Select-Object SamAccountName,PasswordLastSet | ' \
          'ConvertTo-Json'
    result = sb.run(["powershell.exe", "-Command", cmd % OU_PATH],
                    capture_output=True, text=True).stdout
    return json.loads(result)


max_pwd_age = get_max_pwd_age()
