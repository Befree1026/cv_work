import train

def get_n_params(train):
    pp=0
    for p in list(train.parameters()):
        nn=1
        for s in list(p.size()):
            nn = nn*s
        pp += nn
    return pp