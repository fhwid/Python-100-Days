import pygame, os


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    x, y = 50, 50
    # 设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
    screen.fill((242, 242, 242))
    # 通过指定的文件名加载图像
    ball_image = pygame.image.load('c:\\Users\\fanhw1\\PycharmProjects\\Python-100-Days\\Day01-15\\res\\ball.png')
    # 在窗口上渲染图象
    screen.blit(ball_image, (x, y))
    # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
    pygame.display.flip()
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))



if __name__ == '__main__':
    main()


