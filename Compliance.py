# Audits and Compliance Frameworks

class ComplianceFramework:
    def __init__(self, name, requirements):
        self.name = name
        self.requirements = requirements

    def check_compliance(self, company):
        """Checks a company's compliance with the framework's requirements."""
        for requirement in self.requirements:
            if not company.complies_with(requirement):
                return False
        return True

class Company:
    def __init__(self, name, policies):
        self.name = name
        self.policies = policies

    def complies_with(self, requirement):
        """Returns True if the company's policies comply with the requirement, False otherwise."""
        return requirement in self.policies

# Test the ComplianceFramework and Company classes
gdpr = ComplianceFramework('GDPR', ['data protection policy', 'consent form', 'data breach notification process'])
company = Company('Acme Inc.', ['data protection policy', 'consent form', 'employee code of conduct'])

# Check the company's compliance with the GDPR framework
print(gdpr.check_compliance(company))
