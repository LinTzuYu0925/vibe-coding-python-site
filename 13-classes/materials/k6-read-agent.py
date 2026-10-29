# 練習「讀」AI 寫的程式：先不要執行，預測輸出
class Agent:
    def __init__(self, name):
        self.name = name
        self.steps = 0

    def act(self):
        self.steps += 1
        return self.name + " 做了第 " + str(self.steps) + " 步"

    def __str__(self):
        return "Agent(" + self.name + ")"


class SmartAgent(Agent):
    def __init__(self, name, tool):
        super().__init__(name)
        self.tool = tool

    def act(self):
        base = super().act()
        return base + "，使用工具：" + self.tool


a = Agent("小A")
s = SmartAgent("小B", "搜尋")
print(a)
print(s)
print(a.act())
print(s.act())
print(s.act())
print(a.steps, s.steps)
print(isinstance(s, Agent))
