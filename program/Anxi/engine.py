import math


class MyMath():


    def fade(t):
        """Коэффициент интерполяции
        t находится в пределах [0,1]"""
        return 6 * t**5 - 15 * t**4 + 10 * t**3
    

    def lerp(a, b, t):
        """Линейная интерполяция между точками a и b по коэффициенту t
        Фактически возвращает такую точку c, для которой отношения отрезка ac к отрезку ab равняется t
        t находится в пределах [0,1]"""
        return a + t*(b-a)
    

    def gradient(hash,x,y,z):
        """Функция возвращает результат вычисления скалярного произведения,
        который представляет собой величину изменения значения шума в данной точке в соответствии с выбранным градиентом
        hash - хэш координаты"""
        vectors = [[1,1,0],[-1,1,0],[1,-1,0],[-1,-1,0],
                   [1,0,1],[-1,0,1],[1,0,-1],[-1,0,-1],
                   [0,1,1],[0,-1,1],[0,1,-1],[0,-1,-1]]
        
        grad = vectors[hash%12]
    

    def perlin_noise(self,noise_map,x,y,z):

        # Границы карты 255 x 255 x 255
        X_limit_value = math.floor(x) & 255
        Y_limit_value = math.floor(y) & 255
        Z_limit_value = math.floor(z) & 255

        x -= math.floor(x)
        y -= math.floor(y)
        z -= math.floor(z)

        x_fade = self.fade(x)
        y_fade = self.fade(y)
        z_fade = self.fade(z)