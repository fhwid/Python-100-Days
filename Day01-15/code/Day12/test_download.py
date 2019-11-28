from random import randint
from time import time, sleep


def download_task(filename):
    print('start downloading %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s downloaded, %d secs spent.' % (filename, time_to_download))



def main():
    start = time()
    download_task('Python tutial.pdf')
    download_task('forest gump.avi')
    end = time()
    print('totally %.2f seconds spent.' % (end - start))



if __name__ == "__main__":
    main()


