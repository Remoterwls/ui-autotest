import requests, time, json, hashlib, random
from public.data_generate import DataGenerate


class GetVercode(object):
    """获取验证码"""

    def get_vercode(self, phone):

        # 生成当前timestamp（毫秒级）
        nowtime = str(int(time.time() * 1000))

        # 生成nonce随机字符串
        seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nonce_list = []
        for i in range(16):
            nonce_list.append(random.choice(seed))
        nonce = ''.join(nonce_list)

        # 组合生成密码
        password = nowtime + phone + nonce[5:13]

        # MD5加密，生成最终signature
        md5 = hashlib.md5(password.encode('utf-8')).hexdigest()

        # 模拟请求post，获取验证码
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
            'Content-Type': 'application/json'
        }
        api_url = 'http://www-ceshi.nlfit.cn/v1/gym/send_phone_code/register'
        data = {
            'timestamp': nowtime,
            'phone': phone,
            'nonce': nonce,
            'signature': md5
        }
        res = requests.post(api_url, headers=headers, data=json.dumps(data))  # data格式为json
        ver_code = res.json().get('code')
        return ver_code


if __name__ == "__main__":
    phone = DataGenerate().create_phone()
    code = GetVercode().get_vercode(phone)
    print(code)









