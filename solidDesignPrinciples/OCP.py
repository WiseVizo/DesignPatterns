# OCP -> open close principle 

# Before applying OCP (Violation of OCP)

class Report:
    def generate_report(self, report_type):
        if report_type == 'pdf':
            # logic to generate a PDF report
            pass
        elif report_type == 'csv':
            # logic to generate a CSV report
            pass

# After applying OCP

from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class PDFReport(Report):
    def generate_report(self):
        # logic to generate a PDF report
        pass

class CSVReport(Report):
    def generate_report(self):
        # logic to generate a CSV report
        pass

class ExcelReport(Report):
    def generate_report(self):
        # logic to generate an Excel report
        pass

# conclusion -> The Open/Closed Principle states that a class should be open for extension but closed for modification