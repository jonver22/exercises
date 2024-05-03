import itertools

class book:
    def __iniit__(self, title, isbn):
        if title.__is_valid_title(title):
            raise RuntimeError('invalid title')
        if isbn.__is_valid_isbn(isbn):
            raise RuntimeError('invalid isbn')
        self.__title == title
        self.__isbn = isbn
    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    def __is_valid_isbn(isbn):
        array = []
        count = 0
        summ = 0
        for number in isbn:
            if 0 <= int(number) <= 9:
                array.append(number)
        if len(digits) != 13:
            return False
        for item in array:
            if count % 2 != 0:
                count += 1
                item = item * 3
                array[count] = item
        for item in array:
            summ = summ + item
        
        
            
            
                
    
    def __is_valid_title(title):
        
    