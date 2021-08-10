# 定义广度优先遍历(层次遍历)方法
    def breadth_travel(self):
        if self.root == None:
            return
        else:
            # 仍然是用队列的方式实现遍历，末端按遍历顺序逐个添加节点，首端逐个弹出先读到的节点
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.item, end = " ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)

