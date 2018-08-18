# windows api

### 前言

一些特殊场景，非windows不能跑。因此windows也必须管理起来，抽象记录下。


### 内容

> Windows Remote Management

	windows 远程管理（WinRM）是 Microsoft内置的远程管理协议
	
> 快捷开启  [open_winrm.bat](./scripts/open_winrm.bat)


	windows2012 server
	
	使用administrator选择登录后，打开powershell，输入
	
	如果是admin帐户，右击脚本，选择使用管理员运行，同样可以
	
	wget  http://xxxx/open_winrm.bat -outfile  ./open_winrm.bat
	
	然后双击运行即可，输入Y确认即可
	
	
	windows7
	
	1、设置网络属性为工作网络，公网环境无法开启winrm服务
	
	2、打开浏览器，输入 http://xxxx/open_winrm.bat ，选择运行即可
	

> windows api [windows_api.py](./scripts/windows_api.py)
	
	执行方式分为：
	run_cmd：也就是常见的命令行
	run_ps：以字符流的方式读取脚本，执行脚本


### 备注

* windows修改主机名需要重启，请慎重执行
* 附带salt－agent安装脚本，版本可自行指定




