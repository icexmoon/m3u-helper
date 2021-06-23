import os


class Config:
    instance: "Config" = None

    @classmethod
    def getInstance(cls) -> "Config":
        """单例模式，返回一个Config单例"""
        if cls.instance == None:
            cls.instance = cls()
        return cls.instance

    def getProjectHomePath(self):
        """获取项目目录"""
        part = __file__.rpartition('\\')
        return part[0]

    def getCurrentUserWorkDirPath(self):
        """获取当前用户的工作目录"""
        return os.getcwd()

    def getDirSep(self):
        return os.sep

    def getHelpFilePath(self):
        """返回帮助文档的路径"""
        return "{}{}{}".format(self.getProjectHomePath(), self.getDirSep(), "help.info")
