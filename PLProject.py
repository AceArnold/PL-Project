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
                    print('4. Letter Scale System')

                    self.from_system = input('Enter the number of the grading system you are converting from: ')

                    if self.from_system == '1':
                        print('please enter your grade out of 60')
                        grade = input('Enter your grade: ')

                    elif self.from_system == '2':
                         print('please enter your grade out of 4')
                         grade = input('Enter your grade: ')

                    elif self.from_system == '3':
                          print('please enter your grade out of 100')
                          grade = input('Enter your grade: ')

                    elif self.from_system == '4':
                        print('please enter your grade out of A-F')
                        grade = input('Enter your grade: ')

                    else:
                            print('Invalid grading system')
                            return
                        
                

                  

	
	

Grade_Converter()
