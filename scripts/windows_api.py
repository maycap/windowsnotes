# coding: utf-8
# windows 操作封装接口

import winrm

from config import get_config
from helper.logger import get_logger

Myconfig = get_config()
logger = get_logger('web')

class WinRMAPI(object):

    def __init__(self, host, user, password):
        self.host = host
        self.s = winrm.Session(host, auth=(user, password))


    def run_cmd(self, cmd):
        """
        执行cmd
        :param cmd:
        :return:
        """
        logger.info("WINAPI ip:{0}  cmd:{1}".format(self.host, cmd))
        try:
            r = self.s.run_cmd(cmd)
            logger.info("WINAPI ip:{0}  result:{1}".format(self.host, r))
            if r.status_code == 0:
                return True, r.std_out
            else:
                return False, r.std_err
        except Exception as e:
            return False, e.message


    def run_ps(self, ps_script):
        """
        执行powershell 脚本
        :param ps_script:
        :return:
        """
        logger.info("WINAPI ip:{0}  powershell:{1}".format(self.host, ps_script))
        try:
            r = self.s.run_ps(ps_script)
            logger.info("WINAPI ip:{0}  result:{1}".format(self.host, r))
            if r.status_code == 0:
                return True, r.std_out
            else:
                return False, r.std_err
        except Exception as e:
            return False, e.message


    def get_hostname(self):
        """查询主机名"""

        return self.run_cmd('hostname')


    def update_hostname(self, hostname):
        """
        更新主机名
        :param hostname:
        :return:
        """
        ps_script = """
            Rename-Computer -NewName {} -Restart
        """.format(hostname)

        return self.run_ps(ps_script)


    def install_salt(self, syndic):
        """
        安装salt－minion
        syndic: salt－master
        :return:
        """
        ps_script = """
            $saltversion = "Salt-Minion-2017.7.2-Py2-x86-Setup.exe"
            $source = "{0}/$saltversion"
            $destination = "c:\$saltversion"
            Set-Location c:\

            (New-Object System.Net.WebClient).DownloadFile($source, $destination)

            iex "$destination /S /master={1} /minion-name={2}"
            """.format(Myconfig.WINDOWS_FILE_URL, syndic, self.host)

        return self.run_ps(ps_script)


