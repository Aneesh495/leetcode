
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return sx <= tx and (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return sy <= ty and (ty - sy) % tx == 0
        return tx == sx and ty == sy
