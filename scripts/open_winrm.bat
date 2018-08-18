echo "Now look winrm config"
cmd /c winrm enumerate winrm/config/listener

echo "Now quickconfig"
cmd /c winrm quickconfig

echo "Now edit"
cmd /c winrm e winrm/config/listener

echo "set basic"
cmd /c winrm set winrm/config/service/auth @{Basic="true"}

echo "set unencrypted"
cmd /c winrm set winrm/config/service @{AllowUnencrypted="true"}

pause
