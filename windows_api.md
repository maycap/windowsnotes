# windows api

### 前言

一些特殊场景，非windows不能跑。因此windows也必须管理起来，抽象记录下。


### 内容

> Windows Remote Management

	windows 远程管理（WinRM）是 Microsoft内置的远程管理协议
	
> 快捷开启  [open_winrm.bat](./scripts/open_winrm.bat)

	获取 open_winrm.bat, 执行，按需确认	

> windows api [windows_api.py](./scripts/windows_api.py)
	
	执行方式分为：
	run_cmd：也就是常见的命令行
	run_ps：以字符流的方式读取脚本，执行脚本


### 备注

* windows修改主机名需要重启，请慎重执行
* 附带salt－agent安装脚本，版本可自行指定




