from PIL import Image
from Fussy.eq_tool import EqTool

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
        self.image = Image.open(path).convert('L')
        self.gray = self.image.tobytes()
        self.amount = len(self.gray)

        # check if needs equalization, do it
        self.check_eq()

        # statistics
        sta = [0] * 256
        for i in range(0, 256):
            sta[self.gray[i]] += 1

        # probabilities
        for i in range(0, 256):
            sta[i] = sta[i] * 1.0 / self.amount

        # find out the L and R
        valueL = 0
        valueR = 0
        p1 = 0.4
        for i in range(0, 128):
            valueL += sta[i]
        for i in range(128, 256):
            valueR += sta[i]
        valueL = p1 * valueL
        valueR = p1 * valueR
        tmpL = 0
        tmpR = 0
        for i in range(0, 128):
            tmpL += sta[i]
            if tmpL >= valueL:
                valueL = i
                break
        for i in range(0, 128):
            tmpR += sta[255 - i]
            if tmpR >= valueR:
                valueR = 255 - i
                break

        # begin threshold processing
        left = list(range(0, valueL + 1))
        right = list(range(valueR, 256))
        l_mean = 0
        r_mean = 0
        l_prob, r_prob = (tmpL, tmpR)
        for i in left:
            l_mean += i * sta[i]
        for i in right:
            r_mean += i * sta[i]

        # init value alpha
        lt = l_mean / l_prob
        rt = r_mean / r_prob
        l_f = 0
        r_f = 0
        for i in left:
            l_f += abs(lt - i)
        for i in right:
            r_f += abs(rt - i)
        alpha = r_f / l_f

        ptr = valueL + 1
        print(ptr)
        print(valueR)
        print(alpha)

        while ptr < valueR:
            left.append(ptr)
            lt = l_mean + ptr * sta[ptr]
            lt = lt / (l_prob + sta[ptr])
            l_f = 0
            for i in left:
                l_f += abs(lt - i)

            right.append(ptr)
            rt = r_mean + ptr * sta[ptr]
            rt = rt / (r_prob + sta[ptr])
            r_f = 0
            for i in right:
                r_f += abs(rt - i)

            if l_f * alpha < r_f:
                right.pop()
                l_mean += ptr * sta[ptr]
                l_prob += sta[ptr]
            else:
                left.pop()
                r_mean += ptr * sta[ptr]
                l_prob += sta[ptr]
            ptr += 1

        self.threshold = len(left)
        print(self.threshold)

    def saveTo(self, path):
        newImg = [0] * self.amount
        for i in range(0, self.amount):
            if self.gray[i] >= self.threshold:
                newImg[i] = 255
        self.image.frombytes(bytes(newImg))
        self.image.save(path)

    def check_eq(self):
        tool = EqTool()
        # statistics
        sta = [0] * 256
        for i in range(0, 256):
            sta[self.gray[i]] += 1
        if tool.checkIfNeedEq(sta):
            print("need equalization...")
            print("processing...")
            self.gray = tool.histogramEq(self.gray)



def test_main():
    pro = Fussy("D:/source.jpg")
    pro.saveTo("D:/ala.jpg")

test_main()