# M3U-Helper 用户指南

## 目录

- [**项目地址**](https://github.com/icexmoon/m3u-helper#%E9%A1%B9%E7%9B%AE%E5%9C%B0%E5%9D%80)
- [**用途**](https://github.com/icexmoon/m3u-helper#%E7%94%A8%E9%80%94)
- [**注意事项**](https://github.com/icexmoon/m3u-helper#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)
- [**安装**](https://github.com/icexmoon/m3u-helper#%E5%AE%89%E8%A3%85)
- [**更新**](https://github.com/icexmoon/m3u-helper#%E6%9B%B4%E6%96%B0)
- [**功能**](https://github.com/icexmoon/m3u-helper#%E5%8A%9F%E8%83%BD)
  - [**输出帮助信息**](https://github.com/icexmoon/m3u-helper#%E8%BE%93%E5%87%BA%E5%B8%AE%E5%8A%A9%E4%BF%A1%E6%81%AF)
  - [**格式化m3u文件**](https://github.com/icexmoon/m3u-helper#%E6%A0%BC%E5%BC%8F%E5%8C%96m3u%E6%96%87%E4%BB%B6)
  - [**all-in-one**](https://github.com/icexmoon/m3u-helper#all-in-one)
  - [**可选参数**](https://github.com/icexmoon/m3u-helper#%E5%8F%AF%E9%80%89%E5%8F%82%E6%95%B0)
- [**更新日志**](https://github.com/icexmoon/m3u-helper#%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97)

## 项目地址

pypi：<https://pypi.org/project/m3u-helper-icexmoon/>

Github：<https://github.com/icexmoon/m3u-helper>

个人博客：<https://blog.icexmoon.xyz/archives/189.html>

## 用途

本应用主要用于帮助对m3u或m3u8文件进行相关处理，目前包括：检测链接有效性、排序、分组等。

## 注意事项

- 对电视频道有效性的验证是通过调用`requests`模块的`get`请求实现的，所有在0.1秒内连接，并且http状态不是200的url被认为是有效的电视频道，否则视为无效。

- 有效性验证使用`futures`模块实现多线程，目前线程池数目设置为10。

- 需要注意的是，IPTV的网络通畅程度很大程度上是依赖于具体的电信运营商的，所以很可能不同的m3u电视频道源在不同的电信运营商或者不同的地域下的网络流畅程度是不同的，比如电信的用户可以但联通的用户不能观看，所以本程序应该和最终使用m3u文件进行观看IPTV的设备在同一网络下进行使用。

- 本程序只是帮助自动化处理m3u文件，并不提供IPTV源。

- 目前自动化分组和排序的功能相当初级，推荐先手动进行一定程度的修改，比如将`#EXTINF:-1 ,CCTV1`修改为`#EXTINF:-1 ,CCTV01`，这样能获得更好的排序结果。此外如果需要进一步优化排序和分组结果，可以在issues页面进行反馈。

- 目前对m3u文件的解析使用的是`m3u8`包，经过测试发现该包只能正常解析未进行分组的原始m3u文件，比如:

  ```
  #EXTM3U
  #EXTINF:-1 ,CCTV01
  http://39.134.39.39/PLTV/88888888/224/3221226247/index.m3u8
  #EXTINF:-1 ,CCTV02
  http://39.134.39.39/PLTV/88888888/224/3221226220/index.m3u8
  ```

  如果在频道名称前附加了其它数据的，比如进行了分组的：

  ```
  #EXTM3U
  #EXTINF:-1 group-title="中央台",CCTV01
  http://39.134.39.39/PLTV/88888888/224/3221226247/index.m3u8
  #EXTINF:-1 group-title="中央台",CCTV02
  http://39.134.39.39/PLTV/88888888/224/3221226220/index.m3u8
  ```

  将无法正常解析，此问题可能会在后续迭代中进行解决。

- 本程序需要Python运行环境，如果不知道如何安装，可以阅读[**windows下的python环境安装**](https://blog.icexmoon.xyz/?p=101)。

## 安装

```shell
pip install m3u-helper-icexmoon
```

## 更新

```shell
pip install --upgrade m3u-helper-icexmoon
```

## 功能

> 已添加控制台短命令支持，所有功能均可以通过`pymh`快速调用。比如`python -m m3u_helper -h`与`pymh -h`的效果完全一致。

### 输出帮助信息

```shell
pymh -h
```

### 格式化m3u文件

扫描当前工作目录下的所有m3u和m3u8文件，并生成相应的格式化后的文件，生成的文件将以`_formated`后缀作为文件名。

```shell
pymh
```

> 此命令可以结合多种可选参数，具体见功能>可选参数。

### all-in-one

扫描工作目录下的所有m3u和m3u8文件，并会将其包含的频道进行合并后生成一个汇总后并且经过格式化的m3u文件：`all_in_one_formated.m3u`，无论之前有无此同名文件都将进行覆盖，所以请不要自己编写同名文件。

```shell
pymd -a
```

> 此命令可以结合多种可选参数，具体见功能>可选参数。

### 可选参数

- `-c  --check_connect`：验证链接有效性
- `-o  --order`：对结果进行排序
- `-n  --no_print`：不显示处理过程信息

在没有设置可选参数的情况下，程序的默认处理逻辑是“不验证链接有效性、不对结果进行排序、显示处理过程信息”。

可选参数进行组合使用，比如`pymd -aco`，效果为创建汇总m3u，并且对链接进行验证，对频道进行排序。

## 更新日志

### 0.0.1

创建应用。