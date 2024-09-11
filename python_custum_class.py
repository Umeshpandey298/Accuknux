class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def __iter__(self):
        """Return an iterator that yields the length and width in the required format."""
        yield {'length': self.length}
        yield {'width': self.width}
    def area(self):
        
        return self.length * self.width
def main():
    try:
            
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        
        rect = Rectangle(length, width)
            
        print("\nIterating over the Rectangle instance:")
        for dimension in rect:
            print(dimension)  

        print(f"Area of the rectangle: {rect.area()}")

    except ValueError:
        print("Please enter valid integer values for length and width.")


if __name__ == "__main__":
     main()

    
        