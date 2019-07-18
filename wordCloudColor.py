class WordCloudColorFunctions :
    def __init__(self, count_dict, max_words, font_color_vari_level) :
        self.count_dict = count_dict
        self.normalized_rank_dict = self._normalized_rank_dict(font_color_vari_level, max_words)

    def _get_relative_position(self, high, low, ratio):
        ratio = 1 if ratio>1 else ratio
        position = (low + (high - low) * ratio)%360
        return position if position >= 0 else 360-position

    def _normalized_rank_dict(self, font_color_vari_level, max_words):
        R = 10**font_color_vari_level
        rank_dict = {
            key: rank for rank, key in enumerate(sorted(self.count_dict, key=self.count_dict.get, reverse=True), 1)}
        max_rank = min(max_words, max(rank_dict.values()))
        rank_norm = {
            k : R**-(1-(max_rank-rank+1)/max_rank) for k, rank in rank_dict.items()
        }
        return rank_norm

    #set colorfunc
    def colorfunc_red(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(0,120,self.normalized_rank_dict[word])
        S = self._get_relative_position(80,0,self.normalized_rank_dict[word])
        L = self._get_relative_position(40,20,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_green(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(125,10,self.normalized_rank_dict[word])
        S = self._get_relative_position(50,0,self.normalized_rank_dict[word])
        L = self._get_relative_position(60,20,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_blue(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(235,80,self.normalized_rank_dict[word])
        S = self._get_relative_position(70,0,self.normalized_rank_dict[word])
        L = self._get_relative_position(40,20,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_grey(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(0,0,self.normalized_rank_dict[word])
        S = self._get_relative_position(0,0,self.normalized_rank_dict[word])
        L = self._get_relative_position(20,60,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_rainbow(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(0,300,self.normalized_rank_dict[word])
        S = self._get_relative_position(55,35,self.normalized_rank_dict[word])
        L = self._get_relative_position(50,50,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_rainbow_rev(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(250,550,self.normalized_rank_dict[word])
        S = self._get_relative_position(55,35,self.normalized_rank_dict[word])
        L = self._get_relative_position(50,50,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)

    def colorfunc_pastel(self, word, font_size, position, orientation, random_state=None, **kwargs):
        H = self._get_relative_position(200,500,self.normalized_rank_dict[word])
        S = self._get_relative_position(30,30,self.normalized_rank_dict[word])
        L = self._get_relative_position(60,60,self.normalized_rank_dict[word])
        return "hsl(%d, %d%%, %d%%)" % (H,S,L)
