import random


class DataGenerate(object):
    # 随机生成1个手机号
    def create_phone(self):
        seed = '0123456789'
        phone_list = []
        for i in range(8):
            phone_list.append(random.choice(seed))
        phone_data = '166' + "".join(phone_list)
        return phone_data

    # 随机生成一个字符串（8位）
    def create_str(self):
        seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        str_list = []
        for i in range(8):
            str_list.append(random.choice(seed))
        str_data = ''.join(str_list)
        return str_data

    # 随机生成一个文本（8位）
    def create_txt(self):
        seed = '测试你我哈课私教运动'
        txt_list = []
        for i in range(8):
            txt_list.append(random.choice(seed))
        txt_data = ''.join(txt_list)
        return txt_data

    # 随机生成一个混合数据（英文+数字）8位
    def create_mix(self):
        seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        mix_list = []
        for i in range(8):
            mix_list.append(random.choice(seed))
        mix_data = ''.join(mix_list)
        return mix_data


if __name__ == "__main__":
    a = DataGenerate().create_phone()
    b = DataGenerate().create_str()
    c = DataGenerate().create_txt()
    d = DataGenerate().create_mix()
    print(a, b, c, d)

