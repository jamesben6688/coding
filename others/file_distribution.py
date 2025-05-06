"""
https://www.1point3acres.com/bbs/thread-1113415-1-1.html Google ng VO 奇怪面经

一个data center 有集群，大概就是需要快速分发文件到所有的机器里。
所有集群星行连接同一个switch ，每个wire bandwidth 一致，求最快分发方式。
我说了个bfs ，面试官认为还不够快，要考虑多并发和fault tolerance
"""

class FileDistribution:
    def __init__(self, machines):
        self.machines = machines  # machines 是一个机器列表
        self.files = {}  # 用于存储每个机器的文件块

    def split_file(self, file):
        # 假设我们将文件分成N块
        file_blocks = [file[i:i+len(file)//4] for i in range(0, len(file), len(file)//4)]
        return file_blocks

    def distribute_file(self, file):
        file_blocks = self.split_file(file)

        # 假设我们采用树形分发结构来分发文件块
        for i, block in enumerate(file_blocks):
            # 分发文件块到机器
            self.files[self.machines[i]] = block
            print(f"分发文件块 {i+1} 到 {self.machines[i]}")

    def get_file(self, machine):
        # 模拟获取文件块
        return self.files.get(machine, None)

# 示例
machines = ['machine1', 'machine2', 'machine3', 'machine4']
file_data = "This is a large file that needs to be distributed across the machines."
distribution = FileDistribution(machines)

# 分发文件
distribution.distribute_file(file_data)

# 查询某台机器的文件块
print(distribution.get_file('machine1'))

