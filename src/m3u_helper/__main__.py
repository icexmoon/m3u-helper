import getopt
from .main import Main


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'hco', [
            'help', 'check_connect', 'order'])
    except getopt.GetoptError as e:
        print("获取参数信息出错，错误提示：", e.msg)
        exit()
    mainProcess = Main()
    if len(opts) == 0:
        mainProcess.main()
    else:
        for opt in opts:
            argKey = opt[0]
            argVal = opt[1]
            if argKey == '--help' or argKey == '-h':
                pass
            elif argKey == '--check_connect' or argKey == '-c':
                mainProcess.checkConnect = True
            elif argKey == '--order' or argKey == '-o':
                mainProcess.doOrder = True
            else:
                pass
        mainProcess.main()
    exit()


main()
