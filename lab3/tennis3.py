class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, name):
        #sprawdzanie rzeczywistego imienia gracza 
        if name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        #standardowa gra
        if self.player1_points < 4 and self.player2_points < 4 and (self.player1_points + self.player2_points < 6):
            p1_score_name = score_names[self.player1_points]
            
            if self.player1_points == self.player2_points:
                return f"{p1_score_name}-All"
            return f"{p1_score_name}-{score_names[self.player2_points]}"
            
        #remis
        if self.player1_points == self.player2_points:
            return "Deuce"
            
        #kto wygrywa i obliczenie różnicy
        leader = self.player1_name if self.player1_points > self.player2_points else self.player2_name
        point_diff = abs(self.player1_points - self.player2_points)
        
        if point_diff == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"
    
"""
class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1_n if self.p1 > self.p2 else self.p2_n
            return (
                "Advantage " + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
"""