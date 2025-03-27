print('hello world')

class Grade_Converter:
            def __init__(self, grade, from_system, to_system, grading_systems):
                self.grading_systems = grading_systems
                self.grade = grade
                self.from_system = from_system
                self.to_system = to_system

            def convert_grade(self, grade, from_system, to_system):
                    print('Please select the grading system you are converting from:')
                    print('1. National System')
                    print('2. GPA System')
                    print('3. Percentage System')
                    print('4. 4.0 Scale System')

                    self.from_system = input('Enter the number of the grading system you are converting from: ')
                    if self.from_system == '1':
                        self.from_system = 'National System'
                    elif self.from_system == '2':
                        self.from_system = 'GPA System'
                    elif self.from_system == '3':
                        self.from_system = 'Percentage System'
                    elif self.from_system == '4':
                        self.from_system = '4.0 Scale System'
                    else:
                        print('Invalid input. Please try again.')
                        self.from_system = input('Enter the number of the grading system you are converting from: ')
                

                  

	
	

Grade_Converter()
