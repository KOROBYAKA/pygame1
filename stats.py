


class Stats():
    """All stats are here"""
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open ('high_score  ' , 'r') as f:
            self.high_score = int(f.readline())


    def reset_stats(self):
        """reset stats to default value"""
        self.gun_hp = 3
        self.score = 0


