#!/usr/bin/python


class RemoteControl:
    def __init__(self):
        self.channels = ['hbo', 'star', 'Fox', 'cnn', 'zee', 'republic']
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

if __name__ == '__main__':
    rc = RemoteControl()
    #r = iter(rc)
    #print(next(r))
    #print(next(r))
    #print(next(r))
    #print(next(r))
    #print(next(r))
    #print(next(r))
    #print(next(r))
    for i in rc:
        print(i)














