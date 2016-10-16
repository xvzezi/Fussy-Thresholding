# Fussy Thresholding 
Author : 许泽资 5140379068
## Introduction
 - 实现了CDF(cumulative distribution function)下，图片的Histogram Equalization处理，使得图片像素分布均匀的  
   情况下，不损失原有像的相对分布。
 - 实现了Fussy Thresholding 全部，但membership function 没有采用高斯分布等复杂方式，而是用index function  
   的倒数标识，同样的，值越大，内聚程度越高。
 - 文件包中提供了Otsu's method 与Fussy Thresholding 的方法产生效果图的对比。明显的，Fussy Thresholding的  
   边界标示性更好，更能识别出轮廓。
 - 本论文有些地方让人迷惑。
    - membership function没有提供具体的使用师范， 公式中使用的数学符号没有给与具体集中的交代。虽然  
    精神可以领会，但是难以运用，因而我退而求其次，使用了简单的解决方案。
    - 后面将Fussy set 分配完毕之后，并没有提出threshold 接下来应该怎么得到，这是这篇论文最让人疑惑的。  
    我尝试了1.大小反转后停止，2.取集合最值，3.取集合大小。最终发现第三种方式效果最好

## Python Environment
 - python3
 - pip install Pillow

## Class Definition
 - fussy.py 
    ```python
    class Fussy:
    """
    Fussy
        > 能够利用fussy set理论选出合理的threshold，
        > 并且能够较好的处理渐变灰阶的图像
    """
    def __init__(self, path):
        '''
        打开图像并进行预处理
        :param path: 文件路径
        '''

    def saveTo(self, path):
        '''
        存储到指定路径
        :param path: 文件路径 
        '''
    #实例见本文件test_main()
    ```

 - eq_tool.py 
    ```python 
    class EqTool:
    """
    Fussy Method Helper Functions Set
        > checkIfNeedEq:    给一个灰阶数组，检查是否需要直方图均衡化
        > histogramEq:      给一个灰阶数组，运用常规办法均衡化再返回
        >
    """
    def __init__(self, p2 = 0.2):
        '''
        Get a fussy Tool with given p2 factor
        :param p2: 是否需要直方图均衡化的计算因子
        '''

    def checkIfNeedEq(self, grayLevel):
        '''
        灰阶数组应该经过概率化
        :param grayLevel: 灰阶数组
        :return: bool
        '''

    def histogramEq(self, imgBytes):
        '''
        接受源图像灰阶，返回处理后图像
        :param imgBytes: 源图像灰阶
        :return: bytes
        '''
    #实例见本文件test_main()
    ```