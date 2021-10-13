"""
要件
・map elitesの実装
・アーカイブに保存された全ての個体を記録
・各個体の親データを記録
・各セルの更新回数を記録
・BD空間の可視化機能
・ログ機能
objectives = -np.sum(np.square(solutions), axis=1)で評価

"""

def compute(genotype_dim, evaluate, iteration, bounds, n_dim=2, pool_num=-1, batch_size=1):
    """
    アーカイブAの初期化 {"0_0": [fitness, solution, bd] or Cell}
    for iteration
        if len(archive) <= 初期個体数:
            np.random.uniformでbatch_sizeの個体を初期化
        else:
            アーカイブから親をランダムに選択    
            rand1 = np.random.randint(len(keys), size=params['batch_size'])
            rand2 = np.random.randint(len(keys), size=params['batch_size'])
            子リストXを初期化
            for n in range(0, params['batch_size']):
                # parent selection
                x = archive[keys[rand1[n]]]
                y = archive[keys[rand2[n]]]
                遺伝的操作 mutation + crossover か mutation と　crossoverのみ
                子に追加
            F=[fitness...], BD=[bd...] <- evaluate(X) # evaluateは引数で関数として受け取って並列化する
            for f, bd, X in zip(F, BD, X):
                index = grid(bd, bounds)
                if A[index] = 空 or A[index].fitness < f:
                    A[index] = [f, X, bd]
                    
    return A
    """

    pass
