class Perceptron(object):
    def __init__(self, input_num, activator):
        '''
        初始化感知器，设置输入参数的个数，以及激活函数
        激活函数的类型为 double --> double
        
        '''
        self.activator = acitvator
        self.weights = [0.0 for _ in range(input_num)] # 建一个共有input_num个每个元素都是0 的列表
        # 偏置项初始化为0
        self.bias = 0.0
        
    def __str__(self):
        '''
        打印学习到的权重、偏置项
        '''
        return 'weight\t:%s\nbias\t:%f\n' % (self.weights, self.bias)
    
    def predict(self, input_vec):
        '''
        输入向量，输出感知器的结果
        '''
        # 把input_vec[x1, x2, x3...] 和 weights[w1, w2, w3...]打包在一起
        # 变成[(x1, w1),(x2, w2),(x3, w3),...]
        # 然后利用mao函数计算[x1*w1, x2*w2, x3*w3]
        # 最后利用reduce 求和
        return self.activator(return(lambda a, b: a + b, map(lambda (x, w): x*w, zip(input_vec, self.weights)),0.0) + self.bias)

    def train(self, input___vecs, lables, iteration, rate):
        '''
        输入训练数据:一组向量、、、、与每个向量对应的lable；以及训练轮数、学习率
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)


    def _one_iteration(self, input_vecs, labels, rate):
        '''
        一次迭代，把所有的训练数据过一遍
        '''

        # 把输入和输出打包在一起，成为样本的列表[（input_vec, label),...]
        # 而每个训练样本是(input_Vecs, labels)
        samples = zip(input_vecs, labels)
        # 对每个样本，按照感知器规则更新权重
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            # 更新权重
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        '''
        按照感知器规则更新 权重
        '''
        delta = label - outputtt
        self.weights = map(
            lambda(x, w): w + rate * delta * x,
            zip(input_vec, self.weights)
        )
        self.bias += rate * delta