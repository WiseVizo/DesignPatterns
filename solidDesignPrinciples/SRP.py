# SRP -> Single Responsibility Process or
# SOC -> Seperation Of Concern

# Before applying SRP

class FileManagerAndAuthenticator:
    def read_file(self, file_path):
        # file reading logic
        pass
    
    def authenticate_user(self, username, password):
        # authentication logic
        pass

# After applying SRP

class FileManager:
    def read_file(self, file_path):
        # file reading logic
        pass

class Authenticator:
    def authenticate_user(self, username, password):
        # authentication logic
        pass

# conclusion-> Principle states that a class should have only one reason to change, meaning that a class should have only one job or responsibility.