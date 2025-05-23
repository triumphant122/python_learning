# python_learning
## 《外星人入侵》开发学习过程
1. 规划项目
> 在游戏《外星人入侵》中，玩家控制一艘最初出现在屏幕底部中央
的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键射
击。游戏开始时，一群外星人出现在天空中，并向屏幕下方移动。
玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，
将出现一群新的外星人，其移动速度更快。只要有外星人撞到玩家
的飞船或到达屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船
后，游戏结束。
2. 安装Pygame
```python
$ python -m pip install --user pygame 
#如果是在虚拟环境当中，请将参数 --user 删除。
```
3. 开始游戏项目
### 创建pygame窗口以及响应用户的输入
导入sys模块控制退出游戏。
导入pygame进行绘制游戏屏幕。
```python
 pygame.init()
 # 初始化背景设置
 self.screen = pygame.display.set_mode((1200, 800))
 # 创建一个1200*800的一个屏幕，赋值给属性screen，其对象是一个surface，在Pygame中，surface是屏幕的一部分

 self.bg_color = (230,230,230)
 # 创建了一个背景颜色的属性，在Pygame中，颜色是以RGB值指定的。
```
> sys模块：
  Python中的sys模块是标准库中的一个内置模块，提供了与Python解释器交互的接口。



** 关于虚拟环境，相当与创建了一个环境，环境里的各种包、解释器都是独立与总体环境，可以创建project文件夹，
并且在project文件夹下创建一个alien_invsion的环境，等同与创建了一个新的alien_invasion的文件夹，不过
这个文件自带隔离效果，不需要自己手动建一个alien_ invasion的文件夹，然后在这个文件夹下再去创建文件夹。
我犯的一个错就是自己创建了一个文件夹，又在文件夹下创建了一个虚拟环境，导致我运行py文件需要到我的虚拟
环境文件夹，我更新README时又需要返回上一级文件夹- -！！**

### 创建设置类
创建一个settings的模块，其中包括了一个叫Settings的类，用于储存设置。
创建了设置的类之后需要再主程序文件中创建实例才能访问设置
```python
from settings import Settings # 要引入我们的设置
#  __init__ 方法中进行引用
self.settings = Settings() # 创建一个设置属性，并将设置的类赋值给该属性
# 之后self.screen和屏幕的背景颜色都可以使用设置的类进行管理。
```
### 添加飞船图像
> 在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件
最为简单，因为Pygame默认加载位图。
在创建飞船时，我们使用的飞船不是一个矩形的，但是我们将它当做矩阵一样来处理。
优点是可以简单的判定游戏的元素是否发生了碰撞。
> Ship的方法__init__()接受两个参数：引用self和指向当前AlienInvasion实例的引用。这让Ship
能够访问AlienInvasion中定义的所有游戏资源。

### 在屏幕上绘制飞船
更新alien_invasion.py，创建一艘飞船并调用其方法blitme()：
```python
from ship  from ship import Ship
import Ship
class AlienInvasion:
 """管理游戏资源和行为的类"""
 def __init__(self):
      --snip--
      self.ship = Ship(self)
 def run_game(self):
      --snip--
 # 每次循环时都重绘屏幕。
      self.screen.fill(self.settings.bg_color)
      self.ship.blitme()
```
> 导入Ship类，并在创建屏幕后创建一个Ship实例。调
用Ship()时，必须提供一个参数：一个AlienInvasion实例。在这
里，self指向的是当前AlienInvasion实例。这个参数让Ship能够访
问游戏资源，如对象screen。我们将这个Ship实例赋给了
self.ship。

### 重构方法__check__event()和方法__update_screen()
一个是响应鼠标键盘的方法，一个是更新屏幕的方法
> 辅助方法：辅助方法在类中执行任务，但并非是通过实例调用的。在Python中，辅助方法的名称以
单个下划线打头。
下面是新增方法_check_events()后的AlienInvasion类，只
有run_game()的代码受到影响：
```python
# 修改前代码
def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘和鼠标事件。
            for event in pygame.event.get():  ## 该行代码返回一个列表
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环是都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见。
            pygame.display.flip()
# 修改后代码
def run_game(self):
        """开始游戏主循环"""
        while True:  ## 主重构了原本繁杂的结构，创建了两个新方法，开始时调用创建的方法
            self._check_events()  ##
            self._update_screen()  ## 
            # 每次循环是都重绘屏幕
    def _check_events(self):  ## 响应方法
        """响应按键和鼠标事件。"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()
    def _update_screen(self):  ## 更新屏幕方法
        """更新屏幕上的图像，并切换到最新绘制的屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()
```
  


