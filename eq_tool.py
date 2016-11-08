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
        self.p2 = p2
        self.gray = []

    def checkIfNeedEq(self, grayLevel):
        '''
        灰阶数组应该经过概率化
        :param grayLevel: 灰阶数组
        :return: bool
        '''
        self.gray = grayLevel
        p_tmp = sum(grayLevel[:128])
        print(p_tmp)
        return p_tmp < self.p2

    def histogramEq(self, imgBytes):
        # get the min and max value
        minPix = 0
        maxPix = 255
        while self.gray[minPix] == 0 and minPix < 255:
            minPix += 1
        while self.gray[maxPix] == 0 and maxPix > 0:
            maxPix -= 1
        disPix = maxPix - minPix

        # get the accumulative list
        acGray = [0] * 256
        acGray[0] = self.gray[0]
        for i in range(1, 256):
            acGray[i] = self.gray[i] + acGray[i - 1]
        acGray[255] = 1

        # make the equalization result
        eqRe = [0] * len(imgBytes)
        for i in range(0, len(imgBytes)):
            eqRe[i] = round(acGray[imgBytes[i]] * disPix + minPix)

        return bytes(eqRe)

from PIL import Image
def test_main():
    tool = EqTool()
    print("yes")
    img = Image.open('D:/source.jpg').convert('L')
    print("yes")
    imgBytes = img.tobytes()
    grayList = [0] * 256
    amount = len(imgBytes)
    for i in range(0, amount):
        grayList[imgBytes[i]] += 1
    for i in range(0, 256):
        grayList[i] = grayList[i] * 1.0 / amount
    print(tool.checkIfNeedEq(grayList))
    imgBytes = tool.histogramEq(imgBytes)
    img.frombytes(imgBytes)
    img.save("D:/output.jpg")

test_main()