# psd2ccs
cocostudio1.6 for windows 导入psd布局

策划说他们在cocostudio1.6中用uieditor进行布局的时候,很不方便,需要把美术的psd导出来之后,要一边看着原档,一边找着小图对位置.
就做了这样一个小工具,只是方便他们对位置,不用找图.但是第一个版本缺陷太多.如果他们要继续使用,后期再继续添加其它功能.

之所以不采用json.dumps出json文件,是我搞不清楚哪些key是需要用的.就直接用tenjin把原来的json文件替换关键的几个值,如图片链接,与坐标.
纯当练习.

我用的是python版本是2.7.9,因为psd-tools对python33不支持...
Step.

1.  pip install psd-tools

2.  pip install Pillow

3.  到工作目录,把psd拷贝到根目录下

4.  psd2ccs.py *.psd

Warning.

1.  psd不能有中文
2.  没考虑mac的文件路径,全部用的 '\\', cocostudio1.6没有mac版.如果有需要,以后再改
3.  psd中不要用Group,因为还没加cclayer的映射,只有Sprite的映射

