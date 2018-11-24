# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
from aip import AipSpeech
import wave
import paramiko


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def ssh2(ip, username, password, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, password, timeout=5)
        for m in cmd:
             stdin, stdout, stderr = ssh.exec_command(m)
             stdin.write("Y")
             out = stdout.readlines()
          # 以下两行注释用来执行所有命令和脚本的输出，本程序不用所以注视
          #   for o in out:
          #       print o
        print('%s\t服务器登录执行命令成功\n' % (ip))
        ssh.close()
    except:
        print('%s\t服务器登录异常，请检查\n' % (ip))
    return out


class recoder:
    NUM_SAMPLES = 2000  # pyaudio内置缓冲大小
    SAMPLING_RATE = 8000  # 取样频率
    LEVEL = 500  # 声音保存的阈值
    COUNT_NUM = 20  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
    SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
    TIME_COUNT = 20  # 录音时间，单位s

    Voice_String = []

    def savewav(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.SAMPLING_RATE)
        wf.writeframes(np.array(self.Voice_String).tostring())
        # wf.writeframes(self.Voice_String.decode())
        wf.close()

    def recoder(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        save_count = 0
        save_buffer = []
        time_count = self.TIME_COUNT

        while True:
            time_count -= 1
            # print time_count
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(self.NUM_SAMPLES)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum(audio_data > self.LEVEL)
            print(np.max(audio_data))
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.COUNT_NUM:
                save_count = self.SAVE_LENGTH
            else:
                save_count -= 1

            if save_count < 0:
                save_count = 0

            if save_count > 0:
                # 将要保存的数据存放到save_buffer中
                #print  save_count > 0 and time_count >0
                save_buffer.append(string_audio_data)
            else:
                #print save_buffer
                # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
                #print "debug"
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
            if time_count == 0:
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False


""" 你的 APPID AK SK """
APP_ID = '14843209'
API_KEY = 'QloDD6g7Se6FmohU1eeX3rEE'
SECRET_KEY = 'Lxb9Obl1aqbQ571fXoeEweN1Gtz7zO0Q'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

flag = True
piargv = 1
while flag:
    r = recoder()
    r.recoder()
    r.savewav("test.wav")

    # 识别本地文件
    re_dict = client.asr(get_file_content('test.wav'), 'pcm', 16000, {
        'dev_pid': 1536,
    })

    if 'result' not in re_dict:
        continue
    else:
        print(re_dict['result'])
        if ('1' or '一') in re_dict['result'][0]:
            piargv = '1'
            flag = False
        if ('2' or '二') in re_dict['result'][0]:
            piargv = '2'
            flag = False
        if ('3' or '三') in re_dict['result'][0]:
            piargv = '3'
            flag = False
        if ('4' or '四') in re_dict['result'][0]:
            piargv = '4'
            flag = False
        if ('5' or '五') in re_dict['result'][0]:
            piargv = '5'
            flag = False

cmd = ['echo `python3 /home/pi/twr/demo.py {0} >/dev/tty1` >/dev/tty1'.format(piargv)]  # 阅读文件内容，并获得相关md5码
username = 'pi'
password = 'pi'
print("Begin....")
print(cmd[0])
ssh_list = ssh2('192.168.18.48', username, password, cmd)
