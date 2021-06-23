import enum
class ChannelGroup(enum.Enum):
    CCTV = 1
    LOCAL = 2 #地方台
    HK = 3 #香港
    TAI_WAN = 4 #台湾
    AM = 5 #澳门
    OTHER = 6
    def getName(self):
        if self is ChannelGroup.CCTV:
            return "中央台"
        elif self is ChannelGroup.LOCAL:
            return "地方台"
        elif self is ChannelGroup.HK:
            return "香港台"
        elif self is ChannelGroup.TAI_WAN:
            return "台湾台"
        elif self is ChannelGroup.AM:
            return "澳门台"
        elif self is ChannelGroup.OTHER:
            return "其它台"
        else:
            return ""