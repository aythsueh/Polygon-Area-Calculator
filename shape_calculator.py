class Rectangle:
    def __init__(self, width, height) :
        self.width = width
        self.height = height
        
    def set_width(self, width) : 
        self.width = width

    def set_height(self, height) : 
        self.height = height

    def get_area(self) : 
        area = self.width * self.height
        return area

    def get_perimeter(self) : 
        perimeter =  2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self) : 
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self) : 
        picture = ""
        if self.width > 50 or self.height > 50 :
            picture = "Too big for picture."
        else : 
            i = 0
            while i < self.height : # 0,1,2,...,height
                j = 0
                while j < self.width :  # 0,1,2,...,width
                    picture += "*"
                    j += 1
                picture += "\n"
                i += 1
        return picture

    
    def get_amount_inside(self, shape) : 
        times_width = self.width // shape.width
        times_height = self.height // shape.height
        amnt = times_width * times_height
        return amnt
    
    def __str__(self) :
        display_string = f"Rectangle(width={self.width}, height={self.height})"
        return display_string


class Square(Rectangle):
    def __init__(self, side) :
        self.width = side
        self.height = side

    def set_side(self, side) : 
        self.width = side
        self.height = side

    def __str__(self) :
        display_string = f"Square(side={self.width})"
        return display_string
