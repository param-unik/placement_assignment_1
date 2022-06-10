class File:

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        with open(file = self.file_name, mode = 'r') as file:
            self.data = file.read()
    
    def read_oper(self, mode = 'r' , file_name = ''):
        if file_name == '':
            file_name = self.file_name
        try:
            with open(file = file_name, mode = mode) as file:
                self.data = file.read()
            return self.data 
        except FileNotFoundError as f:
            print('File not found error ', f)
        except IOError:
            print('IO error occured ')
        except Exception as e:
            print('error occured!', e)

    def write_oper(self, file_name = '', mode = 'w'):
        
        if file_name == '':
            file_name = self.file_name

        if mode in ['w', 'w+', 'a']:
            try:
              with open(file = file_name, mode = mode) as file:
                file.write(self.data)
            except FileNotFoundError as f:
                print('File not found error ', f)
            except IOError:
                print('IO error occured ')
            except Exception as e:
                print('error occured!', e)
        else:
            print("mode is incorrect, can't continue")

    def search_replace(self, file_name, search_string, replace_string):
        contents = self.read_oper(file_name = file_name)
        contents = contents.replace(search_string, replace_string)
        print(contents)
        self.data = contents
        self.write_oper(file_name = file_name)



