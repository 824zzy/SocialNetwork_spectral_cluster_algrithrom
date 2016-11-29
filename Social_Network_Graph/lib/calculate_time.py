# encoding=utf-8
import time
#tic 开始计时
def tic():
    globals()['tt'] = time.clock()
    return globals()['tt']

#toc 结束计时并且输出结果
def toc():
    print '\nElapsed time: %.8f seconds\n' % (time.clock()-globals()['tt'])
    return time.clock()-globals()['tt']
