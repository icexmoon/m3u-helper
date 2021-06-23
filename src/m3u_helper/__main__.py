import getopt
import sys
from .main import Main


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'hcoan', [
            'help', 'check_connect', 'order', 'all', 'no_print'])
    except getopt.GetoptError as e:
        print("获取参数信息出错，错误提示：", e.msg)
        exit()
    mainProcess = Main()
    if len(opts) == 0:
        mainProcess.main()
    else:
        allInOne = False
        for opt in opts:
            argKey = opt[0]
            argVal = opt[1]
            if argKey == '--help' or argKey == '-h':
                mainProcess.showHelpInfo()
                exit()
            elif argKey == '--check_connect' or argKey == '-c':
                mainProcess.checkConnect = True
            elif argKey == '--order' or argKey == '-o':
                mainProcess.doOrder = True
            elif argKey == '--all' or argKey == '-a':
                allInOne = True
            elif argKey == '--no_print' or argKey == '-n':
                mainProcess.print = False
            else:
                pass
        if allInOne:
            mainProcess.allInOne()
        else:
            mainProcess.main()
    exit()


main()
